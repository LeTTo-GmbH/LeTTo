# LeTTo – Hinweise für Claude Code

Die Dokumentation unter `docs/` wird über GitHub Pages (Jekyll) als https://doc.letto.at veröffentlicht. Jeder Push auf `master` löst den Workflow „pages build and deployment" aus.

## Regeln für Seiten in `docs/`

- Jede Seite ist ein eigener Ordner mit `index.md`; Links relativ als `../xyz/index.md`.
- Kein YAML-Front-Matter in Wiki-Seiten; der Seitentitel kommt aus der ersten `# Überschrift`.
- Jekyll verarbeitet alle Seiten mit Liquid: `{{…}}` und `{%…%}` im Text – auch in Backticks und Code-Blöcken – als
  `{% raw %}{{servicepath}}{% endraw %}` schreiben, sonst erscheinen sie auf der Seite leer.
- `<…>` außerhalb von Backticks (z.B. `<endpoint>` in Überschriften, Tabellen, Linktexten) als `&lt;…&gt;` schreiben, sonst wird es als HTML-Tag verschluckt.
- Mermaid wird vom Layout `docs/_layouts/default.html` nicht gerendert; Diagramme als ```text-Block.
- HTML-Links (`<a href="…">`) wandelt Jekyll nicht um: dort auf den Ordner zeigen (`xyz/`), nicht auf `index.md`.

## Baum des Wikis `docs/wiki`

Direkt unter `docs/wiki` liegen nur die Bereiche, jede Seite gehört in einen Bereich (keine neuen Ordner direkt unter `wiki/`):

| Bereich | Inhalt |
|---|---|
| `Hauptseite` | Startseite (vom Layout, der Download-Seite und der F1-Hilfe verlinkt) |
| `Einstieg` | Einführung, Hauptansicht, Hilfesystem, Shortcuts, FAQ, Neuigkeiten |
| `Schueler` | Sicht der Schüler: Dashboard, Aktivitäten, gesicherter Modus, Eingabe von Ergebnissen |
| `Fragen` (+ `Dialoge`) | Beispielsammlung, Editor, Fragetypen, Export; Dialoge der Beispielsammlung |
| `Berechnungen` (+ `Funktionen`, `func`) | Berechnungen, Datensätze, Einheiten; Funktionsreferenz |
| `Plugins` | alle Plugin-Seiten und die Referenz-Plugins – wird aus den Plugins verlinkt, nicht verschieben |
| `Tests` (+ `Labor`) | Online-Tests/Aktivitäten, Klassenzimmer, Schuljahr; Labor |
| `Beurteilungen` (+ `Kompetenzen`) | Katalog, Beurteilungen; Kompetenzen und Lehrpläne |
| `Konfiguration` | Profil, Klassenzuordnung, Benutzer, Passwörter |
| `admin` (+ `global`) | Schul-Administration; globaler Administrator |
| `Administration` (+ `Docker`, `Archiv`) | Server: Installation, Setup-Service, Zertifikat, Sicherung, Update; Docker/Images; Glassfish/TomEE |
| `Wiki-Pflege` | Bearbeiten des Wikis |

- Das Layout zeigt auf jeder Wiki-Seite oben den Pfad und unten die direkten Unterseiten, die die Seite nicht selbst verlinkt
  (aus `page.url` und `site.pages`). Dafür muss in den Seiten nichts gepflegt werden – eine neue Seite im richtigen Ordner
  ist automatisch erreichbar.
- `docs/wiki/index.md` enthält oben die Bereiche und darunter „Alle Seiten (A–Z)“ – neue wichtige Seiten dort alphabetisch eintragen.
- Seiten der alten Oberfläche (LeTTo-Server) tragen oben den Hinweis „**Alte Oberfläche:** …“ mit Link auf die neue Seite;
  heißt die neue Seite gleich, hat die alte Seite die Endung `-alt` (zB. `Konfiguration/Benutzer-alt`).
- **Wird eine Seite verschoben oder umbenannt**, die alte Adresse in die Tabelle `weiterleitung` in `docs/404.html`
  eintragen (alte Adresse ohne `/` am Ende → neue Adresse). Die Doku wird aus Programmen direkt verlinkt
  (F1-Hilfe `help_*.properties` in letto-main, App, Plugins, Installations-Skripte), alte Links müssen weiter funktionieren.

## Suchindex `docs/search.json` muss immer gültiges JSON sein

Die Suche in der Titelleiste lädt `search.json`. Ist die Datei kein gültiges JSON, liefert die Suche für **die gesamte Doku** keine Treffer mehr.

- Das Template maskiert Titel und Inhalt mit `| escape | jsonify` (ohne umschließende Anführungszeichen). Diese Form nicht ändern,
  insbesondere nicht zurück zu `"{{ … | escape }}"` und nicht auf `replace`-Filter umstellen – ein `replace: '\', '\\'` wirkt auf GitHub Pages nicht.
  Damit sind Backslashes (Windows-Pfade), Anführungszeichen und Tabs im Seitentext unkritisch.
- Nach jedem Push mit Doku-Änderungen: warten, bis der Pages-Build für den Commit fertig ist
  (`https://api.github.com/repos/LeTTo-GmbH/LeTTo/actions/runs?per_page=1`), dann den Live-Index prüfen:
  ```bash
  python -I .claude/skills/plugin-doku/scripts/checksearch.py
  ```
  Bei einem Fehler sofort beheben und Bescheid geben.

## Skills

- `/plugin-doku` erzeugt die Doku des Java-Referenz-Plugins (`../plugin-demo-java`) unter `docs/wiki/Plugins/referenz-plugin-java/`.
  Details in `.claude/skills/plugin-doku/SKILL.md`.
- `/plugin-doku-python` erzeugt die Doku des Python-Referenz-Plugins (`../plugin-demo-python`) unter `docs/wiki/Plugins/referenz-plugin-python/`;
  sie verlinkt für Endpunkte und DTOs auf die Java-Doku. Details in `.claude/skills/plugin-doku-python/SKILL.md`.
