import socket
import threading
import sys

server_adr = ("127.0.0.1", 12345)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_adr)

print("$ terminate the session with 'end' ")
EOL = '\r\n'

def __ending__():
	client_socket.close()
	print("Client exit.")
	sys.exit(0)

def sender():
	msg_send = ''
	while EOL not in msg_send:
		msg_send = input()
		if msg_send == "end":
			__ending__()
		elif msg_send != "":
			client_socket.send(bytes(msg_send, "UTF-8"))


def receiver():
	while True:
		msg_recv = str(client_socket.recv(8), "UTF-8")
		print("server: " + msg_recv)


recv_thread = threading.Thread(target=receiver, args="")
send_thread = threading.Thread(target=sender, args="")

send_thread.start()
recv_thread.start()
recv_thread.join()
send_thread.join()
