from src.utils.db import getDb

def getMenus():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM menu
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addMenus(menu):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `menu`(`name`, `price`, `category`)
			VALUES (%s, %s, %s)
			;
		"""
	values = [menu["name"], menu["price"], menu["category"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Menu already registered"
	db.commit()

	return "success"

def getMenuCategories():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT menucategories.category, count(*) AS numMenus FROM menucategories
			LEFT JOIN menu on menucategories.category = menu.category
			GROUP BY menucategories.category
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addMenuCategories(menucategories):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `menucategories`(`category`)
			VALUES (%s)
			;
		"""
	values = [menucategories["category"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Menu Category already registered"
	db.commit()

	return "success"

def getTables():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT tables.tableNo, tables.numberofSeats, transactions.status FROM tables
			LEFT JOIN transactions ON tables.tableNo = transactions.tableNo 
			AND status != 'Cancelled' and status != 'Finished'
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	for table in res:
		if table["status"] == None:
			table["availability"] = "Available"
		else:
			table["availability"] = "Not Available"
	#print(res)

	return res