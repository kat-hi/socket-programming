import yaml
import mysql.connector
from mysql.connector import Error
from time import gmtime, strftime



def update_latest_connection_time(client):
	cursor = Database.connect.cursor()
	current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	cursor.execute("UPDATE Connections SET LastConnection = " + current_time + "WHERE ConnectionID =" + client + ";")


def check_client_exist(client):
	pass

def insert_client_connection(client):
	cursor = Database.connect.cursor()
	clientconnection = client
	clientconnection = "(" + str(clientconnection[0]) + ", " + str(clientconnection[1]) + ")"
	cursor.execute("INSERT INTO ConnectionID VALUES (?,?,?)", (clientconnection, 'unkown', 'unknown'))

class Database:
	config = yaml.load(open("config.yaml"))
	while True:
		try:
			connect = mysql.connector.connect(
				host=config.get("host"),
				database=config.get("dbname"),
				user=config.get("user"),
				password=config.get("password")
			)
			break
		except Error as e:
			print("! Connection refused: ", e.__cause__)




