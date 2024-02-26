import sqlite3

def create_db():
    # Conexión a la base de datos
    conexion = sqlite3.connect('data/health.db')
    cursor = conexion.cursor()

    # Creación de la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls (
                        id INTEGER PRIMARY KEY,
                        url TEXT NOT NULL
                    )''')

    # Commit y cierre de la conexión
    conexion.commit()
    conexion.close()

def insertar_url(url):
    # Conexión a la base de datos
    conexion = sqlite3.connect('data/health.db')
    cursor = conexion.cursor()

    # Inserción de la URL en la tabla
    cursor.execute("INSERT INTO urls (url) VALUES (?)", (url,))
    
    # Commit y cierre de la conexión
    conexion.commit()
    conexion.close()

def obtener_urls():
    # Conexión a la base de datos
    conexion = sqlite3.connect('data/health.db')
    cursor = conexion.cursor()

    # Consulta para obtener todas las URLs de la tabla
    cursor.execute("SELECT url FROM urls")
    
    # Obteniendo los resultados
    resultados = cursor.fetchall()
    
    # Cerrando la conexión
    conexion.close()

    # Extrayendo las URLs de los resultados y almacenándolas en una lista
    urls = [resultado[0] for resultado in resultados]

    return urls

