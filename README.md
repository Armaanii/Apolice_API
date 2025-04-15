<!-- banner -->
<img src="https://github.com/Armaanii/Apolice_API/blob/main/foto_readme.png>

# Projeto Apólice API

Este projeto é uma API desenvolvida com FastAPI que se conecta a um banco de dados PostgreSQL e utiliza RabbitMQ para processar mensagens e gerar parcelas para diferentes produtos. Ele é projetado para emitir apólices e gerenciar dados de forma eficiente.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção da API.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar as apólices e parcelas.
- **RabbitMQ**: Sistema de mensageria para processamento assíncrono de tarefas.
- **Docker**: Para criação de containers e orquestração de serviços.
- **SQLAlchemy**: ORM para integração com o banco de dados.
- **Pika**: Biblioteca Python para interação com RabbitMQ.

## Requisitos

Antes de rodar o projeto, você deve ter o **Docker** e o **Docker Compose** instalados em sua máquina.
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Rodando o Projeto

### 1. Clonando o Repositório

Clone este repositório para sua máquina local:

````
git clone https://github.com/Armaanii/Apolice_API/tree/main/apolice_api
````
- cd apolice-api

---------------------------------------------------------------------------------------------

2. Configurando o Docker
- Com o Docker e o Docker Compose configurados, crie e suba os containers necessários:
````
docker-compose up --build
````

## Esse comando irá:
- Construir e iniciar a API FastAPI
- Iniciar o banco PostgreSQL
- Iniciar o RabbitMQ com interface gráfica
- Iniciar os workers (worker_111 e worker_222)

🐇 Acessando o RabbitMQ

-- Abra no navegador:
````
http://localhost:15672
````

## Login padrão:
- #### Usuário: guest
- #### Senha: guest

As filas produto_111 e produto_222 estarão disponíveis na aba "Queues".


## 🔍 Iniciando o Worker

Para iniciar o worker, execute o comando abaixo:
````
docker-compose run --rm worker_111
````
````
docker-compose run --rm api python app/producer_test.py
````
O worker irá começar a escutar as mensagens na fila do RabbitMQ e processá-las, 
inserindo as parcelas no banco de dados PostgreSQL.

## 4. Verificando o Banco de Dados

Para verificar se as parcelas foram inseridas no banco de dados PostgreSQL, 
você pode acessar o banco de dados diretamente com o comando abaixo:
````
docker exec -it postgres_db psql -U user -d apolice -c "SELECT * FROM parcela;"
````

## 5. Enviando uma Mensagem de Teste

Você pode usar o script producer_teste.py para enviar uma mensagem de teste para o RabbitMQ:
````
docker-compose run --rm api python app/producer_test.py
````
````
docker-compose run --rm api python app/producer2_test.py
````

Esse comando irá enviar uma mensagem com os dados de exemplo para a fila produto_111. 
O worker irá processar essa mensagem e inserir as parcelas no banco de dados.

## 6. Teste de envio de um Produto inexistente

Foi criado um teste com nome ````test_produto_invalido.py```` nele foi feito toda tratativa para de erro, 
conforme a mensagem abaixo após rodar o arquivo.

Quando você rodar esse teste:
````
python app/test_produto_invalido.py
````

Resultado esperado da api.

````
- Status Code: 400
- Resposta: {'detail': 'Produto não suportado'}
````

## 7. Acessando a API
Após a construção e execução do Docker Compose, a API estará disponível 
em http://localhost:8000. Você pode acessar os endpoints definidos e verificar a 
documentação automática do FastAPI em:
- Documentação da API: http://localhost:8000/docs
- Redefinição do OpenAPI: http://localhost:8000/redoc

## 8. Parando os Containers
Para parar todos os containers, execute o comando abaixo:
````
docker-compose down
````

- Isso irá parar e remover os containers, mas manterá os volumes persistentes (como o banco de dados).

## 🔄 Limpando o Banco de Dados (opcional)
````
docker exec -it postgres_db psql -U user -d apolice
````

No terminal interativo do PostgreSQL, execute:
````
TRUNCATE TABLE parcela RESTART IDENTITY;
````

## ⚙️ Regras de Negócio
- Produto 111
- Campos obrigatórios:
    - Endereço do imóvel
    - Dados do inquilino (nome e CPF)
    - Dados do beneficiário (nome e CNPJ)

- Produto 222
- Campos obrigatórios:
    - Placa do carro
    - Chassi
    - Modelo do veículo

## 📬 Estrutura Esperada do Payload
- Produto 111

```
{
  "produto": 111,
  "item": {
    "endereco": {"rua": "Rua X", "numero": 123},
    "inquilino": {"nome": "José", "CPF": "12345678912"},
    "beneficiario": {"nome": "Imobiliária X", "CNPJ": "12345678912345"}
  },
  "valores": {
    "precoTotal": 1200.0,
    "parcelas": 6
  }
}
```
- Produto 222

```
{
  "produto": 222,
  "item": {
    "placa": "ABC1234",
    "chassi": "123231",
    "modelo": "Porsche"
  },
  "valores": {
    "precoTotal": 3000.0,
    "parcelas": 12
  }
}
```

## Considerações Finais
Este é um projeto básico para gerenciar apólices e processar parcelas usando RabbitMQ e PostgreSQL. 
Você pode estender as funcionalidades para adicionar mais filas, workers, e lógica de processamento conforme necessário.

Caso tenha dúvidas ou problemas ao executar o projeto, não hesite em entrar em contato ou consultar 
a documentação oficial das ferramentas utilizadas.

#### *Autor: Rodrigo Guedes*

Esse arquivo `README.md` serve como um guia para configurar, executar e testar a API com os contêineres do Docker. 
Ele cobre desde a inicialização do projeto até como interagir com a API e testar a integração do worker.



