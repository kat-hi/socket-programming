'''
@ autor: k.s.

'''

import socket as sock
import threading
import databaseConnection
import yaml

config = yaml.load(open("config.yaml"))

sock = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
currentConnection = ''
acceptedConnections = []
socketbacklog = 2


class Connection:
	def __init__(self, socket):
		self.socket = socket
		self.receive()

	def sender(self, msg):
		for connection in acceptedConnections:
			if connection != self.socket:
				try:
					connection.send(bytes(msg, "UTF-8"))
				except IndexError as iE:
					print("index Error", iE.__cause__)
		self.receive()

	def receive(self):
		while True:
			msg_recv = str(self.socket.recv(512), "UTF-8")
			if msg_recv != '':
				print(msg_recv)
				self.sender(msg_recv)


def start_server():
	sock.bind(("192.168.0.23", config.port))
	#sock.bind(("127.0.0.1", 1234))
	sock.listen(socketbacklog)


def update_accepted_connections(connection):
	if len(acceptedConnections) == 0:
		acceptedConnections.append(connection)
	else:
		connection_exists = False
		for socket in acceptedConnections:
			if socket == connection:
				connection_exists = True
				print("socket==connection")
		if not connection_exists:
			acceptedConnections.append(connection)
			print("connection added")


if __name__ == "__main__":
	database = databaseConnection.Database()
	start_server()
	while len(acceptedConnections) < socketbacklog:
		con, adr = sock.accept()
		update_accepted_connections(con)
		databaseConnection.insert_client_connection(sock.getsockname())
		threading.Thread(target=Connection, args=(con,)).start()
