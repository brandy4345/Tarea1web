import filetype
from database import db
import re 

def validate_tipo(tipo_fruta_o_verdura):
    try:
        num = int(tipo_fruta_o_verdura)
        if (num == 0 or num == 1):
            return True
    except Exception:
        return False

def validar_producto_id(productos, inicio, fin):
    for producto in productos: 
        try:
            num = int(producto)
            if (not(num>=inicio and num<=fin)):
                return False
        except Exception:
            return False
    return True


def validar_lista (productos):
    return type(productos)== list and len(productos)>=1 and len(productos)<=5 


def validate_producto(producto_fruta,producto_verdura,tipo_fruta_o_verdura):
    if (validate_tipo(tipo_fruta_o_verdura)):
        num = int(tipo_fruta_o_verdura)
        if (num == 0):
            return validar_lista(producto_fruta) and  validar_producto_id(producto_fruta,1,37)
        elif(num == 1):
            return validar_lista(producto_verdura) and validar_producto_id(producto_verdura,38,62)
    else:
        return False

def validate_description(descripcion):
    return type(descripcion)==str and len(descripcion)<=300 

def validate_img(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if img is None:
        
        return False

    # check if the browser submitted an empty file
    if img.filename == "":
        
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
       
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        
        return False
    return True

def validate_region(region):
    try:
        num = int(region)
        return num>=1 and num<=16
    except Exception:
        return False

def validate_comuna(region, comuna):
    try:
        num = int(comuna)
        regionId_db = db.get_regionid_by_comunaid(num)
        regionId = int(region)

        return regionId_db[0] == regionId
    except Exception:
        return False

def validate_region_comuna(region,comuna):
    if(validate_region(region)):
        return validate_comuna(region, comuna)
    else:
        return False

def validate_nombre(nombre):
    return type(nombre) == str and len(nombre)>=3 and len(nombre)<=80

def validate_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if (re.match(regex,email)):
        return len(email) <=30
    else:
        return False

def validate_telefono(telefono):
    regex = r'(\+?56)?\s?0?9\s?[98765432]\d{7}'
    if (re.match(regex,telefono)):
        return True
    else:
        return False

def validate_forms_producto(tipo_fruta_o_verdura,
                      productos_fruta,
                      productos_verdura,
                      descripcion,
                      foto,
                      region,
                      comuna,
                      nombre,
                      email,
                      telefono):
    return validate_tipo(tipo_fruta_o_verdura) and validate_producto(productos_fruta,productos_verdura, tipo_fruta_o_verdura) and \
        validate_description(descripcion) and validate_img(foto) and validate_region_comuna(region,comuna) \
        and validate_nombre(nombre) and validate_email(email) and validate_telefono(telefono)

def validate_forms_pedido(tipo_fruta_o_verdura,
                      productos_fruta,
                      productos_verdura,
                      descripcion,
                      region,
                      comuna,
                      nombre,
                      email,
                      telefono):
    return validate_tipo(tipo_fruta_o_verdura) and validate_producto(productos_fruta,productos_verdura, tipo_fruta_o_verdura) and \
        validate_description(descripcion) and validate_region_comuna(region,comuna) \
        and validate_nombre(nombre) and validate_email(email) and validate_telefono(telefono)