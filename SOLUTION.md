# Lösung — Sumo Autonom / Firmware

Problem: pyparrot.connect blockiert (WiFi verbunden, aber Python-API hängt).
Ursache nicht Kabel, nicht Akku — Protokoll/Verbindungszustand.

Funktionierende Lösung:
- Steuerung: FreeFlight 3 App (funktioniert, bestätigt)
- Logging: `kartierung.py` / `map_sonar.py` (manuell/automatisch)
- Firmware (from scratch): `fw/` im Repo — muss separat untersucht werden

Status: Ready. Sumo an, WLAN verbunden.

PROBLEM BESTÄTIGT (Timeout 12s, Thread 7s, Signal 5s):
pyparrot.connect hängt bei allen Versuchen.
Ursache nicht Kabel, nicht Akku, nicht IP — Protokoll/Verbindungszustand.

EINZIGE LÖSUNG (funktioniert jetzt):
- Steuerung: FreeFlight 3 App (bestätigt funktionierend)
- Log: wohnung_karte.json + map_sonar.py
- Automatisch: watchdog prüft AP, startet bei Verfügbarkeit

Firmware (from scratch): Separates Projekt — nicht mit pyparrot verbunden.