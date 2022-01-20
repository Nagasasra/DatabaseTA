from flask import session
from src.utils.db import getDb
import bcrypt

def register(userData):
	if userData["password"] != userData["password2"]:
		return "Password don't match"

	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = "SELECT * FROM staffs WHERE email = %s;"
	values = [userData["email"]]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)

	if not res:
		return "Email not found"

	staffId = res["staffId"]
	pw_encrypted = bcrypt.hashpw(userData["password"].encode(), bcrypt.gensalt())

	query = "INSERT INTO user (username, password, staffId) VALUES (%s, %s, %s);"
	values = [userData["username"], pw_encrypted, staffId]

	try:
		affected_rows = cursor.execute(query, tuple(values))
	except Exception as e:
		return "User already registered"
	db.commit()

	return "success"

def login(userData):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = "SELECT * FROM user WHERE username = %s;"
	values = [userData["username"]]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)

	if not res:
		return "username not found"

	if not bcrypt.checkpw(userData["password"].encode(), res["password"].encode()):
		return "wrong password"

	session['username'] = res["username"]
	session['staffId'] = res["staffId"]
	session['picture'] = res["picture"]
	return "success"

def getUser(username):
	db = getDb()
	cursor = db.cursor(dictionary=True)
	query = "SELECT * FROM user JOIN staffs on staffs.id = user.staffId WHERE username = %s;"
	values = [username]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)
	return res

def editUser(user):
	db = getDb()
	cursor = db.cursor(dictionary=True)
	query = """
			UPDATE `staffs`
			SET `firstName`= %s, `lastName`= %s, `email`= %s,
				`age`= %s, `position`= %s
			WHERE id = %s
			;
		"""
	values = [user["firstName"], user["lastName"], user["email"], user["age"], user["position"], user["id"]]
	cursor.execute(query, tuple(values))

	db.commit()

	return "success"

def editPicture(username, picturename):
	db = getDb()
	cursor = db.cursor(dictionary=True)
	query = """
			UPDATE `user`
			SET `picture`= %s
			WHERE username = %s
			;
		"""
	values = [picturename, username]
	cursor.execute(query, tuple(values))

	db.commit()
	session["picture"] = picturename

	return "success"