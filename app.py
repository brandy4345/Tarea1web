from flask import Flask, request, make_response,render_template, redirect, url_for, jsonify,abort
from flask_cors import cross_origin
from utils.validations import validate_forms_pedido, validate_forms_producto
from utils import validations
from database import db
from werkzeug.utils import secure_filename
import hashlib
import os
import filetype
from PIL import Image

app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'

app.secret_key = "s3cr3t_k3y" # ah?

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1000 * 1000 # 32 MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File exceeds the maximum file size allowed', 413


#----- Routes -----
@app.route("/")
def index(): 
    return render_template("ferialibre/index.html")

@app.route("/agregar-pedido")
def agregarPedido():
    return render_template("ferialibre/agregar-pedido.html")

@app.route("/agregar-producto")
def agregarProducto():
    return render_template("ferialibre/agregar-producto.html")

@app.route("/region-comunas", methods = ['GET'])
@cross_origin(origin="localhost", supports_credentials=True)
def ajaxRegionComunas():
    regiones = db.get_regiones()
    comunas = db.get_comunas()
    data = {}
    for id, nombre in regiones:
        data[id] = {
            "nombre" : nombre,
            "comunas" : []
        }
    for id_comuna, nombre, id_region in comunas:
        data[id_region]["comunas"].append({
            "id": id_comuna,
            "nombre": nombre
        })
    return jsonify(data)


@app.route("/informacion-pedido")
def informacionPedido():
    return render_template("ferialibre/informacion-pedido.html")


@app.route("/informacion-productos")
def informacionProducto():
    return render_template("ferialibre/informacion-producto.html")

@app.route("/ver-pedidos")
def verPedidos():
    return render_template("ferialibre/ver-pedidos.html")

@app.route("/get-pedidos/<int:numero>", methods = ['GET'])
@cross_origin(origin="localhost", supports_credentials=True)
def getPedidos(numero):
    if numero < 0:
        numero = 0
    pedidos = db.get_pedidos(numero)
    return jsonify(pedidos)

@app.route("/ver-productos")
def verProductos():
    return render_template("ferialibre/ver-productos.html")
@app.route("/get-productos/<int:numero>", methods = ['GET'])
@cross_origin(origin="localhost", supports_credentials=True)
def getProductos(numero):
    if numero < 0:
        numero = 0
    productos = db.get_productos(numero)
    data = []
    for i in range(len(productos)):
        temp =[]
        for j in range(4):
            temp.append(productos[i][j])
        filename = productos[i][5]
        name, extension = os.path.splitext(filename)
        name += "_120x120"
        temp.append(productos[i][4]+"/"+name+extension)
        data.append(temp)
    return jsonify(data)

@app.route("/post-producto", methods = ["POST"])
def postProducto():
    
    tipo_fruta_o_verdura = request.form.get("Tipo-fruta-o-verdura")
    productos_fruta = request.form.getlist("fruta")
    productos_verdura = request.form.getlist("verdura")
    descripcion = request.form.get("descripcion-producto")
    foto = request.files.get("foto")
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    telefono = request.form.get("telefono")

    if validate_forms_producto(tipo_fruta_o_verdura,
                      productos_fruta,
                      productos_verdura,
                      descripcion,
                      foto,
                      region,
                      comuna,
                      nombre,
                      email,
                      telefono):

      #save the product
        
        if (int(tipo_fruta_o_verdura)==0):
            db.create_producto("fruta",descripcion, comuna, nombre, email, telefono)
            ultimo_id = db.get_last_id_from_producto ()
            db.create_producto_verdura_fruta(ultimo_id[0],productos_fruta)
        else:
            db.create_producto("verdura",descripcion, comuna, nombre, email, telefono)
            ultimo_id = db.get_last_id_from_producto ()
            db.create_producto_verdura_fruta(ultimo_id[0],productos_verdura)
        
        nombre_carpeta = f"producto{ultimo_id[0]}"
        ruta_carpeta = os.path.join(app.config["UPLOAD_FOLDER"], nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

        _filename = hashlib.sha256(
            secure_filename(foto.filename) # nombre del archivo
            .encode("utf-8") # encodear a bytes
            ).hexdigest()
        _extension = filetype.guess(foto).extension
        img_filename = f"{_filename}.{_extension}"


        foto.save(os.path.join(ruta_carpeta,img_filename))

        sizes = [(120, 120), (640, 480),(1280,1024)]


        for size in sizes:
            with Image.open(foto) as img:
                foto_copia = img.resize (size)
                nombre_foto = f"{_filename}_{size[0]}x{size[1]}.{_extension}"
                foto_copia.save(os.path.join(ruta_carpeta,nombre_foto))
        db.create_foto(ruta_carpeta, img_filename, ultimo_id)

    else:
        #print(validations.validate_tipo(tipo_fruta_o_verdura))
        #print(validations.validate_producto(productos_fruta,productos_verdura,tipo_fruta_o_verdura))
        #print(validations.validate_description(descripcion))

        #print(validations.validate_img(foto))
        #print(validations.validate_region_comuna(region,comuna))

        #print(validations.validate_nombre(nombre))
        #print(validations.validate_email(email))

        #print(validations.validate_telefono(telefono))
        
        print(validations.validate_region(region))
        print(validations.validate_comuna(region,comuna))
        
        

    return index()

@app.route("/stats", methods=["GET"])
def stats():
    return render_template("ferialibre/stats.html")

@app.route("/get-product-data", methods = ['GET'])
@cross_origin(origin="localhost", supports_credentials=True)
def getProductData():
    productData= db.get_product_data()
    return jsonify(productData)

@app.route("/get-pedido-data", methods = ['GET'])
@cross_origin(origin="localhost", supports_credentials=True)
def getPedidoData():
    pedidoData= db.get_pedido_data()
    return jsonify(pedidoData)

@app.route("/post-pedido", methods = ["POST"])
def postPedido():
        
    tipo_fruta_o_verdura = request.form.get("Tipo-fruta-o-verdura")
    pedidos_fruta = request.form.getlist("fruta")
    pedidos_verdura = request.form.getlist("verdura")
    descripcion = request.form.get("descripcion-producto")
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    telefono = request.form.get("telefono")

    if validate_forms_pedido(tipo_fruta_o_verdura,
                      pedidos_fruta,
                      pedidos_verdura,
                      descripcion,
                      region,
                      comuna,
                      nombre,
                      email,
                      telefono):

      #save the product
        
        if (int(tipo_fruta_o_verdura)==0):
            db.create_pedido("fruta",descripcion, comuna, nombre, email, telefono)
            ultimo_id = db.get_last_id_from_pedido ()
            db.create_pedido_verdura_fruta(ultimo_id[0],pedidos_fruta)
        else:
            db.create_pedido("verdura",descripcion, comuna, nombre, email, telefono)
            ultimo_id = db.get_last_id_from_pedido ()
            db.create_pedido_verdura_fruta(ultimo_id[0],pedidos_verdura)

    else:
        #print(validations.validate_tipo(tipo_fruta_o_verdura))
        #print(validations.validate_producto(productos_fruta,productos_verdura,tipo_fruta_o_verdura))
        #print(validations.validate_description(descripcion))


        #print(validations.validate_region_comuna(region,comuna))

        #print(validations.validate_nombre(nombre))
        #print(validations.validate_email(email))

        #print(validations.validate_telefono(telefono))
        
        print(validations.validate_region(region))
        print(validations.validate_comuna(region,comuna))
        
        

    return index()