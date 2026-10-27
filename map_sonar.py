"""
Sonar-Mapping — einfache 2D-Karte via Sumo-Sonar (Abstand/Höhe).
Leicht, kein LLM nötig.
"""
MAP_GRID = {}

def add_point(angle, distance):
    # Einfaches Polar -> Kartesisch Mapping
    x = int(distance * 0.1)  # Skalierung
    y = int(angle * 0.5)
    MAP_GRID[(x, y)] = distance
    print(f"Punkt: Winkel={angle}°, Distanz={distance}cm -> ({x},{y})")

def print_map():
    for k, v in MAP_GRID.items():
        print(f"  {k}: {v}cm")
