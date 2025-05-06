import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

QUERIES = [
    "conciertos en vivo en CDMX",
    "centros culturales Ciudad de México",
    "bares con música electrónica",
    "eventos culturales gratuitos",
    "galerías de arte con eventos musicales"
]

def buscar_lugares(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "region": "mx",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"❌ Error en la búsqueda: {query}")
        return []

    data = response.json()
    return data.get("results", [])[:3]  # Tomamos los primeros 3 de cada query

def main():
    todos_lugares = []

    for q in QUERIES:
        print(f"\n🔎 Buscando: {q}")
        lugares = buscar_lugares(q)
        for lugar in lugares:
            nombre = lugar.get("name")
            direccion = lugar.get("formatted_address")
            rating = lugar.get("rating", "Sin rating")
            tipos = ", ".join(lugar.get("types", []))
            print(f"🎶 {nombre}\n📍 {direccion}\n⭐ {rating}\n🗂️ {tipos}\n")
            todos_lugares.append({
                "nombre": nombre,
                "direccion": direccion,
                "rating": rating,
                "tipos": tipos
            })

    print(f"\n✅ Total lugares recolectados: {len(todos_lugares)}")

if __name__ == "__main__":
    main()
