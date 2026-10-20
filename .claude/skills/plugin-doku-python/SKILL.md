---
name: plugin-doku-python
description: Erzeugt oder aktualisiert die Doku des Python-Referenz-Plugins (plugin-demo-python, FastAPI) unter docs/wiki/Plugins/referenz-plugin-python aus dem Sourcecode – mit Links auf die Endpunkt- und DTO-Seiten der Java-Doku und den Unterschieden der Python-Version. Verwenden, wenn die Python-Plugin-Doku neu erstellt, aktualisiert oder mit dem Code abgeglichen werden soll.
---

# Doku des Python-Referenz-Plugins generieren

Erzeuge bzw. aktualisiere die Dokumentation des Python-Referenz-Plugins für die GitHub-Pages-Doku von LeTTo.

Die Python-Version ist eine Portierung des Java-Referenz-Plugins mit **derselben REST-Schnittstelle**. Die ausführliche Beschreibung
jedes Endpunkts, DTOs und Enums steht deshalb in der Java-Doku (`docs/wiki/Plugins/referenz-plugin-java/`, erzeugt mit dem Skill `plugin-doku`).
Die Python-Doku beschreibt die Python-Umsetzung, verlinkt für Details auf die Java-Seiten und nennt jede Abweichung.
Eigene Seiten je Endpunkt oder DTO gibt es für Python **nicht**.

## Quelle und Ziel

- **Quelle:** `../plugin-demo-python` (Repo https://github.com/LeTTo-GmbH/plugin-demo-python), relativ zum LeTTo-Repo-Root.
  Das LeTTo-Repo bindet es über `additionalDirectories` in `.claude/settings.json` ein. Ist es nicht erreichbar: abbrechen und den Benutzer
  bitten, beide Repos nebeneinander auszuchecken.
- **Ziel:** `docs/wiki/Plugins/referenz-plugin-python/` – Dateien außerhalb dieses Ordners nur wie unter „Verlinkung" beschrieben ändern.
- **Voraussetzung:** Die Java-Doku existiert und ist aktuell; die Python-Seiten verlinken auf deren Endpunkt-, DTO- und Enum-Seiten.
  Fehlt eine verlinkte Java-Seite, zuerst den Skill `plugin-doku` ausführen (bzw. den Benutzer darauf hinweisen).

Relevante Quellen im Plugin-Repo:

| Quelle | Inhalt für die Doku |
|---|---|
| `README.md`, `dockerhub/README.md` | Build, Installation, Tests, Debugging, Endpunkt-Übersicht, Docker Hub |
| `app/main.py` | der gesamte Service: `CONF_*`-Konstanten, Umgebungsvariablen, Pfade, Pydantic-DTOs, Klasse `PluginDemo`, `REGISTERED_PLUGINS`/`create_plugin`, Registrierung, Konfigurationssitzungen, Endpunkte (`mount_internal_open`, `extern_router`, `@app.get`), OpenAPI-Links |
| `resources/index.html`, `resources/plugins/<plugin>/*` | Hilfeseite, Hilfetext und JavaScript des Plugins |
| `tests/*` | was die Tests abdecken |
| `Dockerfile`, `build.bat`, `yml/`, `proxy/`, `scripts/` | Build, Docker, Compose, Proxy, Start- und Healthcheck-Script |
| `img.png` | Screenshot der PyCharm-Debug-Konfiguration (als `build-deployment/pycharm-debug.png` übernehmen) |

## Seitenstruktur

Gleiche Gliederung wie die Java-Doku, jede Seite ein eigener Ordner mit `index.md`:

```
docs/wiki/Plugins/referenz-plugin-python/
  index.md                     Überblick, technische Daten (Versionen aus requirements.txt/Dockerfile), Links, Tabelle „Python oder Java?", Inhaltsverzeichnis
  architektur/index.md         Abschnitte von app/main.py, weitere Dateien, Erreichbarkeit der Pfade, Konfigurationssitzungen, Registrierung
  eigenes-plugin/index.md      neues Plugin aus dem Python-Demo: alle Stellen für Servicepfad/Namen, CONF_*, Plugin-Klasse, Registrierung, Ressourcen, Tests
  plugin-api/index.md          alle CONF_*-Konstanten mit Java-Gegenstück, Methoden von PluginDemo mit Endpunkt und Java-Gegenstück, Uhr-Plugin inkl. Bewertung im Vergleich zu Java
  rest-schnittstelle/index.md  alle Endpunkte: Methode, Pfad, Request, Response, Spalte „Python" (tatsächliches Verhalten), Link auf die Java-Endpunkt-Seite
  dtos/index.md                alle Pydantic-Modelle mit Link auf die Java-DTO-Seite und Spalte „Abweichung"; Java-Klassen ohne Modell; abweichende Felder und Standardwerte
  build-deployment/index.md    build.bat, Dockerfile, Startoptionen, Compose-Variablen, Registrierungs-Einstellungen, Proxy, Installation, Registrierungsdaten, Tests, Debugging
```

Nicht vorhandene Inhalte nicht erfinden: Ist im Code etwas nicht dokumentiert oder unklar, kurz so kennzeichnen („im Code nicht dokumentiert").

## Inhaltliche Regeln

- **Vergleich mit Java ist der Kern der Doku.** Für jeden Endpunkt im Code nachlesen, was die Python-Funktion tatsächlich liefert, und mit
  der Java-Endpunkt-Seite vergleichen. Abweichungen ausdrücklich nennen, insbesondere:
  - Fehlerverhalten (Python liefert bei unbekanntem Plugin-Typ HTTP 200 mit leerem Ergebnis statt 404),
  - feste Antworten statt Plugin-Aufruf (z.B. `maxima`, `generatedatasets`, `renderlatex`, fest eingetragene Werte wie der PIG-Tag in `imagetemplates`),
  - nicht implementierte Teile (z.B. `confighttp`/`CONFIGMODE_URL`),
  - zusätzliche Pfade (z.B. die interne API auch unter `<servicepath>/open`, `<servicepath>/ping`).
- **DTOs:** Feldnamen, Aliase (`Field(alias=...)`) und Standardwerte mit den Java-DTO-Seiten vergleichen; das Script `check.py` liefert den Feldvergleich.
  Enums werden in Python als String übertragen – auf die Java-Enum-Seiten verlinken.
- **Bewertung des Uhr-Plugins** (bzw. des jeweiligen Demo-Plugins) als Tabelle Python vs. Java.
- Links auf die Java-Doku relativ: von einer Unterseite `../../referenz-plugin-java/rest-schnittstelle/<Controller>/<methode>/index.md`
  bzw. `../../referenz-plugin-java/dtos/<Dto>/index.md`; die Zuordnung Python-Pfad → Java-Seite steht in `app/main.py` in `DOC_API_ENDPOINTS` und `DOC_INFO_ENDPOINTS`.
- Den Servicepfad als `<servicepath>` schreiben (Standard `/plugindemopython`), in Backticks.

## Format-Konventionen

- Sprache: Deutsch, Stil wie die bestehenden Seiten in `docs/wiki/` (knappe Aufzählungen, Tabellen).
- **Kein YAML-Front-Matter.** Jede Seite beginnt mit einer `# Überschrift` (daraus erzeugt GitHub Pages den Titel).
- Direkt unter der Überschrift steht als HTML-Kommentar der Quellstand:
  `<!-- erstellt aus plugin-demo-python @ <commit-hash> (revision <inhalt von revision.txt>) – bei Änderungen im Plugin-Repo nachziehen -->`
- Links relativ mit `../xyz/index.md`; jede Unterseite endet mit einem Link zurück auf `../index.md`, die Startseite mit einem Link auf `../index.md` (Plugins).
- `<…>` außerhalb von Backticks als `&lt;…&gt;` schreiben, sonst wird es als HTML-Tag verschluckt.
- Jekyll verarbeitet die Seiten mit Liquid: `{{…}}` und `{%…%}` als `{% raw %}{{…}}{% endraw %}` schreiben.
- Code-Beispiele als ```python, ```bash bzw. ```text-Blöcke, kurz halten. Mermaid wird nicht gerendert.
- Bilder in den jeweiligen Seitenordner legen und relativ einbinden.
- **Suchindex `docs/search.json` muss gültiges JSON bleiben** – Template mit `| escape | jsonify` nicht ändern (Details in `CLAUDE.md`
  und im Skill `plugin-doku`). Backslashes in Pfaden (z.B. aus `build.bat`) sind damit unkritisch.

## Ablauf

1. **Quellstand ermitteln:** `git -C ../plugin-demo-python rev-parse --short HEAD` und `revision.txt` lesen.
   Auf uncommittete Änderungen im Plugin-Repo hinweisen (`git -C ../plugin-demo-python status -s`).
2. **Neu oder inkrementell?**
   - Existiert der Zielordner noch nicht oder verlangt der Benutzer „komplett neu": alle Seiten neu schreiben.
   - Sonst den Hash aus dem Kommentar in `index.md` lesen, mit `git -C ../plugin-demo-python diff --stat <alter-hash>..HEAD` und
     `git -C ../plugin-demo-python diff <alter-hash>..HEAD -- app/main.py` die Änderungen ermitteln und nur die betroffenen Seiten anpassen:
     - `CONF_*`, `PluginDemo` → plugin-api (und ggf. eigenes-plugin),
     - Endpunkt-Funktionen, Router, Pfade → rest-schnittstelle und architektur,
     - Pydantic-Modelle → dtos,
     - Registrierung, Umgebungsvariablen, `Dockerfile`, `yml/`, `proxy/`, `scripts/`, `build.bat`, `tests/` → build-deployment (und ggf. architektur),
     - Versionen in `requirements.txt`/`Dockerfile` → index.
     Überall den Kommentar auf den neuen Hash setzen.
3. **Quellen lesen** (siehe Tabelle) und die Seiten schreiben.
4. **Verlinkung** (nur diese Änderungen außerhalb des Zielordners):
   - `docs/wiki/Plugins/index.md`, Abschnitt „Plugin-Entwicklung": Punkt zum Referenz-Plugin (Python) mit Links auf
     `../Plugins/referenz-plugin-python/index.md`, `eigenes-plugin` und `rest-schnittstelle`; fehlende Links ergänzen, andere Inhalte nicht ohne Rückfrage löschen.
   - `docs/wiki/index.md`: Eintrag „Referenz-Plugin (Python)" im Abschnitt „Alle Seiten (A–Z)" direkt nach „Referenz-Plugin (Java)", falls noch nicht vorhanden.
   - `docs/wiki/Plugins/referenz-plugin-java/index.md`, Abschnitt „Links": Verweis auf die Python-Portierung, falls noch nicht vorhanden.
5. **Prüfen:**
   ```bash
   python -I .claude/skills/plugin-doku-python/scripts/check.py ../plugin-demo-python
   ```
   Das Script prüft, dass jeder Endpunkt aus `app/main.py` auf der REST-Seite, jedes Pydantic-Modell auf der DTO-Seite und jede
   `CONF_*`-Konstante auf der Plugin-API-Seite vorkommt; es vergleicht die Felder der Modelle mit den Java-DTO-Seiten (Abweichungen müssen
   auf der DTO-Seite stehen) und prüft Links, Bilder, Maskierung von `<…>`/`{{…}}` und den Quell-Kommentar. Bei Fehlern die Seiten ergänzen
   und erneut prüfen. Die „Hinweise" der Ausgabe (z.B. Feldabweichungen) mit der DTO-Seite abgleichen.
   Ändert sich die Code-Struktur so, dass das Script Endpunkte oder Modelle nicht mehr erkennt, das Script anpassen.
6. **Zusammenfassung** für den Benutzer: Quellstand, neue/geänderte Seiten, gefundene Abweichungen zu Java, Auffälligkeiten im Code.
   Nicht committen und nicht pushen, außer der Benutzer verlangt es.
7. **Nach dem Push** (nur wenn gepusht wurde): Pages-Build abwarten und den Suchindex prüfen –
   `python -I .claude/skills/plugin-doku/scripts/checksearch.py` – sowie die neuen Seiten per HTTP-Status (200).
