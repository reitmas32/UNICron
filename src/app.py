from flask import Flask
import os
import cron
import time
import multiprocessing
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

def runCron():
    while True:
        cron.cron()
        time.sleep(60)

if __name__ == '__main__':
        # Crea un proceso para ejecutar la función
    proceso = multiprocessing.Process(target=runCron)

    # Inicia el proceso
    proceso.start()
    app.run(host='0.0.0.0', port=5000)
