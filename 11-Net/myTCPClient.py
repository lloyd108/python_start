import socket
from datetime import datetime as dt


def tcp_client():
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 6677)
    skt.connect(addr)

    msg = "Client msg is {0}".format(dt.now())
    msg = msg.encode()
    skt.send(msg)

    rst = skt.recv(200)
    print(rst.decode())

    skt.close()


if __name__ == "__main__":
    print("TCP client started...")
    tcp_client()
    print("TCP client ended...")
