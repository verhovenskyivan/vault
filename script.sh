#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Использование: $0 <env> <bucket>"
    exit 1
fi

VAULT_TOKEN="ваш_токен"
export VAULT_TOKEN

ENVIRONMENT="$1"
BUCKET="$2"
SECRET_PATH="infra/minio/$ENVIRONMENT/$BUCKET"
PASSWORD=$(openssl rand -base64 20)

vault kv put "$SECRET_PATH" user="$BUCKET" password="$PASSWORD"

echo "Секрет успешно создан в Vault:"
echo "Путь: $SECRET_PATH"
echo "User: $BUCKET"
echo "Password: Сгенерирован"
