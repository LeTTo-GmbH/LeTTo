"""Prüft den veröffentlichten Suchindex der LeTTo-Doku.
Aufruf: python -I checksearch.py [url] [suchbegriff]
Standard: https://doc.letto.at/search.json und "plugin". Exit-Code 1, wenn die Datei kein gültiges JSON ist."""
import json, sys, random, urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else 'https://doc.letto.at/search.json'
word = (sys.argv[2] if len(sys.argv) > 2 else 'plugin').lower()
# Zufallsparameter umgeht den CDN-Cache
raw = urllib.request.urlopen(f'{url}?v={random.randint(0, 10**9)}', timeout=60).read().decode('utf-8')
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print(f'FEHLER: search.json ist kein gültiges JSON: {e}')
    print('Umgebung der Fehlerstelle:', raw[max(0, e.pos - 200):e.pos + 60])
    sys.exit(1)
hits = [d for d in data if word in (d.get('title', '') + d.get('content', '')).lower()]
print(f'OK: {len(data)} Einträge, {len(hits)} Treffer für "{word}"')
