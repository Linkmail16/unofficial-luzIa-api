import requests

url = "http://195.35.9.209:9474/chat"
text = input("Text: ")

payload = {
    "content":text,
    "chatid": "test_chat_123"
}

headers = {
    "Content-Type": "application/json"
}
try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Respuesta del servidor:")
        print(response.json())
    else:
        print(f"Error: Código de estado {response.status_code}")
        print(response.json())
except Exception as e:
    print(f"Ocurrió un error al hacer la solicitud: {e}")
