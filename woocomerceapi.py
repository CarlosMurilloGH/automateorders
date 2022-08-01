from woocommerce import API
import json
import os

from dotenv import load_dotenv

load_dotenv()

wcapi = API(
    url=os.getenv("URL"), # Your store URL
    consumer_key=os.getenv("CONSUMER_KEY"), # Your consumer key
    consumer_secret=os.getenv("CONSUMER_SECRET"), # Your consumer secret
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)

# Get processed orders
# print(wcapi.get("orders", params={"status": "processing"}).json())

#Getting the order from its ID
order=wcapi.get("orders/3254").json()


#Sacar todos los productos con su informacion del pedido
orderList=order["line_items"]

#Obtener solo los nombres de los productos
product_names=[]

for names in order["line_items"] :
    product_names.append(names["name"])
# print(product_names)


#Obtener el ID de los productos
# for id in order["line_items"] :
#     productId = id["product_id"]

#Obtener datos para olva
billing=order["billing"]

Nombres=billing["first_name"]

Apellidos=billing["last_name"]

Departamento=billing["state"]

Ciudad=billing["city"]

Direccion=billing["address_1"]

Celular=billing["phone"]

Dni=billing["billing_dni"]

# print(Nombres,Apellidos,Departamento,Ciudad,Direccion ,Celular,Dni)


#Buscar stickers

folder = "D:\\stickers\\final"
productList_extenstion = [i + '.png' for i in product_names]
# print(productList_extenstion)

# fileToSearch = productList_extenstion[2]
fileToSearch = ["abra.png","119,png"]

for relPath,dirs,files in os.walk(folder):
    if([i in fileToSearch] in files):
        fullPath = os.path.join(folder, relPath, fileToSearch)
        print(fullPath)

