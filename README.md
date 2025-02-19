# LuzIA Unofficial API

This is a simple unofficial API for interacting with LuzIA, created using Flask. The API allows you to send messages and maintain context for conversations by providing a unique chat ID.

---

# LuzIA API No Oficial

Esta es una sencilla API no oficial para interactuar con LuzIA, creada con Flask. La API permite enviar mensajes y mantener el contexto de las conversaciones proporcionando un ID de chat único.

---

## Changelog
### v1.1 - 2025-02-18 

### 🔹 Added option to enable/disable chat context
- Now you can decide whether to use conversation history by including the `chatContext` parameter.
- If `"chatContext": false` is sent in the request, the message will be processed **without any previous context**.
- If `"chatContext"` is omitted or set to `true`, the message will be processed **with full conversation history**.

### 🔹 Improved documentation
- Added clearer explanations and examples for better integration.

---

## Historial de cambios
### v1.1 - 2025-02-18 

### 🔹 Añadida opción para activar/desactivar el contexto del chat
- Ahora puedes decidir si usar el historial de la conversación incluyendo el parámetro `chatContext`.
- Si envías `"chatContext": false` en la solicitud, el mensaje será procesado **sin historial previo**.
- Si omites `"chatContext"` o lo estableces en `true`, el mensaje será procesado **con el historial completo de la conversación**.

### 🔹 Mejora en la documentación
- Se agregaron explicaciones más claras y ejemplos para una mejor integración.

---

## Features / Características

- **Maintain conversation context** using unique chat IDs.
- **Simple integration** with any project.
- **Free to use** for personal or development purposes.
---
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
text = input("Text: ")

# Request payload / Datos para la solicitud
payload = {
    "content": text, # Message to send / Mensaje a enviar
    "chatid": "test_chat_123", # Unique chat ID / ID unico del chat
    "chatContext": True # ¨EN¨ Decide whether to use chat history or not (True/False)
    # ¨EN¨ or simply omit this variable if you want to use context by default
    # ¨ES¨ Decide si usar un chat con contexto o no (True/False)
    # ¨ES¨ o simplemente no coloques esta variable si quieres usar contexto
}

# Request headers / Encabezados para la solicitud
headers = {
    "Content-Type": "application/json"
}

# Sending the POST request / Realizando la solicitud POST
try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: Status code {response.status_code}")
        print(response.json())
except Exception as e:
    print(f"An error occurred: {e}")
```

### Example Response / Ejemplo de Respuesta

The server response will look like this:

La respuesta del servidor lucirá así:

```json
{
    "content": "¡Hola! Estoy muy bien, gracias. ¿Y tú? ¿Cómo va tu día?"
}
```
