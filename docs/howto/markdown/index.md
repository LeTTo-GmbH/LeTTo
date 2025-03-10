# Doc zu Markdown
* [https://github.github.com/gfm/](https://github.github.com/gfm/)

# Sonderzeichen

Verblocken mit Backslash als Markdown führt zu Fehlern in der Indexierung der Suche! `&#92`

| Name               | Zeichen | Entity     | Markdown    | 
|--------------------|---------|------------|-------------|
| Backslash          | &#92;   | &amp;#92;  | &#92;&#92;  |
| eckige Klammer auf | &#91;   | &amp;#91;` | &#92;&#91;  |
| eckige Klammer zu  | &#93;   | &amp;#93;  | &#92;&#93;  |
| senkrechter Strich | &#124;  | &amp;#124; | &#92;&#124; |
| Doppelhochkomma    | &quot;  | &amp;quot; | &#92;&quot; |
| Einfachhochkomma   | &#39;   | &amp;#39;  | &#92;&#39;  |
| Kleiner            | &lt;    | &amp;lt;   | &#92;&lt;   |
| Größer             | &gt;    | &amp;gt;   | &#92;       |

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
## Indexierungs-Fehler
Index in Datei: https://doc.letto.at/search.json
* Im Browser öffnen - Fehlermeldungen lesen
* Datei downloaden und in Geany öffnen - Fehler suchen
* korrigieren im Markdown-Sourcecode

## Zu wenige Suchtreffer
* Wenn nur 10 Treffer gefunden werden die Einträge von limit in der Datei docs/assets/js/simple-jekyll-search.min.js von 10 auf 100 erhöhen
* obige Korrektur immer anwenden wenn jekyll-search auf eine neue Version gesetzt wird.

