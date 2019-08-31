# @ author: k.s.

import socket as sock
import threading

#server_adr = ("192.168.0.23", 12345)
server_adr = ("127.0.0.1", 1234)
sock = sock.socket(sock.AF_INET, sock.TCP_NODELAY)
sock.connect(server_adr)


def sender():
	msg = input()
	client = sock.getsockname()
	client = "(" + str(client[0]) + ", " + str(client[1]) + "): "
	sock.send(bytearray(client + msg, "UTF-8"))


def receiver():
	msg_recv = str(sock.recv(512), "UTF-8")
	print(msg_recv)


if __name__ == "__main__":
	while True:
		send = threading.Thread(target=sender, args=())
		threading.Thread(target=receiver, args=(), daemon=True).start()
		send.start()
		send.join()




