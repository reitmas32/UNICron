import requests
import time
from config import MAX_RETRIES, WAIT_TIME
from config import log
from urls import obtener_urls

def check_apis():
    failed_urls = []
    lista_urls = obtener_urls()
    for url in lista_urls:
        log.msg("\n\n")
        log.msg(f"{'*'*100}")
        log.msg(f"CONSULTADO SALUD DE: {url}")
        log.msg(f"{'*'*100}")
        success_api = False
        for attempt in range(MAX_RETRIES):
            try:
                log.msg(f"Intento: {attempt+1}, consultado a la url: {url} ")
                response = requests.get(url)
                if response.status_code == 200:
                    log.msg("response==> success")
                    success_api = True
                    break
                else:
                    log.error(f"response==> failed, status_code==> {response.status_code}")
            except Exception:
                log.error("response=> failed")
            time.sleep(WAIT_TIME)

        if not success_api:
            failed_urls.append(url)
            

    return failed_urls
