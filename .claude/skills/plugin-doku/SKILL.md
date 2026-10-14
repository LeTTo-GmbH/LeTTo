---
name: plugin-doku
description: Erzeugt oder aktualisiert die Doku des Java-Referenz-Plugins (plugin-demo-java) unter docs/wiki/Plugins/referenz-plugin-java aus dem Sourcecode – inklusive eigener, querverlinkter Seiten für jeden Controller, jeden Endpunkt, jedes DTO und jede Enum. Verwenden, wenn die Plugin-Doku neu generiert, aktualisiert oder mit dem Plugin-Code abgeglichen werden soll.
---

# Doku des Referenz-Plugins generieren

Erzeuge bzw. aktualisiere die Dokumentation des Java-Referenz-Plugins für die GitHub-Pages-Doku von LeTTo.

## Quelle und Ziel

- **Quelle:** `../plugin-demo-java` (Repo https://github.com/LeTTo-GmbH/plugin-demo-java), relativ zum LeTTo-Repo-Root.
  Falls das Verzeichnis nicht erreichbar ist: abbrechen und den Benutzer bitten, Claude im LeTTo-Repo mit
  `--add-dir ../plugin-demo-java` zu starten bzw. beide Repos nebeneinander auszuchecken.
- **Ziel:** `docs/wiki/Plugins/referenz-plugin-java/` – Dateien außerhalb dieses Ordners nur wie unter „Verlinkung" beschrieben ändern.

Relevante Quellen im Plugin-Repo:

| Quelle | Inhalt für die Doku |
|---|---|
| `README.md`, `HELP.md` | Anleitung „Neues Plugin erstellen", Build, Debugging |
| `src/main/java/at/letto/plugins/controller/*` | REST-Endpunkte (Pfad, Methode, Request-/Response-DTO, JavaDoc, Swagger-Annotationen, Fehlerfälle) |
| `src/main/java/at/letto/plugins/config/Endpoint.java` | Pfad-Konstanten (vollständige Pfade daraus zusammensetzen) |
| `src/main/java/at/letto/plugins/dto/*`, `enums/*` | DTOs und Enums der Schnittstelle |
| `src/main/java/at/letto/plugins/plugin/BasePlugin.java`, `PluginService.java` | Plugin-API: welche Methoden ein Plugin überschreibt, welche Plugin-Methode ein Endpunkt aufruft |
| `src/main/java/at/letto/plugins/plugin/uhr/PluginUhr.java`, `src/main/resources/plugins/uhr/*` | Beispiel-Plugin (Uhr) |
| `src/main/java/at/letto/plugins/config/*` | Konfiguration, Registrierung am LeTTo-Server (ausgehender Aufruf an das Setup-Service) |
| `build/`, `Dockerfile`, `yml/`, `proxy/` | Build, Docker-Deployment, Proxy |
| `src/main/resources/help/index.html` | Hilfeseite des Services |

## Seitenstruktur

Jede Seite ist ein eigener Ordner mit `index.md` (Konvention der LeTTo-Doku):

```
docs/wiki/Plugins/referenz-plugin-java/
  index.md                     Überblick, Zweck, Links zu GitHub/Swagger/JavaDoc, Inhaltsverzeichnis
  architektur/index.md         Aufbau des Services, Paketstruktur, Ablauf LeTTo-Server <-> Plugin (Textdiagramm, siehe Format-Konventionen)
  eigenes-plugin/index.md      Schritt-für-Schritt: neues Plugin aus dem Demoprojekt erstellen (setpluginname, BasePlugin, StartupConfiguration, Ressourcen)
  plugin-api/index.md          BasePlugin: überschreibbare Methoden mit Zweck, Parametern, Rückgabe; am Uhr-Plugin erklärt
  build-deployment/index.md    Build (build.bat/build.sh), Docker, Proxy-Konfiguration, Registrierung am Server, Debugging

  rest-schnittstelle/index.md                     Übersicht: alle Controller mit Basispfad, Erreichbarkeit, Anzahl Endpunkte;
                                                  darunter eine Gesamttabelle aller Endpunkte (je Zeile Link auf die Endpunkt-Seite)
  rest-schnittstelle/<Controller>/index.md        eine Seite je Controller (Ordnername = Klassenname, z.B. ApiController)
  rest-schnittstelle/<Controller>/<methode>/index.md
                                                  eine Seite je Endpunkt (Ordnername = Java-Methodenname im Controller, z.B. score)

  dtos/index.md                                   Übersicht aller DTOs, gruppiert (Requests, Frage/Variablen, Darstellung, Bewertung,
                                                  Konfiguration, Service/Registrierung, intern); je Zeile Link und Kurzbeschreibung
  dtos/<DtoName>/index.md                         eine Seite je Klasse in dto/ (Ordnername = Klassenname, z.B. PluginScoreRequestDto)
  enums/index.md                                  Übersicht aller Enums mit Werten in Kurzform
  enums/<EnumName>/index.md                       eine Seite je Enum (Ordnername = Enum-Name, z.B. TOLERANZMODE)
```

- Ordnernamen exakt wie der Java-Name schreiben (Groß-/Kleinschreibung beibehalten, GitHub Pages ist case-sensitive).
- Für **jeden** Controller, **jede** Endpunkt-Methode (`@GetMapping`, `@PostMapping`, …), **jede** Klasse in `dto/` und **jede** Enum in `enums/`
  gibt es genau eine Seite. Auch Klassen in `dto/`, die kein REST-DTO sind (z.B. `PluginConfigurationConnection`), bekommen eine Seite
  mit dem Hinweis „interne Klasse, wird nicht über REST übertragen".
- Konstanten einer Klasse (z.B. `CONFIGMODE_*` in `PluginConfigurationInfoDto`) werden auf der Seite dieser Klasse beschrieben, nicht separat.

Nicht vorhandene Inhalte nicht erfinden: Wenn im Code etwas nicht dokumentiert oder unklar ist, kurz so kennzeichnen
(„im Code nicht dokumentiert") statt zu raten.

## Inhalt der Detailseiten

### Controller-Seite `rest-schnittstelle/<Controller>/index.md`

- Überschrift `# <Controller>`, Zweck (aus JavaDoc und `@Tag`-Beschreibung), Basispfad (`@RequestMapping`), Erreichbarkeit
  (nur Docker-Netzwerk / extern über Proxy) und Link auf die JavaDoc des Controllers (`/<endpoint>/open/javadoc/...`).
- Tabelle aller Endpunkte: Methode | Pfad | Request (Link) | Response (Link) | Kurzbeschreibung – Pfad bzw. Methodenname verlinkt auf die Endpunkt-Seite.
- Hinweise, die für alle Endpunkte gelten (z.B. 404 bei unbekanntem Plugin-Typ, Delegation an einen anderen Controller).

### Endpunkt-Seite `rest-schnittstelle/<Controller>/<methode>/index.md`

- Überschrift `# <HTTP-Methode> <vollständiger Pfad>` (z.B. `# POST /open/score`).
- Steckbrief-Tabelle: Controller (Link), Java-Methode, HTTP-Methode, vollständiger Pfad (bei mehreren Pfaden alle), Erreichbarkeit,
  Content-Type (falls `produces` gesetzt), Request-Body bzw. Parameter (Typ, Link), Response (Typ, Link).
- **Beschreibung:** vollständige JavaDoc bzw. `@Operation`-Beschreibung, sprachlich geglättet, inhaltlich unverändert.
- **Request:** Tabelle der Felder, die der Endpunkt tatsächlich auswertet (aus der JavaDoc `r.xyz` bzw. aus dem Code), mit Link auf das DTO
  und auf DTO-Typen einzelner Felder. Felder des DTOs, die der Endpunkt nicht verwendet, als solche kennzeichnen.
- **Response:** Typ mit Link; was im Feld steht bzw. welche Felder der Controller selbst setzt (z.B. `configurationUrl`).
- **Ablauf im Service:** welche Plugin-Methode aufgerufen wird (Link auf `plugin-api/index.md`), bzw. welche Methode von `PluginConfiguration`.
- **Fehlerfälle:** HTTP-Status und Bedingungen, nur soweit im Code erkennbar.
- **Beispiel (optional):** JSON-Skelett des Requests, ausschließlich aus den Feldern des DTOs mit Platzhalterwerten (`"<typ>"`) – keine erfundenen Werte.
- **Siehe auch:** gleichwertige Endpunkte in anderen Controllern (z.B. `ApiExternOpenController` → `ApiController`),
  fachlich zusammengehörige Endpunkte (z.B. Konfigurationssitzung: `configurationInfo` → `setConfigurationData` → `getConfiguration`).

### DTO-Seite `dtos/<DtoName>/index.md`

- Überschrift `# <DtoName>`, Zweck (Klassen-JavaDoc), Paket, Link auf die JavaDoc.
- Feldtabelle: Feld | Typ | Standardwert (falls im Code gesetzt) | Bedeutung. Typen, die selbst DTOs oder Enums sind, verlinken
  (auch in Generics, z.B. `List<`[PluginDatasetDto](../PluginDatasetDto/index.md)`>`).
- Konstanten (`public static final`) und fachlich relevante Methoden/Konstruktoren (z.B. Konstruktor von `PluginDto`, der das Bild erzeugt) kurz beschreiben.
- **Verwendet in Endpunkten:** Tabelle Endpunkt (Link auf Endpunkt-Seite) | Rolle | Kurzbeschreibung des Endpunkts. Rolle ist eine von:
  - `Request` / `Response` – direkt als Body,
  - `in <Dto>.<feld>` – verschachtelt in einem anderen DTO, das Request oder Response eines Endpunkts ist (rekursiv auflösen, Pfad angeben),
  - `ausgehend` – Body eines Aufrufs des Plugins an einen anderen Service (z.B. Registrierung am Setup-Service; Link auf `build-deployment/index.md`).
  Kommt das DTO in keinem Endpunkt vor, „wird in keinem Endpunkt verwendet" schreiben und angeben, wo es stattdessen benutzt wird (z.B. Plugin-API).
- **Verwendet in DTOs:** Liste der DTOs, die ein Feld dieses Typs haben (Link, Feldname).
- **Verwendet in der Plugin-API:** Methoden von `PluginService`/`BasePlugin` mit diesem Typ als Parameter oder Rückgabe (Link auf `plugin-api/index.md`).

### Enum-Seite `enums/<EnumName>/index.md`

- Überschrift `# <EnumName>`, Zweck, Paket, Link auf die JavaDoc.
- Wertetabelle: Wert | Bedeutung (Reihenfolge wie im Code; Hinweise wie „neue Werte nur hinten anfügen" übernehmen).
- Methoden der Enum (z.B. `parse`, `htmlColor`) kurz beschreiben.
- **Verwendet in DTOs:** DTO (Link) und Feldname.
- **Verwendet in Endpunkten:** wie bei DTOs, Rolle immer als Pfad über das DTO (`in PluginScoreInfoDto.status`).
- **Verwendet in der Plugin-API:** falls zutreffend (z.B. `InputElement` als Rückgabe von `getInputElement()`).

## Querverlinkung

Ziel: Von jeder Erwähnung eines Endpunkts, DTOs oder Enums kommt man mit einem Klick auf dessen Seite.

- **Jede** Erwähnung eines DTO- oder Enum-Namens in Tabellen und Fließtext aller Seiten im Zielordner (auch `architektur`, `plugin-api`,
  `eigenes-plugin`, `build-deployment`) ist ein Link auf dessen Seite – innerhalb einer Seite reicht es, die erste Erwähnung je Abschnitt
  sowie jede Tabellenzelle zu verlinken.
- **Jede** Erwähnung eines Endpunkts (Pfad wie `/open/score` oder Methodenname) ist ein Link auf die Endpunkt-Seite.
- Die Plugin-API-Tabelle verlinkt in der Spalte „REST-Endpunkt" auf die Endpunkt-Seiten.
- Auch DTO- und Enum-Namen **innerhalb** von Code-Spans (z.B. Methodensignaturen in der Plugin-API) werden verlinkt: Der Code-Span wird
  in Code-Stücke und verlinkte Namen aufgeteilt (`` `String getHTML(String params,` [`PluginQuestionDto`](…) `q)` ``).
  Leerzeichen an den Rändern der Stücke stehen außerhalb der Backticks, da Markdown sie im Code-Span entfernt. Das erledigt `linkify.py`.
- Die Querverweise „Verwendet in …" werden **aus dem Code berechnet**, nicht geschätzt: zuerst eine vollständige Zuordnung
  Endpunkt → Request-/Response-Typ aus den Controllern bilden, dann für jeden Typ rekursiv alle Feldtypen (inkl. Generics und Arrays) auflösen
  und daraus die Rückverweise für jedes DTO und jede Enum ableiten. Die Zuordnung ist für alle Seiten dieselbe – Seiten nicht unabhängig voneinander befüllen.
- Relative Links je nach Tiefe der Seite:

| von Seite in | auf DTO | auf Enum | auf Endpunkt |
|---|---|---|---|
| `dtos/<X>/` | `../<Y>/index.md` | `../../enums/<E>/index.md` | `../../rest-schnittstelle/<C>/<m>/index.md` |
| `enums/<X>/` | `../../dtos/<Y>/index.md` | `../<E>/index.md` | `../../rest-schnittstelle/<C>/<m>/index.md` |
| `rest-schnittstelle/<C>/` | `../../dtos/<Y>/index.md` | `../../enums/<E>/index.md` | `<m>/index.md` bzw. `../<C2>/<m>/index.md` |
| `rest-schnittstelle/<C>/<m>/` | `../../../dtos/<Y>/index.md` | `../../../enums/<E>/index.md` | `../../<C2>/<m>/index.md` |
| Seiten der ersten Ebene (`plugin-api/` usw.) | `../dtos/<Y>/index.md` | `../enums/<E>/index.md` | `../rest-schnittstelle/<C>/<m>/index.md` |

- Keine Anker auf Überschriften mit Sonderzeichen (Backticks, Gedankenstriche) setzen – deren IDs sind unzuverlässig; lieber auf die Seite verlinken.

## Format-Konventionen

- Sprache: Deutsch, Stil wie die bestehenden Seiten in `docs/wiki/` (knappe Aufzählungen, Tabellen).
- **Kein YAML-Front-Matter.** Jede Seite beginnt mit einer `# Überschrift` (daraus erzeugt GitHub Pages den Titel).
- Direkt unter der Überschrift steht als HTML-Kommentar der Quellstand:
  `<!-- generiert aus plugin-demo-java @ <commit-hash> (revision <inhalt von revision.txt>) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->`
- Links relativ mit `../xyz/index.md`, wie in den bestehenden Seiten.
- Navigation am Seitenende:
  - Seiten der ersten Ebene: Link zurück zur Übersicht `../index.md`.
  - Controller-, DTO- und Enum-Seiten: Link auf ihre Übersicht (`../index.md`) und auf die Startseite des Referenz-Plugins (`../../index.md`).
  - Endpunkt-Seiten: Link auf den Controller (`../index.md`), auf die REST-Übersicht (`../../index.md`) und die Startseite (`../../../index.md`).
- `<` und `>` in Tabellen (Generics) als `&lt;` / `&gt;` schreiben, außer innerhalb von Backticks. Das gilt auch für `<endpoint>` in Überschriften und Linktexten.
- Jekyll verarbeitet die Seiten mit Liquid: Platzhalter wie `{{servicepath}}` – auch in Backticks und Code-Blöcken – als
  `{% raw %}{{servicepath}}{% endraw %}` schreiben, sonst werden sie auf der Seite leer dargestellt.
- Code-Beispiele als ```java, ```json bzw. ```bash-Blöcke, kurz halten und nur Ausschnitte zitieren, die den Sachverhalt zeigen.
- Diagramme als ```text-Block (ASCII). Mermaid wird vom Layout `docs/_layouts/default.html` nicht gerendert.
- Bilder in den jeweiligen Seitenordner legen und relativ einbinden.

## Ablauf

1. **Quellstand ermitteln:** `git -C ../plugin-demo-java rev-parse --short HEAD` und `revision.txt` lesen.
   Auf uncommittete Änderungen im Plugin-Repo hinweisen (`git -C ../plugin-demo-java status -s`).
2. **Neu oder inkrementell?**
   - Existiert der Zielordner noch nicht oder fehlen die Detailseiten (`dtos/<X>/`, `enums/<X>/`, `rest-schnittstelle/<C>/`):
     alle Seiten neu erzeugen. Alte Inhalte von `dtos/index.md` und `rest-schnittstelle/index.md` werden dabei zu Übersichtsseiten umgebaut.
   - Sonst den Hash aus dem Kommentar in `index.md` lesen und mit
     `git -C ../plugin-demo-java diff --stat <alter-hash>..HEAD` die Änderungen ermitteln.
     Betroffene Seiten aktualisieren – dabei die Abhängigkeiten beachten:
     - geändertes DTO/Enum → dessen Seite, die Seiten aller Endpunkte und DTOs, die es verwenden, und die Übersichten;
     - geänderter Controller/Endpunkt → Endpunkt- und Controller-Seite, REST-Übersicht und die „Verwendet in"-Abschnitte aller
       DTOs/Enums, deren Zuordnung sich ändert (Zuordnung vorher/nachher vergleichen);
     - neue Klassen/Endpunkte → neue Seiten anlegen; entfernte → Ordner löschen und alle Links darauf entfernen.
     Überall den Kommentar auf den neuen Hash setzen.
     Wenn der Benutzer „komplett neu" verlangt, alles neu erzeugen.
3. **Quellen lesen** (siehe Tabelle), die Zuordnung Endpunkt ↔ DTO ↔ Enum aufbauen (siehe Querverlinkung) und die Seiten schreiben:
   - Die Seiten der ersten Ebene (`index.md`, `architektur`, `eigenes-plugin`, `plugin-api`, `build-deployment`) von Hand schreiben bzw. aktualisieren.
   - Die Detail- und Übersichtsseiten (`rest-schnittstelle/**`, `dtos/**`, `enums/**`) mit den Scripten im Ordner `scripts/` dieses Skills erzeugen
     (Pfade relativ zum LeTTo-Repo-Root, Manifest in den Scratchpad legen):
     ```bash
     python -I .claude/skills/plugin-doku/scripts/gen.py ../plugin-demo-java docs/wiki/Plugins/referenz-plugin-java <hash> <revision> <scratchpad>/manifest.json
     python -I .claude/skills/plugin-doku/scripts/linkify.py docs/wiki/Plugins/referenz-plugin-java <scratchpad>/manifest.json
     ```
     - `gen.py` liest Controller, `Endpoint.java`, DTOs, Enums und `PluginService.java`, berechnet die Zuordnung und schreibt alle
       Controller-, Endpunkt-, DTO- und Enum-Seiten samt Übersichten. Es überschreibt nur diese Seiten.
     - `linkify.py` verlinkt danach in **allen** Seiten des Zielordners (auch den handgeschriebenen) Erwähnungen von DTOs, Enums,
       Controllern und Endpunkt-Pfaden und schützt `{{…}}` vor Liquid. Es ist idempotent und kann nach jeder Änderung erneut laufen.
     - Inhalte, die sich nicht aus dem Code ableiten lassen, stehen als Tabellen am Anfang von `gen.py`: `SEE_ALSO` (Siehe auch je Endpunkt),
       `EP_NOTES` (Ablauf-Hinweise je Endpunkt), `C_NOTES`, `DTO_NOTES`, `ENUM_NOTES` und `GROUPS` (Gruppen der DTO-Übersicht).
       Bei Änderungen im Plugin-Code diese Tabellen prüfen und anpassen: neue Endpunkte/DTOs ergänzen, entfernte streichen,
       Hinweise an geändertes Verhalten anpassen. Neue DTOs ohne Gruppe landen automatisch in der Gruppe „Sonstige".
     - Ändert sich die Code-Struktur so, dass das Parsing nicht mehr greift (z.B. neue Annotationen, andere Schreibweise der Pfade),
       die Scripte anpassen statt die Seiten von Hand zu korrigieren – sonst gehen die Korrekturen beim nächsten Lauf verloren.
     - Seiten zu entfernten Klassen oder Endpunkten löscht `gen.py` nicht – verwaiste Ordner vor dem Lauf entfernen (siehe Prüfen).
4. **Verlinkung** (nur diese Änderungen außerhalb des Zielordners):
   - `docs/wiki/Plugins/index.md`, Abschnitt „Plugin-Entwicklung": verweist auf `../Plugins/referenz-plugin-java/index.md` und die Unterseiten.
     Fehlende Links ergänzen; Links auf Seiten, die es nicht mehr gibt, anpassen. Andere Inhalte des Abschnitts nicht ohne Rückfrage löschen.
   - `docs/wiki/index.md`: Eintrag „Referenz-Plugin (Java)" alphabetisch passend einfügen, falls noch nicht vorhanden.
     Die Detailseiten werden dort **nicht** einzeln eingetragen.
5. **Prüfen:**
   - Alle relativen Links im Zielordner zeigen auf existierende Dateien.
   - Vollständigkeit: Für jeden Controller, jede Endpunkt-Methode, jede Klasse in `dto/` und jede Enum in `enums/` existiert der Ordner
     mit `index.md` (Abgleich der Dateilisten bzw. per Grep auf `@*Mapping` in den Controllern).
   - Keine verwaisten Ordner: Jeder Ordner unter `dtos/`, `enums/` und `rest-schnittstelle/` entspricht einer existierenden Klasse bzw. Methode.
   - Jede Detailseite wird von mindestens einer Übersichtsseite verlinkt.
   - Stichprobe der Rückverweise: Für zwei DTOs und eine Enum per Grep in den Controllern und DTOs nachprüfen, dass „Verwendet in" vollständig ist.
   - Falls Ruby/Jekyll lokal verfügbar ist, optional `bundle exec jekyll build` in `docs/` ausführen.
6. **Zusammenfassung** für den Benutzer: Quellstand, Anzahl neuer/geänderter/gelöschter Seiten (je Gruppe), offene Punkte (undokumentierte Stellen).
   Nicht committen, außer der Benutzer verlangt es.
