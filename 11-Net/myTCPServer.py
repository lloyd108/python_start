import socket


def tcp_server():
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 6677)
    skt.bind(addr)

    skt.listen()

    while True:
        skt_c, addr_c = skt.accept()
        msg = skt_c.recv(500)

        msg = msg.decode("utf-8")

        rst = "Recieved message \"{0}\" from {1}".format(msg, addr_c)
        print(rst)

        skt_c.send(rst.encode())

        skt_c.close()


if __name__ == "__main__":
    print("TCP server started...")
    tcp_server()
    print("TCP server ended...")
