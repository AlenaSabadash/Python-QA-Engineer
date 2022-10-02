import sys
import subprocess
from datetime import datetime
from itertools import groupby


class ProcessReport:
    def __init__(self):
        self.processes = self.__get_processes()

    @staticmethod
    def __get_processes():
        output = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE).stdout.readlines()
        headers = [h for h in " ".join(output[0].decode().strip().split()).split() if h]
        raw_data = map(lambda s: s.decode().strip().split(None, len(headers) - 1), output[1:])
        return [dict(zip(headers, r)) for r in raw_data]

    def __get_users(self):
        user_set = {p["USER"] for p in self.processes}
        return list(user_set)

    def __users_processes_count(self):
        groups = {}
        data = sorted(self.processes, key=lambda x: x["USER"])
        for k, g in groupby(data, lambda x: x["USER"]):
            groups[k] = len(list(g))

        return groups

    def __get_process_usage_totals(self, key):
        return sum([float(p[key]) for p in self.processes])

    def __get_most_usage(self, key):
        return sorted(self.processes, key=lambda x: x[key], reverse=True)[0]["COMMAND"]

    def result(self):
        out = sys.stdout
        with open(f"{datetime.now().strftime('%d-%m-%Y-%H:%M')}-scan.txt", "w") as f:
            sys.stdout = f

            print("Отчёт о состоянии системы:")
            print(f"Пользователи системы: {', '.join(self.__get_users())}")
            print(f"Процессов запущено: {len(self.processes)}")

            print("Пользовательских процессов:")
            for k, v in self.__users_processes_count().items():
                print(f"{k}: {v}")

            print(f"Всего памяти используется: {self.__get_process_usage_totals('%MEM'):.2f}%")
            print(f"Всего CPU используется: {self.__get_process_usage_totals('%CPU'):.2f}%")

            print(f"Больше всего памяти использует: {self.__get_most_usage('%MEM')[:20]}")
            print(f"Больше всего CPU использует: {self.__get_most_usage('%CPU')[:20]}")

        sys.stdout = out


def main():
    ProcessReport().result()


if __name__ == "__main__":
    main()
