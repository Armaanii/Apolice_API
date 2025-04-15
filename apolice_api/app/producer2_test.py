import pika
import json

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

# Garante que a fila exista
channel.queue_declare(queue="produto_222", durable=True)

# Payload de teste para o Produto 222 (seguros de veículos)
payload = {
    "produto": 222,
    "item": {
        "placa": "ABC1D23",
        "chassi": "ABCDE123",
        "modelo": "Porsche"
    },
    "valores": {
        "precoTotal": 3000.0,
        "parcelas": 12
    }
}

# Publica a mensagem
channel.basic_publish(
    exchange="",
    routing_key="produto_222",
    body=json.dumps(payload),
    properties=pika.BasicProperties(
        delivery_mode=2,  # torna a mensagem persistente
    )
)

print("✅ Mensagem do produto 222 publicada com sucesso!")
connection.close()
