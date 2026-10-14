# Plugin-API (BasePlugin)
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* `PluginService` (`at.letto.plugins.plugin`) ist das Interface, das jedes Plugin erfüllt. Die DTOs sind von LeTTo unabhängig.
* `BasePlugin` ist die abstrakte Basisklasse mit Standardimplementierungen. Ein eigenes Plugin erbt davon,
  setzt im Konstruktor seine Eigenschaften und überschreibt die benötigten Methoden.
* Jede REST-Anfrage erzeugt eine neue Instanz mit `new Plugin(name, config)`; danach wird `setImageService(...)` aufgerufen.
* Getter für alle Eigenschaften erzeugt Lombok (`@Getter`).

## Eigenschaften (im Konstruktor setzen)

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `name` | String | Konstruktor | Name des Plugins in der Frage |
| `config` | String | Konstruktor | Konfigurationsstring |
| `typ` | String | – | Typ des Plugins |
| `version` | String | `"1.0"` | Version; ändert sich die Version, ändert sich auch die Prüfsumme jedes Plugin-Bildes |
| `wikiHelp` | String | `"Plugins"` | Name der Wiki-Seite, wenn eine Doku am LeTTo-Wiki vorliegt |
| `helpUrl` | String | `""` | Hilfe-URL für die Beschreibung des Plugins |
| `helpfiles` | String[] | `{"plugins/plugin.html"}` | Hilfedateien (HTML) für den Plugin-Dialog |
| `javascriptLibs` | String[] | `{"plugins/plugintools.js"}` | JavaScript-Libraries des Plugins (Ressourcenpfade) |
| `javaScript` | boolean | `false` | Plugin hat eine JavaScript-Schnittstelle bei der Beispieldarstellung |
| `initPluginJS` | String | `""` | Name der JS-Methode zur Initialisierung für die interaktive Ergebniseingabe |
| `configPluginJS` | String | `"configPlugin"` | Name der JS-Methode zur Konfiguration |
| `configurationMode` | int | `CONFIGMODE_JSF` | Konfigurations-Modus, siehe [Architektur](../architektur/index.md#konfigurationsdialog) |
| `defaultPluginConfig` | boolean | `false` | Standard-Plugin-Konfiguration verwenden |
| `width`, `height` | int | 400, 400 | Größe des zu erzeugenden Bildes in Pixel (max. `MAX_IMAGE_SIZE` = 2000) |
| `imageWidthProzent` | int | 100 | Bildbreite in Prozent der Seitenbreite |
| `math` | boolean | `false` | Plugin kann CalcErgebnis und VarHash als JSON verarbeiten |
| `cacheable` | boolean | `true` | Plugin ist stateless und liefert bei gleicher Angabe immer das gleiche Verhalten |
| `useQuestion` | boolean | `true` | Plugin benötigt die Frage |
| `useVars` | boolean | `true` | Datensatz-Variablen ohne Konstante benötigt |
| `useCVars` | boolean | `true` | Datensatz-Variablen mit Konstanten benötigt |
| `useMaximaVars` | boolean | `true` | Maxima-Durchrechnungen ohne eingesetzte Datensätze benötigt |
| `useMVars` | boolean | `true` | Maxima-Durchrechnungen mit eingesetzten Datensätzen benötigt |
| `addDataSet` | boolean | `true` | Button „AddDataset" im umgebenden Konfigurationsdialog |
| `calcMaxima` | boolean | `true` | Button „Maxima" im umgebenden Konfigurationsdialog |
| `externUrl` | boolean | `false` | Plugin ist über den Browser direkt erreichbar |
| `pluginServiceURL` | String | `""` | URL des Plugin-Services für die direkte Kommunikation |

## Methoden

### Muss implementiert werden

| Methode | Zweck |
|---|---|
| `void paint(Graphics2D g, PluginImageResultDto r)` | Zeichnet das Plugin-Bild (Größe `width` × `height`). Fehlermeldungen in `r` eintragen (`ok=false`, `messages`). |
| `void parseDrawParams(String params, PluginQuestionDto q, PluginImageResultDto r)` | Wertet die Parameter des PIG-Tags vor dem Zeichnen aus (z.B. Bildgröße). |
| `PluginScoreInfoDto score(PluginDto, String antwort, ToleranzDto, VarHashDto, PluginAnswerDto, double grade)` | Bewertet die Schülereingabe (REST: `/open/score`). |

`BasePlugin` implementiert `parseDrawParams` und `score` nicht, daher sind sie in jedem Plugin zu implementieren.

### Überschreibbare Methoden mit Standardverhalten

| Methode | REST-Endpunkt | Standard in `BasePlugin` | Zweck |
|---|---|---|---|
| `String getHTML(String params, PluginQuestionDto q)` | `/open/gethtml` | `""` | Fragetext für einen PIT-Tag |
| `String getAngabe(String params)` | `/open/angabe` | `null` | Angabetext für das Textfeld der Frage |
| `List<PluginDatasetDto> generateDatasets()` | `/open/generatedatasets` | leere Liste | Datensätze, die in der Frage vorhanden sein sollten |
| `Vector<String> getVars()` | `/open/getvars` | `null` | Variablen, die als Dataset benötigt werden |
| `String getMaxima(String params, PluginQuestionDto q, PluginMaximaCalcModeDto mode)` | `/open/maxima` | `""` | Maxima-Berechnungsstring |
| `ImageBase64Dto getImageDto(String params, PluginQuestionDto q)` | `/open/image` | erzeugt Bild über `parseDrawParams` + `paint`, PNG Base64 | Bild als Base64 |
| `ImageUrlDto getImageUrl(String params, PluginQuestionDto q)` | – (intern, z.B. im `PluginDto`-Konstruktor) | speichert Bild im Image-Service, liefert URL | Bild als öffentliche URL |
| `String getPluginImageDescription(String imageParams, PluginQuestionDto q)` | – | aus Typ, Version, Name, Config, Parametern und Frage | eindeutige Beschreibung, daraus wird der Dateiname des Bildes gebildet |
| `Vector<String[]> getImageTemplates()` | `/open/imagetemplates` | `null` | Bildvarianten: [0] Beschreibung, [1] PIG-Tag, [2] Hilfetext |
| `CalcErgebnisDto parserPlugin(VarHashDto vars, CalcParamsDto cp, CalcErgebnisDto... p)` | `/open/parserplugin` | `null` | Funktion `plugin("name",p1,p2,…)` im Lösungsfeld |
| `String parserPluginEinheit(String... p)` | `/open/parserplugineinheit` | `null` | Recheneinheit des Ergebnisses von `parserPlugin` |
| `String modifyAngabe(String text, PluginQuestionDto q)` | `/open/modifyangabe` | `text` | verändert Text in PI-Tags vor dem Darstellen |
| `String modifyAngabeTextkomplett(String text, PluginQuestionDto q)` | `/open/modifyangabetextkomplett` | `text` | verändert den gesamten Angabetext |
| `String updatePluginstringJavascript(String pluginDef, String jsResult)` | `/open/updatepluginstringjavascript` | `pluginDef` | passt die Plugindefinition an das JavaScript-Ergebnis an (z.B. interaktive Karte) |
| `PluginDto loadPluginDto(String params, PluginQuestionDto q, int nr)` | `/open/loadplugindto` | `null` | `PluginDto` für das JavaScript des Plugins |
| `PluginRenderDto renderLatex(PluginDto, String answer, String mode)` | `/open/renderlatex` | leeres `PluginRenderDto` | LaTeX-Quelltext für den Fragedruck |
| `PluginRenderDto renderPluginResult(boolean tex, PluginDto, String antwort, ToleranzDto, VarHashDto, PluginAnswerDto, double grade)` | `/open/renderpluginresult` | leeres `PluginRenderDto` | HTML oder LaTeX mit Schülereingabe und Lösung |
| `InputElement getInputElement()` | – (in `PluginGeneralInfo`) | `JAVASCRIPT` wenn `javaScript`, sonst `TextArea` | Eingabeelement der Subquestion |
| `String getHelp()` | – (in `PluginGeneralInfo`) | Inhalt aller `helpfiles` | HTML-Hilfe |
| `List<JavascriptLibrary> javascriptLibraries()` | – (in `PluginGeneralInfo`) | leer | externe JS-Libraries mit vollständiger URL |
| `List<JavascriptLibrary> javascriptLibrariesLocal()` | – (in `PluginGeneralInfo`) | Quelltext aller `javascriptLibs` | lokale JS-Libraries |
| `PluginGeneralInfo getPluginGeneralInfo()` | `/open/generalinfo` | aus den Eigenschaften | allgemeine Informationen |
| `PluginConfigurationInfoDto configurationInfo(String configurationID)` | `/open/configurationinfo` | aus den Eigenschaften | Informationen zum Start des Konfigurationsdialogs |
| `PluginConfigDto setConfigurationData(String configuration, PluginQuestionDto q)` | `/open/setconfigurationdata` | setzt `config`, leeres `PluginConfigDto` | Daten für das Konfigurations-JavaScript |
| `String getConfiguration()` | `/open/getconfiguration` | `config` | aktuelle Konfiguration (oder `"@ERROR: Meldung"`) |

### Hilfsmethoden in BasePlugin

| Methode | Zweck |
|---|---|
| `BufferedImage getAWTImage(String params, PluginQuestionDto q, PluginImageResultDto r)` | erzeugt das Bild über `paint`, bei Fehlern ein Fehlerbild |
| `void paintFehler(Graphics g, String msg)` | gibt eine Fehlermeldung im Bild aus |
| `String loadHelpFile(String resource)` | lädt eine Hilfedatei und ersetzt Umlaute durch HTML-Entitäten |
| `String getHelpMessageFromResource(String name)` | lädt den `<body>`-Inhalt einer HTML-Ressource, ersetzt `{{servicepath}}` |
| `static Iterable<MatchResult> findMatches(String pattern, CharSequence s)` | alle Regex-Treffer |
| `String getTag()` | Plugin-Definition `[PI name typ "config"]` |

## Beispiel: Uhr-Plugin

Dateien:

| Datei | Beschreibung |
|---|---|
| `src/main/java/at/letto/plugins/plugin/uhr/PluginUhr.java` | Plugin-Klasse |
| `src/main/resources/plugins/uhr/uhr1Script.js` | interaktive Eingabe (`initPluginUhr1`) |
| `src/main/resources/plugins/uhr/uhr1ConfigScript.js` | Konfigurationsdialog (`configPluginUhr1`) |
| `src/main/resources/plugins/uhr/Uhr1.html` | Hilfetext |

### Konstruktor

```java
public PluginUhr(String name, String params) {
    super(name, params);
    version           = "1.0";
    helpfiles         = new String[]{"plugins/uhr/Uhr1.html"};
    javascriptLibs    = new String[]{"plugins/uhr/uhr1Script.js","plugins/uhr/uhr1ConfigScript.js"};
    javaScript        = true;
    initPluginJS      = "initPluginUhr1";
    configPluginJS    = "configPluginUhr1";
    configurationMode = PluginConfigurationInfoDto.CONFIGMODE_JAVASCRIPT;
    width  = 500;
    height = 500;
    externUrl = true;
    // ... danach Auswertung von params (durch ";" getrennt)
}
```

Konfigurationsparameter (durch `;` getrennt):

| Parameter | Bedeutung |
|---|---|
| `mode=js` / `mode=iframe` / `mode=string` / `mode=jsf` | Konfigurations-Modus `CONFIGMODE_JAVASCRIPT` (Standard) / `CONFIGMODE_URL` / `CONFIGMODE_STRING` / `CONFIGMODE_JSF` |
| `bgcolor=<farbe>` | Hintergrundfarbe: `red`, `green`, `blue`, `gray`, `yellow`; Standard weiß. Ungültige Werte landen in `configMessage` |
| `w<Prozent>` | Bildbreite in Prozent (1–100) |

Bildparameter im PIG-Tag (durch `,` getrennt, ausgewertet in `parseDrawParams`):

| Parameter | Bedeutung |
|---|---|
| `size=<Breite>x<Höhe>` | Bildgröße in Pixel |
| `size=<Größe>` | quadratisches Bild |

### Überschriebene Methoden

| Methode | Umsetzung im Uhr-Plugin |
|---|---|
| `paint` | zeichnet Ziffernblatt mit 12 Stundenmarken und Zahlen in `bgcolor` |
| `parseDrawParams` | wertet `size=` aus |
| `getImageTemplates` | eine Vorlage `[PIG <name> ""]` („Uhrblatt") |
| `score` | Musterlösung `answerText` als Zeit in Anführungszeichen (z.B. `"10:30"`) oder als Zahl (Sekunden); Schülereingabe wird mit `Datum.parseTime` in Sekunden umgerechnet und mit `PluginToolsMath.equals` unter Berücksichtigung der Toleranz verglichen → `Score.OK` mit vollen Punkten, sonst `Score.FALSCH` |
| `loadPluginDto` | `new PluginDto(params, this, q, nr)` – Bild, Größe und Tag-Name |
| `configurationInfo` | setzt `configurationMode`, `javaScriptMethode = configPluginJS` und `configurationID` |
| `setConfigurationData` | übergibt Testparameter (`TEST`, `help`, `vars`) in `PluginConfigDto.params` |
| `getVars`, `parserPlugin`, `parserPluginEinheit` | liefern `null` (nicht verwendet) |

Hinweis: Das Feld `handcolor` ist vorgesehen, wird derzeit aber nicht ausgewertet.

[Referenz-Plugin (Java)](../index.md)
