import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("EVENTBRITE_TOKEN")
EVENT_ID = "abstracta-85471863033"  # Usando la ID que proporcionaste

def obtener_detalles_evento(event_id):
    url = f"https://www.eventbriteapi.com/v3/events/{event_id}/?expand=venue,organizer"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers)
    print("Status:", response.status_code)

    try:
        data = response.json()
        print("\nDetalles del Evento:")
        print(f"Nombre: {data.get('name', {}).get('text', 'Sin nombre')}")
        print(f"Descripción: {data.get('description', {}).get('text', 'Sin descripción')}")
        print(f"Fecha de inicio: {data.get('start', {}).get('local', 'Sin fecha')}")
        print(f"Fecha de fin: {data.get('end', {}).get('local', 'Sin fecha')}")
        venue = data.get('venue', {})
        print(f"Lugar: {venue.get('name', 'Sin lugar')}, {venue.get('address', {}).get('localized_address_display', 'Sin dirección')}")
        organizer = data.get('organizer', {})
        print(f"Organizador: {organizer.get('name', 'Sin organizador')}")
        print(f"¿Gratuito?: {'Sí' if data.get('is_free') else 'No'}")
        print(f"URL del evento: {data.get('url', 'Sin URL')}")

    except Exception as e:
        print("❌ No se pudo decodificar JSON:", e)
        print(response.text)

if __name__ == "__main__":
    obtener_detalles_evento(EVENT_ID)