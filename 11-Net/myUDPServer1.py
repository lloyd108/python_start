import socket


def server_func():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = ("127.0.0.1", 6666)
    skt.bind(addr)

    data, addr_from = skt.recvfrom(500)
    print(data, type(data), sep="/////")
    text = data.decode("utf-8")
    print(text, type(text), sep="/////")

    rsp = "Message recived..."
    data = rsp.encode("utf-8")
    skt.sendto(data, addr_from)


if __name__ == "__main__":
    print("Starting server...")

    while True:
        try:
            server_func()
        except Exception as e:
            print(e)

    print("Server stopped...")
