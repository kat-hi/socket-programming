# import yaml
import config
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
	clientconnection = str(clientconnection[0]) + ", " + str(clientconnection[1])
	sqlquery = 'INSERT INTO Connections ( `ip`, `latestConnection`) VALUES (%s, %s)'
	cursor.execute(sqlquery, (clientconnection, "unknown"))
	Database.connect.commit()
	print("database updated")
	cursor.close()


class Database:
	while True:
		try:
			'''connect = mysql.connector.connect(
				host=config.get("host"),
				database=config.get("dbname"),
				user=config.get("user"),
				password=config.get("password")
			)'''
			connect = mysql.connector.connect(
				host=config.host,
				database=config.dbname,
				user=config.user,
				password=config.password
			)
			break
		except Error as e:
			print("! Connection refused: ", e.__cause__)




