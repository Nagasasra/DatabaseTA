from src.utils.db import getDb

def getTransactions():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT transactions.*, firstName, lastName FROM transactions
			JOIN staffs ON transactions.staffId = staffs.id
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def getTransaction(id_trx):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM transactions
			WHERE id = %s
			;
		"""
	values = [id_trx]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	#print(res)

	return res

def addTransactions(transaction):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	status = "Waiting for Order"
	query = """ 
			INSERT INTO `transactions`(`date`, `arrival_time`, `staffId`, `tableNo`, `status`)
			VALUES (%s, %s, %s, %s, %s)
			;
		"""
	values = [transaction["date"], transaction["arrival_time"], transaction["staffId"], transaction["tableNo"], status]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Transaction already registered"
	db.commit()

	return "success"

def editTransactions(transaction):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			UPDATE `transactions` SET exit_time = %s, status = %s
			WHERE id = %s
			;
		"""
	values = [transaction["exit_time"], transaction["status"], transaction["id"]]
	
	cursor.execute(query, tuple(values))
	db.commit()

	return "success"

def updatePrices(id_trx):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	menus = getTransactionMenu(id_trx)
	totalPrice = 0
	for menu in menus:
		totalPrice += menu["subtotal"]

	query = """ 
			UPDATE `transactions` SET totalPrice = %s
			WHERE id = %s
			;
		"""
	values = [totalPrice, id_trx]
	
	cursor.execute(query, tuple(values))
	db.commit()

	return "success"

def getTransactionMenu(id_trx):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM transactionmenus
			JOIN menu on transactionmenus.menuId = menu.id
			WHERE transactionId = %s
			;
		"""
	values = [id_trx]
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addTransactionMenu(menu):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	menu = dict(menu)
	menu["price"] = menu["menuId"].split(",")[1]
	menu["menuId"] = menu["menuId"].split(",")[0]
	subtotal = int(menu["qty"]) * int(menu["price"])
	print(menu["qty"], menu["price"], subtotal)
	query = """ 
			INSERT INTO `transactionmenus`(`transactionId`, `menuId`, `qty`, `price`, `subtotal`)
			VALUES (%s, %s, %s, %s, %s)
			;
		"""
	values = [menu["transactionId"], menu["menuId"], menu["qty"], menu["price"], subtotal]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Transaction Menu already registered"
	db.commit()

	return "success"

def deleteTransactionMenu(id_trx, menuId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			DELETE FROM transactionmenus
			WHERE transactionId = %s and menuId = %s
			;
		"""
	values = [id_trx, menuId]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Transaction Menu doesn't exist"
	db.commit()

	return "success"