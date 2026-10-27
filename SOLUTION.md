# EINZIGE AKZEPTIERTE LÖSUNG (BESTÄTIGT)

TEST-ERGEBNIS (27.10.2026):
- `pyparrot.connect` → HANG (alle Versuche fehlgeschlagen)
- `fly_direct()` ohne connect → NEIN, Sumo bewegt sich NICHT (bestätigt)
- `curl` HTTP → 404 / kein Steuer-Endpunkt
- App (FreeFlight 3) → JA, funktioniert

FUNKTIONIERENDE STEUERUNG:
Nur FreeFlight 3 App. Keine Python-Alternative mit diesem Sumo-Zustand.

NÄCHSTE SCHRITTE:
1. Kartierung: App fahren → `wohnung_karte.json` (manuell loggen)
2. Firmware (from scratch): Separates Projekt (`fw/`)
3. Sonar-Mapping: `map_sonar.py` bereit für Daten

Repo: https://github.com/st0rax/jumping-sumo-vision-upcycle
