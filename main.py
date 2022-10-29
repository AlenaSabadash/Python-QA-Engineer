import socket
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus

http_response = "Request Method: {}\r\n" "Request Source: {}\r\n" "Response Status: {}"


def start_server():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)

    print("Сервер запущен\n")

    try:
        while True:
            conn, address = server_socket.accept()
            with conn:
                data = conn.recv(1024).decode().split("\r\n")
                if not data:
                    break

                request, *rest = data
                method, path, version = request.split()
                query_params = parse_qs(urlparse(path).query)

                status = 200
                if status_ := query_params.get("status"):
                    try:
                        status = int(status_[0])
                    except ValueError:
                        conn.send(f"{status_[0]} невалидный статус\r\n".encode())

                try:
                    response_status = HTTPStatus(status)
                except ValueError as e:
                    conn.send(str(e).encode())
                    continue

                resp = "\r\n".join(
                    [
                        http_response.format(
                            method,
                            address,
                            f"{response_status} {response_status.phrase}",
                        ),
                        *rest,
                    ]
                )
                conn.send(resp.encode())
    except KeyboardInterrupt:
        print("\nСервер выключен")


if __name__ == "__main__":
    start_server()
