# LeTTo – Hinweise für Claude Code

Die Dokumentation unter `docs/` wird über GitHub Pages (Jekyll) als https://doc.letto.at veröffentlicht. Jeder Push auf `master` löst den Workflow „pages build and deployment" aus.

## Regeln für Seiten in `docs/`

- Jede Seite ist ein eigener Ordner mit `index.md`; Links relativ als `../xyz/index.md`.
- Kein YAML-Front-Matter in Wiki-Seiten; der Seitentitel kommt aus der ersten `# Überschrift`.
- Jekyll verarbeitet alle Seiten mit Liquid: `{{…}}` und `{%…%}` im Text – auch in Backticks und Code-Blöcken – als
  `{% raw %}{{servicepath}}{% endraw %}` schreiben, sonst erscheinen sie auf der Seite leer.
- `<…>` außerhalb von Backticks (z.B. `<endpoint>` in Überschriften, Tabellen, Linktexten) als `&lt;…&gt;` schreiben, sonst wird es als HTML-Tag verschluckt.
- Mermaid wird vom Layout `docs/_layouts/default.html` nicht gerendert; Diagramme als ```text-Block.

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
