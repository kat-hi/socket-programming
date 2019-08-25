# @ author: k.s.

import socket as sock
import threading


server_adr = ("127.0.0.1", 12345)
sock = sock.socket(sock.AF_INET, sock.TCP_NODELAY)
sock.connect(server_adr)


def sender():
	msg = input()
	sock.send(bytearray("client: " + msg, "UTF-8"))


def receiver():
	msg_recv = str(sock.recv(2048), "UTF-8")
	print(msg_recv)


if __name__ == "__main__":
	while True:
		send=threading.Thread(target=sender, args=())
		recv=threading.Thread(target=receiver, args=())
		send.start()
		recv.start()
		recv.join()





