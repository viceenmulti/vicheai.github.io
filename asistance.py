import os
import json
import urllib.request

# Intenta leer la clave desde el entorno o archivo local
API_KEY = os.environ.get("GEMINI_API_KEY")

# Si no la encuentra guardada, se la pide al usuario
if not API_KEY:
    API_KEY = input("Ingresa tu API Key de Gemini: ").strip()

MODELO = "gemini-1.5-flash"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:generateContent?key={API_KEY}"

print("====================================")
print("  ¡Asistente Gemini Listo!          ")
print("====================================\n")

while True:
    pregunta = input("Tú > ")
    if pregunta.strip().lower() == "salir":
        break
    if not pregunta.strip():
        continue

    payload = {
        "contents": [{
            "parts": [{"text": pregunta}]
        }]
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            texto = res_body["candidates"][0]["content"]["parts"][0]["text"]
            print(f"\nIA > {texto}\n")
            print("-" * 40)
    except Exception as e:
        print(f"\n[Error]: {e}\n")
