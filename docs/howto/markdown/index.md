# Doc zu Markdown
* https://github.github.com/gfm/

# Sonderzeichen

Verblocken mit Backslash als Markdown führt zu Fehlern in der Indexierung der Suche!

| Name               | Zeichen | Entity   | Markdown | Als Zeichen |
|--------------------|---------|----------|----------|-------------|
| Backslash          | &#92;   | `&#92;`  | `\\`     | `\`         |
| eckige Klammer auf | &#91;   | `&#91;`  | `\[`     | `[`         |
| eckige Klammer zu  | &#93;   | `&#93;`  | `\]`     |             |
| senkrechter Strich | &#124;  | `&#124;` | `\|`     |             |
| Doppelhochkomma    | &quot;  | `&quot;` | `\"`     |             |
| Einfachhochkomma   | &#39;   | `&#39;`  | `\'`     |             |
| Kleiner            | &lt;    | `&lt;`   | `\<`     |             |
| Größer             | &gt;    | `&gt;`   | `\>`     |             |

# Google Custom Search
* Konfiguration: https://programmablesearchengine.google.com/controlpanel/all
* Prüfe die vorhandenen Daten: https://search.google.com/search-console/index?resource_id=sc-domain%3Adoc.letto.at
  https://search.google.com/search-console?resource_id=sc-domain%3Adoc.letto.at

# Kommentare in md-Dateien:
`[//]`: Diese Art von Kommentaren ist nicht kompatibel mit Github-DOC!!!
`<!-- Dies ist ein Kommentar -->` : Funktioniert auch mit Github-DOC!!!

# Probleme beim Such-Index
Index in Datei: https://doc.letto.at/search.json
* Im Browser öffnen - Fehlermeldungen lesen
* Datei downloaden und in Geany öffnen - Fehler suchen
* korrigieren im Markdown-Sourcecode