from api_service import check_apis
from email_service import send_email
from config import log
import time

def cron():
    failed_urls = check_apis()

    
    if failed_urls:
        log.warning(f"Existieron errores en los siguientes URLs: {failed_urls}")
        send_email(failed_urls)
