import os
from google import genai

# Pega tu nueva API Key entre las comillas
API_KEY = "AQ.Ab8RN6IluMx8tyLcdzlDMak3ZD4RbDU4RMUAmbmQww6W5AL95Q"

client = genai.Client(api_key=API_KEY)

print("====================================")
print("  ¡Asistente de Consola Listo!      ")
print("  Escribe 'salir' para cerrar.      ")
print("====================================\n")

while True:
    pregunta = input("Tú > ")
    
    if pregunta.lower().strip() == "salir":
        print("\n¡Nos vemos!")
        break
        
    if not pregunta.strip():
        continue

    try:
        response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=pregunta
)
        print(f"\nIA > {response.text}\n")
        print("-" * 40)
    except Exception as e:
        print(f"\n[Error]: {e}\n")