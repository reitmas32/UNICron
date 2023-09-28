import requests
import time
from config import PAGINAS_REVISAR, MAX_RETRIES, WAIT_TIME
from config import log

def escribir_en_archivo(texto):
    nombre_archivo = "logs/urls.log"
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(texto + '\n')
        print(f'Se ha escrito en el archivo "{nombre_archivo}" con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al escribir en el archivo "{nombre_archivo}": {str(e)}')

def check_apis():
    failed_urls = []
    for url in PAGINAS_REVISAR:
        escribir_en_archivo("\n\n")
        escribir_en_archivo(f"{'*'*100}")
        escribir_en_archivo(f"CONSULTADO SALUD DE: {url}")
        escribir_en_archivo(f"{'*'*100}")
        success_api = False
        for attempt in range(MAX_RETRIES):
            try:
                escribir_en_archivo(f"Intento: {attempt+1}, consultado a la url: {url} ")
                response = requests.get(url)
                if response.status_code == 200:
                    escribir_en_archivo(f"response==> success")
                    success_api = True
                    break
                else:
                    escribir_en_archivo(f"response==> failed, status_code==> {response.status_code}")
            except Exception:
                escribir_en_archivo(f"response=> failed")
            time.sleep(WAIT_TIME)

        if not success_api:
            failed_urls.append(url)
            

    return failed_urls
