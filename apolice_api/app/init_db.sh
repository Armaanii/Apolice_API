#!/bin/bash

echo "Aguardando banco de dados ficar disponível..."

# Espera o banco subir antes de tentar conectar
while ! nc -z postgres_db 5432; do
  echo "Aguardando banco de dados"
  sleep 3
done

echo "Banco de dados disponível! Criando tabelas..."
python app/init_db.py

echo "Tabelas criadas com sucesso!"
