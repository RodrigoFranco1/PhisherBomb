import requests
from faker import Faker

def generar_usuario_falso():
    fake = Faker()
    fake_user = {
        "email": fake.email(),
        "password": fake.password(),
    }
    return fake_user

def enviar_info(url, usuario):
    try:
        # Realizar la solicitud POST
        response = requests.post(url, data=usuario)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print("Datos enviados correctamente.")
        else:
            print(f"Ocurrió un error al enviar los datos. Código de estado: {response.status_code}")

    except requests.RequestException as e:
        print(f"Ocurrió un error al enviar los datos: {e}")

# URL del sitio de phishing
url_phishing = 'http://unbouncepages.com/aadsafgsdgvxbv/'

# Número de intentos que quieres realizar
numero_intentos = 1000

for _ in range(numero_intentos):
    usuario_falso = generar_usuario_falso()
    enviar_info(url_phishing, usuario_falso)
