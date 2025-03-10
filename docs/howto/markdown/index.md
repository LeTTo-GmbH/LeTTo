# Doc zu Markdown
* [https://github.github.com/gfm/](https://github.github.com/gfm/)

# Sonderzeichen

Verblocken mit Backslash als Markdown führt zu Fehlern in der Indexierung der Suche!

| Name               | Zeichen | Entity   | Markdown | Als Zeichen |
|--------------------|---------|----------|----------|-------------|
| Backslash          | &#92;   | `&#92;`  | `\\`     |           |
| eckige Klammer auf | &#91;   | `&#91;`  | `\[`     |           |
| eckige Klammer zu  | &#93;   | `&#93;`  | `\]`     |           |
| senkrechter Strich | &#124;  | `&#124;` | `\|`     |           |
| Doppelhochkomma    | &quot;  | `&quot;` | `\"`     |           |
| Einfachhochkomma   | &#39;   | `&#39;`  | `\'`     |           |
| Kleiner            | &lt;    | `&lt;`   | `\<`     |           |
| Größer             | &gt;    | `&gt;`   | `\>`     |           |


# Google Custom Search
* Konfiguration: [https://programmablesearchengine.google.com/controlpanel/all](https://programmablesearchengine.google.com/controlpanel/all)
* Prüfe die vorhandenen Daten: https://search.google.com/search-console/index?resource_id=sc-domain%3Adoc.letto.at
  https://search.google.com/search-console?resource_id=sc-domain%3Adoc.letto.at

# Kommentare in md-Dateien:
* als Markdown-Kommentar [](Das ist ein Kommentar) :
  <pre>&#91;&#93;(Das ist ein Kommentar)</pre>

* Als HTML-<!-- Das ist ein Kommentar -->Kommentar:
  <pre>&lt;!-- Dies ist ein Kommentar --&gt;</pre>

# Probleme beim Such-Index
Index in Datei: https://doc.letto.at/search.json
* Im Browser öffnen - Fehlermeldungen lesen
* Datei downloaden und in Geany öffnen - Fehler suchen
* korrigieren im Markdown-Sourcecode