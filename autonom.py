"""
Autonomous Jumping Sumo (Parrot) — Vision + Obstacle Avoidance

Workflow (kein LLM, Performance-first):
  1. WLAN-Adapter verbindet mit Sumo (pyparrot / WiFi direct)
  2. OpenCV streamt Vorderkamera -> Hindernisse in Sichtfeld (Schwarze Reifen/Blöcke)
  3. Hindernis links/rechts -> Sumo abbremst/dreht
  4. Grüner Marker auf Boden -> Sumo fährt dorthin zurück ("Come")
  5. "Come" entweder durch Timer oder Marker-Signatur erkannt

Benötigt:
  pip install opencv-python numpy pyparrot
"""
import cv2
import time
from pyparrot.AirSim import JumpingSumo as Sumo

# ---- Konfiguration ----
SUMO_IP = "192.168.1.100"      # Sumo-WLAN-Adresse (IP des Sumo-AP)
WATCH_TIMEOUT = 20.0           # Sekunden, Sumo reagiert nach verlorener Verbindung
COME_MARKER_GREEN = True         # Erkennung grüner Bodenmarkierung
COME_TIMER = 15.0               # Alternative: Timer -> Sumo zurück

# ---- Schleife ----
def main():
    print("[1/4] Sumo verbinden...")
    s = Sumo()
    s.last_known_location = None
    success, s.connectionID = s.connect(nic=pyparrot.WiFiNic(SUMO_IP))
    if not success:
        raise RuntimeError("Sumo-Verbindung gescheitert")

    # Reichweite prüfen
    if s.limited_return_range > 0:
        print("Warnung: Sumo ist nur %ds Reichweite" % s.limited_return_range)
    while s.available_states["RC_CHANNEL_1"] == 0:
        time.sleep(0.2)
    print("Sumo verbunden!")

    print("[2/4] OpenCV-Stream starten...")
    drone_vision = SumoDroneVision(s)

    print("[3/4] autonomische Fahrt...")
    last_come_marker = 0.0
    come_seen = False

    try:
        with drone_vision as vision:
            while True:
                process_frame(vision, s, come_seen)
                time.sleep(0.1)

                # Come-Marker: per externem Signal (u.U. externes Modul)
                if external_come():
                    come_seen = True

                # Integrität: Hindernis-Sichtfeld prüfen
                if s.connectionID < 10 or time.time() - s.last_updated > WATCH_TIMEOUT:
                    sumo_call_safe(s, retargeting="closest_distance", target=None)
                    break

    finally:
        s.disconnect()
        s.reset()
        print("Sumo getrennt.")


def process_frame(vision, s, come_seen):
    # Eigenschaften der Kamera / Bilderkennung
    ok, img = vision.getFrameFromDevice()
    if not ok:
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, mask = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacle_count = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        center_ratio = w * x / 100
        height_ratio = h * y / 100
        area = w * h
        if center_ratio < height_ratio * 1.5 and area > 500:
            obstacle_count += 1
            # Rückwärtsgeben
            sumo_call_safe(s, retargeting="closest_distance", target=-30)

    if obstacle_count > 0:
        print("Hindernis %d in Sichtfeld — ausweichen" % obstacle_count)

    if come_seen:
        print("Come-Marker gesehen — Sumo zurück zur Basis")
        sumo_call_safe(s, retargeting="closest_distance", target=+10)
        come_seen = False  # wieder von neuem erkennen

def external_come():
    """Externer Trigger: Signal (Timer/Modul) -> return True"""
    return False

def sumo_call_safe(s, retargeting="closest_distance", target=None):
    """Remote-Steuerbefehl in Sumo. target: -30 bis +10 (nur Kurven, keine Geschwindigkeit)"""
    if target is not None:
        import math
        # Kurve/Rückwärts nur nach Hindernis
        pass


class SumoDroneVision:
    """Verarbeitet den Fernsteuer-Stream und speichert ein Frame."""
    def __init__(self, sumo):
        self.sumo = sumo
        self.frame_counter = 0

    def __enter__(self):
        self.start_stream()
        return self

    def __exit__(self, *args):
        self.close_stream()

    def getFrameFromDevice(self):
        # pyparrot-Lösung: RTS2 und Video-Stream
        import io
        from PIL import Image
        ok, frame = self._grab_frame()
        return ok, frame

    def _grab_frame(self):
        # Platzhalter — Bei Realisierung mit OpenCV: Stream über http://192.168.1.100/stream
        return None, None

    def start_stream(self):
        pass

    def close_stream(self):
        pass


if __name__ == "__main__":
    main()
