# LuzIA Unofficial API

This is a simple unofficial API for interacting with LuzIA, created using Flask. The API allows you to send messages and maintain context for conversations by providing a unique chat ID.

---

# LuzIA API No Oficial

Esta es una sencilla API no oficial para interactuar con LuzIA, creada con Flask. La API permite enviar mensajes y mantener el contexto de las conversaciones proporcionando un ID de chat único.

---

## Features / Características

- **Maintain conversation context** using unique chat IDs.
- **Simple integration** with any project.
- **Free to use** for personal or development purposes.

- **Mantener el contexto de la conversación** utilizando IDs de chat únicos.
- **Integración sencilla** con cualquier proyecto.
- **Uso gratuito** para propósitos personales o de desarrollo.

---

## Usage / Uso

### Sending a Request / Enviando una Solicitud

#### Python Example / Ejemplo en Python

```python
import requests

# Server URL / URL del servidor
url = "http://195.35.9.209:9474/chat"
tet = input("Text: ")

# Request payload / Datos para la solicitud
payload = {
    "content": tet,
    "chatid": "test_chat_123"
}

# Request headers / Encabezados para la solicitud
headers = {
    "Content-Type": "application/json"
}

# Sending the POST request / Realizando la solicitud POST
try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Server response:")
        print(response.json())
    else:
        print(f"Error: Status code {response.status_code}")
        print(response.json())
except Exception as e:
    print(f"An error occurred: {e}")
```
