import argparse
import glob
import json
import os
import re
from typing import Union, Optional

import pandas as pd
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError

parser = argparse.ArgumentParser(description="Apache access log parser")

parser.add_argument("-l", "--log_file", type=str, help="Log file name")
parser.add_argument("-p", "--path", default=".", type=str, help="Logs dir path")

args = parser.parse_args()


class LogItem(BaseModel):
    ip: str
    datetime: str
    method: str
    request_path: str
    response_code: str
    bytes: Optional[Union[int, str]] = None
    referer: str
    user_agent: str
    spent_time: Optional[Union[int, str]] = None


class ReportResult(BaseModel):
    requests_count: int
    by_methods_count: dict[list, int]
    most_requests_ips: list[str]
    slowest_requests: list[dict[str, str]]


parts = [
    r"(?P<ip>\S+)",
    r"(\S+)",
    r"(\S+)",
    r"\[(?P<datetime>[\w:/]+\s[+\-]\d{4})\]",
    r"\"(?P<method>.*?)",
    r"(?P<request_path>.*?)",
    r"(?P<response_code>\d{3})",
    r"(?P<bytes>\S+)",
    r"(?P<referer>\S+)",
    r"(?P<user_agent>.*)",
    r"(?P<spent_time>\d+)",
]
pattern = re.compile(r"\s+".join(parts))


def main():
    log_data: list[dict[str, any]] = []

    for filename in glob.glob(os.path.join(args.path, args.log_file)):
        print(f"Processing {filename} log file...")
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            for i, line in enumerate(f):
                line = pattern.match(line).groupdict()
                try:
                    log_data.append(LogItem(**line).dict())
                except ValidationError as e:
                    print("error: ", e)
                    print(f"line: {i}", line)
                    break

        df = pd.DataFrame(log_data)
        methods_group = df.groupby("method")["method"].count()

        result = json.dumps(
            {
                "requests_count": len(log_data),
                "by_methods_count": methods_group.to_dict(),
                "most_requests_ips": df["ip"].value_counts()[:3].index.tolist(),
                "slowest_requests": df.nlargest(3, "spent_time")[
                    ["method", "request_path", "ip", "datetime", "spent_time"]
                ].to_dict("records"),
            },
            indent=4,
        )

        with open(f"result-{filename.split('/')[-1]}.json", "w") as f:
            f.write(result)

        print(result)


if __name__ == "__main__":
    main()
