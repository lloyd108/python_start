import socket


def client_func():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = ("127.0.0.1", 6666)

    msg = "Message sending..."
    data = msg.encode("utf-8")
    skt.sendto(data, addr)

    data, addr_from = skt.recvfrom(20)

    text = data.decode()

    print(text)


if __name__ == "__main__":
    client_func()
