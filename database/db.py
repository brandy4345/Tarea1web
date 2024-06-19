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

def create_producto(tipo, descripcion, comuna_id,nombre_productor,email_productor,celular_productor):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO producto (tipo, \
									  descripcion, \
									  comuna_id, \
									  nombre_productor, \
									  email_productor, \
									  celular_productor) VALUES (%s,%s,%s,%s,%s,%s);" 
	, (tipo, descripcion, comuna_id,nombre_productor,email_productor,celular_productor))
	conn.commit()
def create_pedido(tipo, descripcion, comuna_id,nombre_comprador,email_comprador,celular_comprador):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO pedido (tipo, \
									  descripcion, \
									  comuna_id, \
									  nombre_comprador, \
									  email_comprador, \
									  celular_comprador) VALUES (%s,%s,%s,%s,%s,%s);" 
	, (tipo, descripcion, comuna_id,nombre_comprador,email_comprador,celular_comprador))
	conn.commit()

def get_last_id_from_producto (): 
	conn = get_conn()
	cursor = conn.cursor()
	#No me funciono select LAST_INSERT_ID() 
	cursor.execute("SELECT MAX(id) from producto")
	id = cursor.fetchone()
	return id
def get_last_id_from_pedido (): 
	conn = get_conn()
	cursor = conn.cursor()
	#No me funciono select LAST_INSERT_ID() 
	cursor.execute("SELECT MAX(id) from pedido")
	id = cursor.fetchone()
	return id

def create_producto_verdura_fruta(id, productoLista):
	conn = get_conn()
	cursor = conn.cursor()
	for producto in productoLista:
		cursor.execute("insert into producto_verdura_fruta (producto_id, tipo_verdura_fruta_id) VALUES (%s,%s);",
				 (id,int(producto)))
	conn.commit()
def create_pedido_verdura_fruta(id, pedidoLista):
	conn = get_conn()
	cursor = conn.cursor()
	for pedido in pedidoLista:
		cursor.execute("insert into pedido_verdura_fruta (tipo_verdura_fruta_id,pedido_id) VALUES (%s,%s);",
				 (int(pedido),id))
	conn.commit()

def create_foto(ruta_archivo,nombre_archivo, producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, producto_id) VALUES (%s,%s,%s);",
				(ruta_archivo, nombre_archivo, producto_id))
	conn.commit()

def get_regionId_by_nombre(region):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("Select id from region where nombre=%s;",(region,))
	id = cursor.fetchone()
	return id

def get_comunaId_by_nombre(comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("Select id from comuna where nombre=%s;",(comuna,))
	id = cursor.fetchone()
	return id

def get_regiones():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select * from region;")
	regiones = cursor.fetchall()
	return regiones

def get_comunas():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select * from comuna;")
	comunas = cursor.fetchall()
	return comunas

def get_comunas_by_regionId(region_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select nombre from comuna where region_id = %s;",(region_id,))
	regiones = cursor.fetchall()
	return regiones

def get_pedidos(page_size):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select id,tipo,comuna_id from producto limit %s;",(page_size,))
	pedidos = cursor.fetchall()
	return pedidos

def get_comuna_by_comunaId(comunaId):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select nombre from comuna where id=%s;",(comunaId,))
	comuna  = cursor.fetchone()
	return comuna

def get_region_by_comunaId(comunaId):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select region_id from comuna where id=%s;",(comunaId,))
	comuna  = cursor.fetchone()
	cursor.execute("select nombre from region where id=%s",(comuna[0],))
	region = cursor.fetchone
	return region

def get_foto_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select ruta_archivo,nombre_archivo from foto where producto_id=%s;",(id,))
	foto = cursor.fetchone()
	return foto

def get_productos_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("select tipo_verdura_fruta_id from producto_fruta_verdura where id=%s;",(id,))
	productos = cursor.fetchall()
	lista =  []
	for producto in productos:
		cursor.execute("select nombre from tipo_verdura_fruta where id=%s;",(producto[0],))
		temp = cursor.fetchone()
		lista.append(temp[0])
	return lista

def get_product_data():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute("Select t2.nombre,COUNT(*) as cant \
					from producto_verdura_fruta t1 \
					INNER JOIN tipo_verdura_fruta t2 ON t1.tipo_verdura_fruta_id=t2.id\
					group by tipo_verdura_fruta_id ; ")
	data = cursor.fetchall()
	return data

def get_pedido_data():
	conn = get_conn()
	cursor = conn.cursor()	
	cursor.execute("SELECT t2.nombre, COUNT(*) \
					FROM pedido t1 \
					INNER JOIN comuna t2 ON t1.comuna_id = t2.id \
					GROUP BY t2.nombre;")
	data = cursor.fetchall()
	return data