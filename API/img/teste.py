import requests
import base64
import json

# Caminho da imagem local
CAMINHO_IMAGEM = "notebook.jpg"

# URL da API
URL_API = "http://127.0.0.1:5000/itens"

# Lê a imagem e converte para Base64
with open(CAMINHO_IMAGEM, "rb") as img:
    foto_bem_base64 = base64.b64encode(img.read()).decode("utf-8")

# Corpo da requisição
dados = {
    "nome": "Notebook Dell Inspiron 15",
    "descr": "Notebook utilizado no laboratório de informática",
    "categoria": "Eletrônico",
    "valor": 3500.00,
    "foto_bem": foto_bem_base64,
    "qrcode": "NOTB-001",
    "observacao": "Equipamento em bom estado",
    "estado_fisico": "Bom",
    "condicao_uso": "Operacional",
    "conservacao": "Adequada",
    "funcionalidade": "Completa",
    "id_unidade": 1,
    "id_departamento": 2,
    "id_sala": 3
}

# Envia a requisição POST
response = requests.post(URL_API, json=dados)

# Exibe o resultado
print("Status:", response.status_code)
print("Resposta:", response.text)
