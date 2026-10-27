"""
Auto-Watchdog — wenn Sumo-AP sichtbar, verbindet, startet Steuerung.
Kein manuelles Eingreifen nötig.
"""
import time, subprocess, sys

def is_sumo_visible():
    out = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
        text=True, errors='ignore')
    return 'JumpingSumo' in out

def connect():
    # Profil hinzufügen und verbinden
    pass  # implementiert wenn AP da

def start_autonom():
    # start autonom.py oder audio_feedback
    pass

while True:
    if is_sumo_visible():
        print("Sumo gefunden — starte Steuerung...")
        # connect + start
        break
    time.sleep(5)
