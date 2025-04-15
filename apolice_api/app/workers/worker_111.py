import pika
import json
from app.core.database import SessionLocal
from app.core.models import Parcela
from app.core.schemas import Produto111

def callback(ch, method, properties, body):
    print("📥 Mensagem recebida, processando...")
    try:
        # Carrega e valida os dados recebidos com o schema Produto111
        data = json.loads(body)
        payload = Produto111(**data)

        session = SessionLocal()
        valor_parcela = payload.valores.precoTotal / payload.valores.parcelas

        for i in range(1, payload.valores.parcelas + 1):
            parcela = Parcela(
                numero=i,
                valor=valor_parcela,
                produto=payload.produto
            )
            session.add(parcela)

        session.commit()
        session.close()

        print("✅ Mensagem processada e parcelas salvas com sucesso!")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print("❌ Erro ao processar mensagem:", e)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()

        channel.queue_declare(queue="produto_111", durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue="produto_111", on_message_callback=callback)

        print("✅ Worker 111 conectado ao RabbitMQ e aguardando mensagens na fila 'produto_111'...")
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print("🚫 Não foi possível conectar ao RabbitMQ:", e)

if __name__ == "__main__":
    main()
