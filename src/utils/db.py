from mysql.connector import connect
import mysql.connector
import os

__db = connect(
	host=os.getenv("SQLHOST"),
	user=os.getenv("SQLUSER"),
	password=os.getenv("SQLPASS"),
	database=os.getenv("SQLDATABASE"),
	port=os.getenv("SQLPORT")
)

def getDb():
	if not __db.is_connected():
		__db.reconnect()
	return __db

def getError():
	return mysql.connector.Error