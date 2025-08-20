import json
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Funktion, um Keys zu bereinigen
def clean_keys(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            clean_key = re.sub(r'[.$#[\]/]', '_', key)
            if clean_key == "":
                clean_key = "_"
            new_obj[clean_key] = clean_keys(value)
        return new_obj
    elif isinstance(obj, list):
        # Prüfen, ob Listenelemente dicts mit "Character" haben
        if all(isinstance(item, dict) and "Character" in item for item in obj):
            return {
                re.sub(r'[.$#[\]/]', '_', item["Character"]): clean_keys({k: v for k, v in item.items() if k != "Character"})
                for item in obj
            }
        else:
            return [clean_keys(item) for item in obj]
    else:
        return obj

# Tkinter-Root verstecken
root = tk.Tk()
root.withdraw()

# Datei-Auswahl-Dialog
input_file = filedialog.askopenfilename(
    title="Wähle deine JSON-Datei aus",
    filetypes=[("JSON-Dateien", "*.json")]
)

if not input_file:
    messagebox.showinfo("Abbruch", "Keine Datei ausgewählt!")
    exit()

# Ausgabe-Dateiname automatisch generieren
output_file = os.path.splitext(input_file)[0] + "_firebase_ready.json"

# JSON einlesen
try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    messagebox.showerror("Fehler", f"JSON konnte nicht geladen werden:\n{e}")
    exit()

# Keys bereinigen & Character-Namen als Keys verwenden
cleaned_data = clean_keys(data)

# Bereinigte JSON speichern
try:
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
    messagebox.showinfo("Erfolg", f"Bereinigte JSON-Datei wurde gespeichert:\n{output_file}")
except Exception as e:
    messagebox.showerror("Fehler", f"Datei konnte nicht gespeichert werden:\n{e}")
