"""
Sumo LLM Harness — klein, performant, kein LLM auf dem Sumo.
LLM (TinyLLaMA / lokal) sendet Text -> Harness -> pyparrot Befehl.
"""

# Mapping: natürliche Sprache -> pyparrot Aktion
COMMAND_MAP = {
    "vorwärts": (0, 40, 0, 0, 2),
    "rückwärts": (0, -40, 0, 0, 2),
    "links": (0, 0, -30, 0, 2),
    "rechts": (0, 0, 30, 0, 2),
    "komm": (0, 10, 0, 0, 3),
    "stop": (0, 0, 0, 0, 1),
    "jump": "flip",  # optional
}

def execute(text_command, sumo_conn):
    text = text_command.lower()
    if text in COMMAND_MAP:
        cmd = COMMAND_MAP[text]
        if isinstance(cmd, tuple):
            roll, pitch, yaw, vert, dur = cmd
            sumo_conn.fly_direct(roll, pitch, yaw, vert, dur)
            return f"ausgeführt: {text}"
        else:
            return f"aktion: {cmd}"
    return "unbekannt — nur vorwärts/rückwärts/links/rechts/komm/stop"
