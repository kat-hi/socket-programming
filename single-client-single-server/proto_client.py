import socket
import threading

server_adr = ("192.168.0.23", 1234)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_adr)

print("$ terminate the session with 'end' ")


def __ending__():
	client_socket.close()
	print("Client exit.")
	exit(0)


def sender():
	while True:
		msg_send = input()
		if msg_send == "end":
			__ending__()
		elif msg_send != "":
			client_socket.send(bytes(msg_send, "UTF-8"))


def receiver():
	while True:
		msg_recv = str(client_socket.recv(1024), "UTF-8")
		print("server: " + msg_recv)


recv_thread = threading.Thread(target=receiver, args="")
send_thread = threading.Thread(target=sender, args="")

send_thread.start()
recv_thread.start()
recv_thread.join()
send_thread.join()
