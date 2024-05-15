from flask import Flask, request, render_template, redirect, url_for


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
    #aca irian las opciones elegidas
    descripcion = request.form.get("descripcion-producto")
    foto = request.form.get("foto")