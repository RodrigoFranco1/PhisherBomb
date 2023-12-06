import requests
from faker import Faker
import argparse

def generar_usuario_falso():
    fake = Faker()
    fake_user = {
        "email": fake.email(),
        "password": fake.password(),
    }
    return fake_user

def enviar_info(url, usuario):
    try:
        response = requests.post(url, data=usuario)
        if response.status_code == 200:
            print("Datos enviados correctamente.")
        else:
            print(f"Error al enviar datos. Código de estado: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error al enviar datos: {e}")

def main(url, numero_intentos):
    for _ in range(numero_intentos):
        usuario_falso = generar_usuario_falso()
        enviar_info(url, usuario_falso)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PhisherBomb: Herramienta para inundar sitios de phishing con datos falsos.")
    parser.add_argument("-u", "--url", required=True, help="URL del sitio de phishing")
    parser.add_argument("-r", "--requests", type=int, default=100, help="Número de solicitudes falsas a enviar")
    args = parser.parse_args()

    main(args.url, args.requests)
