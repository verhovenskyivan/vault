import string
import random
from pyvault import Client

client = Client()

client.auth.login(url='',token='')

def generate_password(length=15):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_user_folder(bucket):
    folder_path = f'goods/infra/datasource/minio/prod/{bucket}'
    
    # Создаем папку пользователя в Vault
    response = client.secrets.kv.v1.create_or_update_secret(folder_path, {})
    
    if response.status_code == 200:
        print(f"Папка для  {bucket} успешно создана в Vault.")
    else:
        print("Ошибка при создании папки  в Vault.")

def write_credentials_to_vault(bucket, password):
    folder_path = f'goods/infra/datasource/minio/prod/{bucket}'
    
    response = client.secrets.kv.v1.create_or_update_secret(folder_path, {'user': bucket, 'password': password})
    
    if response.status_code == 200:
        print(f"Имя пользователя и пароль успешно сохранены в Vault для пользователя {bucket}.")
    else:
        print("Ошибка при записи данных в Vault.")

if __name__ == "__main__":
    bucket = input("Введите бакет: ")
    password = generate_password()
    print(f"Сгенерированный пароль для пользователя {bucket}: {password}")
    
    create_user_folder(bucket)
    write_credentials_to_vault(bucket, password)
