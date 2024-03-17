import hvac
import random
import string
import getpass

ENVIRONMENT = input("Введите значение env (test/prod): ")
BUCKET = input("Введите название бакета: ")
SECRET_PATH = f"infra/minio/{ENVIRONMENT}/{BUCKET}"

PASSWORD = getpass.getpass(prompt="Введите пароль для секрета: ")

if not PASSWORD:
    PASSWORD_LENGTH = 20
    PASSWORD_CHARS = string.ascii_letters + string.digits
    PASSWORD = ''.join(random.choice(PASSWORD_CHARS) for _ in range(PASSWORD_LENGTH))

client = hvac.Client(url=SECRET_PATH, token=os.environ["MM_VAULT_TOKEN"])

try:
    client.secrets.kv.v2.create_or_update_secret(
        path=SECRET_PATH,
        secret=dict(user=BUCKET, password=PASSWORD)
    )
    print("Секрет успешно создан в Vault:")
    print("Путь:", SECRET_PATH)
    print("User:", BUCKET)
    print("Password:")
except Exception as e:
    print("Произошла ошибка при создании секрета в Vault:", e)
