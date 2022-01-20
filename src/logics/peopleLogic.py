from src.utils.db import getDb

def getStaffs():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM staffs LEFT JOIN user
			on staffs.id = user.staffId;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addStaffs(staff):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `staffs`(`firstName`, `lastName`, `email`, `position`, `gender`, `age`)
			VALUES (%s, %s, %s, %s, %s, %s)
			;
		"""
	values = [staff["firstName"], staff["lastName"], staff["email"], staff["position"], staff["gender"], staff["age"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Staff already registered"
	db.commit()

	return "success"