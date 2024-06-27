# import pandas as pd
# import requests
# import json
# import uuid
# import os
#
# # Obtener la ruta del archivo y del script
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, 'Prueba técnica - Backend Data .xlsx')
#
# # Leer las diferentes hojas del archivo
# sheets = pd.read_excel(file_path, sheet_name=None)
#
# # Definir las URLs para cada endpoint
# urls = {
#     "Transacciones": "http://127.0.0.1:8000/api/transactions/",
#     "Categorías": "http://127.0.0.1:8000/api/categories/",
#     "Comercios": "http://127.0.0.1:8000/api/merchants/",
#     "Keywords": "http://127.0.0.1:8000/api/keywords/"
# }
#
#
# # Función para limpiar datos
# def clean_data(data):
#     # Convertir NaN a None
#     data = data.where(pd.notnull(data), None)
#     return data
#
#
# # Lista de campos requeridos para cada tipo de datos
# required_fields = {
#     "Transacciones": ["id", "description", "amount", "date"],
#     "Categorías": ["id", "name", "type"],
#     "Comercios": ["id", "merchant_name", "merchant_logo", "category"],
#     "Keywords": ["id", "keyword", "merchant"]
# }
#
#
# # Función para verificar campos requeridos
# def validate_fields(data, required_fields):
#     for field in required_fields:
#         if field not in data or data[field] is None:
#             return False
#     return True
#
#
# # Función para convertir filas de DataFrame en JSON y enviar POST def post_data(df, url, required_fields): for _,
# row in df.iterrows(): # Convertir la fila a un diccionario y luego a JSON data = row.to_dict() # Limpiar los datos
# data = clean_data(pd.Series(data)).to_dict() # Generar UUIDs si es necesario if "id" in data and pd.isna(data[
# "id"]): data["id"] = str(uuid.uuid4()) # Convertir las fechas a cadenas if "date" in data and data["date"] is not
# None: data["date"] = data["date"].strftime('%Y-%m-%d') if isinstance(data["date"], pd.Timestamp) else data["date"]
# Validar campos requeridos if not validate_fields(data, required_fields): print(f'Skipping row due to missing
# required fields: {data}') continue response = requests.post(url, data=json.dumps(data), headers={'Content-Type':
# 'application/json'}) try: response_json = response.json() except requests.exceptions.JSONDecodeError: response_json
# = None print(f'Response from {url}:', response.status_code, response_json)
#
#
# # Enviar los datos de cada hoja a la URL correspondiente
# for sheet_name, url in urls.items():
#     df = sheets[sheet_name]
#     post_data(df, url, required_fields[sheet_name])


# import pandas as pd
# import requests
# import json
# import uuid
# import os
#
# # Obtener la ruta del archivo y del script
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, 'Prueba técnica - Backend Data .xlsx')
#
# # Leer las diferentes hojas del archivo
# sheets = pd.read_excel(file_path, sheet_name=None)
#
# # Definir las URLs para cada endpoint
# urls = {
#     "Transacciones": "http://127.0.0.1:8000/api/transacciones/",
#     "Categorías": "http://127.0.0.1:8000/api/categorias/",
#     "Comercios": "http://127.0.0.1:8000/api/comercios/",
#     "Keywords": "http://127.0.0.1:8000/api/keywords/"
# }
#
#
# # Función para limpiar datos
# def clean_data(data):
#     # Convertir NaN a None
#     data = data.where(pd.notnull(data), None)
#     return data
#
#
# # Lista de campos requeridos para cada tipo de datos
# required_fields = {
#     "Transacciones": ["id", "description", "amount", "date"],
#     "Categorías": ["id", "name", "type"],
#     "Comercios": ["id", "merchant_name", "merchant_logo", "category"],
#     "Keywords": ["id", "keyword", "merchant"]
# }
#
#
# # Función para verificar campos requeridos
# def validate_fields(data, required_fields):
#     for field in required_fields:
#         if field not in data or data[field] is None:
#             return False
#     return True
#
#
# # Función para convertir filas de DataFrame en JSON y enviar POST
# def post_data(df, url, required_fields):
#     for _, row in df.iterrows():
#         # Convertir la fila a un diccionario y luego a JSON
#         data = row.to_dict()
#         # Limpiar los datos
#         data = clean_data(pd.Series(data)).to_dict()
#         # Generar UUIDs si es necesario
#         if "id" in data and pd.isna(data["id"]):
#             data["id"] = str(uuid.uuid4())
#         # Convertir las fechas a cadenas
#         if "date" in data and data["date"] is not None:
#             data["date"] = data["date"].strftime('%Y-%m-%d') if isinstance(data["date"], pd.Timestamp) else data["date"]
#         # Validar campos requeridos
#         if not validate_fields(data, required_fields):
#             print(f'Skipping row due to missing required fields: {data}')
#             continue
#         response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
#         try:
#             response_json = response.json()
#         except requests.exceptions.JSONDecodeError:
#             response_json = None
#         print(f'Response from {url}:', response.status_code, response_json)
#
#
# # Enviar los datos de cada hoja a la URL correspondiente
# for sheet_name, url in urls.items():
#     df = sheets[sheet_name]
#     post_data(df, url, required_fields[sheet_name])


import pandas as pd
import requests
import json
import uuid
import os

# Obtener la ruta del archivo y del script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'Prueba técnica - Backend Data .xlsx')

# Leer las diferentes hojas del archivo
sheets = pd.read_excel(file_path, sheet_name=None)

# Definir las URLs para cada endpoint
urls = {
    "Transacciones": "http://127.0.0.1:8000/api/transacciones/",
    "Categorías": "http://127.0.0.1:8000/api/categorias/",
    "Comercios": "http://127.0.0.1:8000/api/comercios/",
    "Keywords": "http://127.0.0.1:8000/api/keywords/"
}

# Obtener el token de autenticación
login_url = "http://127.0.0.1:8000/api/token/"
login_data = {
    "username": "mario",
    "password": "1234",
    # "username": "Ch1le",
    # "password": "20245sout",
}


# Función para obtener el token de autenticación
def get_auth_token(login_url, login_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(login_url, data=json.dumps(login_data), headers=headers)
    response.raise_for_status()
    try:
        response_json = response.json()
        if 'access' in response_json:
            return response_json['access']
        elif 'token' in response_json:
            return response_json['token']
        else:
            raise KeyError("Neither 'access' nor 'token' found in response JSON.")
    except (ValueError, KeyError) as e:
        print(f"Failed to get token: {e}. Response JSON was {response.text}")
        exit(1)

# Obtener el token de autenticación
token = get_auth_token(login_url, login_data)
print("Authentication Token:", token)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

# Función para limpiar datos
def clean_data(data):
    # Convertir NaN a None
    data = data.where(pd.notnull(data), None)
    return data

# Lista de campos requeridos para cada tipo de datos
required_fields = {
    "Transacciones": ["id", "description", "amount", "date"],
    "Categorías": ["id", "name", "type"],
    "Comercios": ["id", "merchant_name", "merchant_logo", "category"],
    "Keywords": ["id", "keyword", "merchant"]
}

# Función para verificar campos requeridos
def validate_fields(data, required_fields):
    for field in required_fields:
        if field not in data or data[field] is None:
            return False
    return True

# Función para convertir filas de DataFrame en JSON y enviar POST
def post_data(df, url, required_fields, headers):
    for _, row in df.iterrows():
        # Convertir la fila a un diccionario y luego a JSON
        data = row.to_dict()
        # Limpiar los datos
        data = clean_data(pd.Series(data)).to_dict()
        # Generar UUIDs si es necesario
        if "id" in data and pd.isna(data["id"]):
            data["id"] = str(uuid.uuid4())
        # Convertir las fechas a cadenas
        if "date" in data and data["date"] is not None:
            data["date"] = data["date"].strftime('%Y-%m-%d') if isinstance(data["date"], pd.Timestamp) else data["date"]
        # Validar campos requeridos
        if not validate_fields(data, required_fields):
            print(f'Skipping row due to missing required fields: {data}')
            continue
        response = requests.post(url, data=json.dumps(data), headers=headers)
        try:
            response.raise_for_status()  # Lanza un error si la solicitud falló
            response_json = response.json()
            print(f'Response from {url}:', response.status_code, response_json)
        except requests.exceptions.HTTPError as e:
            print(f'HTTPError: {e}. Response from {url}:', response.status_code, response.text)
        except requests.exceptions.JSONDecodeError:
            print(f'JSONDecodeError: Response from {url}:', response.status_code, response.text)

# Enviar los datos de cada hoja a la URL correspondiente
for sheet_name, url in urls.items():
    df = sheets[sheet_name]
    post_data(df, url, required_fields[sheet_name], headers)