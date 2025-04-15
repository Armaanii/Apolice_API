import requests

url = "http://localhost:8000/emitir"

# Payload com produto inexistente
payload = {
    "produto": 999,  # Produto inválido
    "item": {
        "qualquer": "valor"
    },
    "valores": {
        "precoTotal": 1000,
        "parcelas": 2
    }
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Resposta:", response.json())
