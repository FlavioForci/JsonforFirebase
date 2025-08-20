Firebase JSON Cleaner




A simple Python GUI tool to clean and convert JSON files into Firebase Realtime Database-compatible format. Automatically replaces invalid keys and can use character names as keys instead of numeric indices.

Features

✅ Replace Firebase-invalid characters (., $, #, [, ], /) in keys with _.

✅ Convert arrays of characters into objects with Character names as keys.

✅ Automatically removes "Character" from nested objects to avoid duplication.

✅ GUI-based file selection via tkinter.

✅ Output saved as <original>_firebase_ready.json.

✅ Supports multi-level nested JSON.



Installation

Make sure you have Python 3.6+ installed.

Install dependencies (usually included with Python):

# Tkinter is included with most Python installations
pip install tk


Usage

Run the script:

python clean_json_gui.py


A file dialog will open—select your JSON file.

The cleaned JSON will be saved as <original>_firebase_ready.json in the same folder.

A popup will notify you when the process is complete.

Notes

Works best with arrays of objects containing a "Character" field.

All Firebase-invalid characters in keys are replaced automatically.

Nested lists with characters are automatically converted into objects keyed by "Character".

