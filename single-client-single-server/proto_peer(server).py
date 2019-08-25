'''
SOCKET PRECONDITIONs
[1] since we predefined DHCP-Server-Configs on the raspberry pi's (with assigning IP-addresses to
specific MAC-addresses),  we'll use a static IP for passing a host into bind()
[2] furthermore we'll use IPv4, so bind() expects 2-tuple: (host,port)
'''

import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.23", 1234))
server_socket.listen(4)
(con, adr) = server_socket.accept()

print("terminate the session with 'end' ")


def __ending__():
	server_socket.close()
	print("Server exit.")


def receiver():
	while True:
		msg_recv = str(con.recv(1024), "UTF-8")
		if msg_recv == "end":
			__ending__()
		elif msg_recv != "":
			print("client: " + msg_recv)


def sender():
	while True:
		msg_send = input()
		if msg_send == "end":
			__ending__()
		elif msg_send != "":
			con.send(bytes(msg_send, "UTF-8"))


sender_thread = threading.Thread(target=sender, args="")
recv_thread = threading.Thread(target=receiver, args="")

sender_thread.start()
recv_thread.start()
recv_thread.join()
sender_thread.join()
