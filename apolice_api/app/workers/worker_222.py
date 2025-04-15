import pika
import json
from app.core.database import SessionLocal
from app.core.models import Parcela
from app.core.schemas import Produto222
from pydantic import ValidationError


def callback(ch, method, properties, body):
    print("📥 Mensagem recebida, processando...")
    try:
        # Carrega e valida os dados recebidos com o schema Produto111
        data = json.loads(body)
        payload = Produto222(**data)

        session = SessionLocal()
        valor_parcela = payload.valores.precoTotal / payload.valores.parcelas

        for i in range(1, payload.valores.parcelas + 1):
            parcela = Parcela(
                numero=i,
                valor=valor_parcela,
                produto=222
            )
            session.add(parcela)

        session.commit()
        session.close()

        print("✅ Mensagem processada e parcelas salvas com sucesso!")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    except ValidationError as ve:
        print("❌ Erro de validação nos dados do Produto 222:", ve)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    except Exception as e:
        print("❌ Erro inesperado no processamento:", e)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()

        channel.queue_declare(queue="produto_222", durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue="produto_222", on_message_callback=callback)

        print("✅ Worker 222 conectado ao RabbitMQ e aguardando mensagens na fila 'produto_222'...")
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print("🚫 Não foi possível conectar ao RabbitMQ:", e)

if __name__ == "__main__":
    main()
