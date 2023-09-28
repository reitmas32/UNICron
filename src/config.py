import os
import structlog


os.environ["API_URLS"] = """
https://yonesto-api-prod.onrender.com/health,https://uniaccounts-api-prod.onrender.com/health,
https://yonesto-api-dev.onrender.com/health,https://uniaccounts-api-dev.onrender.com/health,
https://yonesto-api-stg.onrender.com/health,https://uniaccounts-api-stg.onrender.com/health,
https://yonesto-web.onrender.com/,https://unicron-test-example-one.onrender.com/,

"""
os.environ["SUPPORT_TEAM"] = "David Roni Hernández Beltrán:roni.hernandez.1999@gmail.com,Oswaldo Rafael Zamora Ramírez:rafa.zamora.rals@gmail.com"
os.environ["GMAIL_USER"]="unicapp.mail@gmail.com"
os.environ["GMAIL_PASSWORD"]="qhfkiqbplqlprhdt"


log = structlog.get_logger()


# Datos de Gmail
GMAIL_USER = os.environ.get('GMAIL_USER')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

# Convertir las variables de entorno a listas de Python
def parse_support_team(data):
    entries = data.split(',')
    return [{'name': entry.split(':')[0], 'email': entry.split(':')[1]} for entry in entries]

def parse_api_urls(data):
    return data.split(',')

# Lista de soporte y URLs a verificar
SOPORTE = parse_support_team(os.environ.get('SUPPORT_TEAM', ""))
PAGINAS_REVISAR = parse_api_urls(os.environ.get('API_URLS', ""))

# Otros valores configurables
MAX_RETRIES = 10
WAIT_TIME = 3
