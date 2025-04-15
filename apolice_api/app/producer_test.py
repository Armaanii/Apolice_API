import pika
import json

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

# Garante que a fila existe
channel.queue_declare(queue="produto_111", durable=True)

# Payload de teste (completo, conforme esperado pelo worker)
payload = {
    "produto": 111,
    "item": {
        "endereco": {
            "rua": "rua x",
            "numero": 123
        },
        "inquilino": {
            "nome": "José",
            "CPF": "12345678912"
        },
        "beneficiario": {
            "nome": "Imobiliária X",
            "CNPJ": "12345678912345"
        }
    },
    "valores": {
        "precoTotal": 1200.0,
        "parcelas": 5
    }
}

# Publica a mensagem
channel.basic_publish(
    exchange="",
    routing_key="produto_111",
    body=json.dumps(payload),
    properties=pika.BasicProperties(
        delivery_mode=2,  # mensagem persistente
    )
)

print("✅ Mensagem publicada com sucesso!")
connection.close()
