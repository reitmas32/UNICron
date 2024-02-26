import sys
from urls import insertar_url

def main():
    # Verificar si se proporciona la URL como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
        sys.exit(1)

    # Obtener la URL del primer argumento
    url = sys.argv[1]

    # Llamar a la función insertar_url con la URL proporcionada
    insertar_url(url)
    print(f"URL '{url}' insertada correctamente en la base de datos.")

if __name__ == "__main__":
    main()
