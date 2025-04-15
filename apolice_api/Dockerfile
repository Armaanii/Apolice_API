# Use uma imagem base mais completa com apt-get
FROM python:3.10-buster

# Instala dependências necessárias, incluindo o nc (netcat)
RUN apt-get update && apt-get install -y netcat

# Define o diretório de trabalho no container
WORKDIR /code

# Copia os arquivos para o diretório de trabalho
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000 para a API
EXPOSE 8000
