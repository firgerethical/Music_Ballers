import overpy

def buscar_teatros_cdmx():
    api = overpy.Overpass()

    # Coordenadas para una zona de CDMX centro: (SurOeste, NorteEste)
    query = """
    node
      ["amenity"="theatre"]
      (19.3,-99.2,19.5,-99.0);
    out;
    """

    result = api.query(query)

    teatros = []
    for node in result.nodes:
        teatros.append({
            "nombre": node.tags.get("name", "Sin nombre"),
            "lat": node.lat,
            "lon": node.lon,
            "tags": node.tags
        })

    return teatros

if __name__ == "__main__":
    resultados = buscar_teatros_cdmx()
    for teatro in resultados[:5]:
        print(f"{teatro['nombre']} - ({teatro['lat']}, {teatro['lon']})")
