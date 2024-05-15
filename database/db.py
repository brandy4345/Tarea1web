import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

def get_region_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select nombre from region where id=%s;", (id,))
	region = cursor.fetchone()
	return region

def get_regionid_by_comunaid(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select region_id from comuna where id=%s;", (id,))
	regionId = cursor.fetchone()
	return regionId
