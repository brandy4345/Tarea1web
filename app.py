from flask import Flask, request, render_template, redirect, url_for
from utils.validations import validate_forms
from utils import validations
from database import db

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


@app.route("/informacion-pedido")
def informacionPedido():
    return render_template("ferialibre/informacion-pedido.html")


@app.route("/informacion-productos")
def informacionProducto():
    return render_template("ferialibre/informacion-producto.html")

@app.route("/ver-pedidos")
def verPedidos():
    return render_template("ferialibre/ver-pedidos.html")

@app.route("/ver-productos")
def verProductos():
    return render_template("ferialibre/ver-productos.html")


@app.route("/post-producto", methods = ["POST"])
def postProducto():
    
    tipo_fruta_o_verdura = request.form.get("Tipo-fruta-o-verdura")
    productos_fruta = request.form.getlist("fruta")
    productos_verdura = request.form.getlist("verdura")
    descripcion = request.form.get("descripcion-producto")
    foto = request.form.get("foto")
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    telefono = request.form.get("telefono")

    if validate_forms(tipo_fruta_o_verdura,
                      productos_fruta,
                      productos_verdura,
                      descripcion,
                      foto,
                      region,
                      comuna,
                      nombre,
                      email,
                      telefono):
        print("esta correctito")
    else:
        print(validations.validate_tipo(tipo_fruta_o_verdura))
        print(validations.validate_producto(productos_fruta,productos_verdura,tipo_fruta_o_verdura))
        print(validations.validate_description(descripcion))
        print(validations.validate_img(foto))
        print(validations.validate_region_comuna(region,comuna))

    return "hola"
