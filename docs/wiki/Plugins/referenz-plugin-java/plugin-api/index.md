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
| `void paint(Graphics2D g,` [`PluginImageResultDto`](../dtos/PluginImageResultDto/index.md) `r)` | Zeichnet das Plugin-Bild (Größe `width` × `height`). Fehlermeldungen in `r` eintragen (`ok=false`, `messages`). |
| `void parseDrawParams(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q,` [`PluginImageResultDto`](../dtos/PluginImageResultDto/index.md) `r)` | Wertet die Parameter des PIG-Tags vor dem Zeichnen aus (z.B. Bildgröße). |
| [`PluginScoreInfoDto`](../dtos/PluginScoreInfoDto/index.md) `score(`[`PluginDto`](../dtos/PluginDto/index.md)`, String antwort,` [`ToleranzDto`](../dtos/ToleranzDto/index.md)`,` [`VarHashDto`](../dtos/VarHashDto/index.md)`,` [`PluginAnswerDto`](../dtos/PluginAnswerDto/index.md)`, double grade)` | Bewertet die Schülereingabe (REST: [`/open/score`](../rest-schnittstelle/ApiController/score/index.md)). |

`BasePlugin` implementiert `parseDrawParams` und `score` nicht, daher sind sie in jedem Plugin zu implementieren.

### Überschreibbare Methoden mit Standardverhalten

| Methode | REST-Endpunkt | Standard in `BasePlugin` | Zweck |
|---|---|---|---|
| `String getHTML(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | [`/open/gethtml`](../rest-schnittstelle/ApiController/getHtml/index.md) | `""` | Fragetext für einen PIT-Tag |
| `String getAngabe(String params)` | [`/open/angabe`](../rest-schnittstelle/ApiController/getAngabe/index.md) | `null` | Angabetext für das Textfeld der Frage |
| `List<`[`PluginDatasetDto`](../dtos/PluginDatasetDto/index.md)`> generateDatasets()` | [`/open/generatedatasets`](../rest-schnittstelle/ApiController/generateDatasets/index.md) | leere Liste | Datensätze, die in der Frage vorhanden sein sollten |
| `Vector<String> getVars()` | [`/open/getvars`](../rest-schnittstelle/ApiController/getVars/index.md) | `null` | Variablen, die als Dataset benötigt werden |
| `String getMaxima(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q,` [`PluginMaximaCalcModeDto`](../dtos/PluginMaximaCalcModeDto/index.md) `mode)` | [`/open/maxima`](../rest-schnittstelle/ApiController/getMaxima/index.md) | `""` | Maxima-Berechnungsstring |
| [`ImageBase64Dto`](../dtos/ImageBase64Dto/index.md) `getImageDto(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | [`/open/image`](../rest-schnittstelle/ApiController/getImage/index.md) | erzeugt Bild über `parseDrawParams` + `paint`, PNG Base64 | Bild als Base64 |
| [`ImageUrlDto`](../dtos/ImageUrlDto/index.md) `getImageUrl(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | – (intern, z.B. im [`PluginDto`](../dtos/PluginDto/index.md)-Konstruktor) | speichert Bild im Image-Service, liefert URL | Bild als öffentliche URL |
| `String getPluginImageDescription(String imageParams,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | – | aus Typ, Version, Name, Config, Parametern und Frage | eindeutige Beschreibung, daraus wird der Dateiname des Bildes gebildet |
| `Vector<String[]> getImageTemplates()` | [`/open/imagetemplates`](../rest-schnittstelle/ApiController/getImageTemplates/index.md) | `null` | Bildvarianten: [0] Beschreibung, [1] PIG-Tag, [2] Hilfetext |
| [`CalcErgebnisDto`](../dtos/CalcErgebnisDto/index.md) `parserPlugin(`[`VarHashDto`](../dtos/VarHashDto/index.md) `vars,` [`CalcParamsDto`](../dtos/CalcParamsDto/index.md) `cp,` [`CalcErgebnisDto`](../dtos/CalcErgebnisDto/index.md)`... p)` | [`/open/parserplugin`](../rest-schnittstelle/ApiController/parserPlugin/index.md) | `null` | Funktion `plugin("name",p1,p2,…)` im Lösungsfeld |
| `String parserPluginEinheit(String... p)` | [`/open/parserplugineinheit`](../rest-schnittstelle/ApiController/parserPluginEinheit/index.md) | `null` | Recheneinheit des Ergebnisses von `parserPlugin` |
| `String modifyAngabe(String text,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | [`/open/modifyangabe`](../rest-schnittstelle/ApiController/modifyAngabe/index.md) | `text` | verändert Text in PI-Tags vor dem Darstellen |
| `String modifyAngabeTextkomplett(String text,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | [`/open/modifyangabetextkomplett`](../rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) | `text` | verändert den gesamten Angabetext |
| `String updatePluginstringJavascript(String pluginDef, String jsResult)` | [`/open/updatepluginstringjavascript`](../rest-schnittstelle/ApiController/updatePluginstringJavascript/index.md) | `pluginDef` | passt die Plugindefinition an das JavaScript-Ergebnis an (z.B. interaktive Karte) |
| [`PluginDto`](../dtos/PluginDto/index.md) `loadPluginDto(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q, int nr)` | [`/open/loadplugindto`](../rest-schnittstelle/ApiController/loadPluginDto/index.md) | `null` | [`PluginDto`](../dtos/PluginDto/index.md) für das JavaScript des Plugins |
| [`PluginRenderDto`](../dtos/PluginRenderDto/index.md) `renderLatex(`[`PluginDto`](../dtos/PluginDto/index.md)`, String answer, String mode)` | [`/open/renderlatex`](../rest-schnittstelle/ApiController/renderLatex/index.md) | leeres [`PluginRenderDto`](../dtos/PluginRenderDto/index.md) | LaTeX-Quelltext für den Fragedruck |
| [`PluginRenderDto`](../dtos/PluginRenderDto/index.md) `renderPluginResult(boolean tex,` [`PluginDto`](../dtos/PluginDto/index.md)`, String antwort,` [`ToleranzDto`](../dtos/ToleranzDto/index.md)`,` [`VarHashDto`](../dtos/VarHashDto/index.md)`,` [`PluginAnswerDto`](../dtos/PluginAnswerDto/index.md)`, double grade)` | [`/open/renderpluginresult`](../rest-schnittstelle/ApiController/renderPluginResult/index.md) | leeres [`PluginRenderDto`](../dtos/PluginRenderDto/index.md) | HTML oder LaTeX mit Schülereingabe und Lösung |
| [`InputElement`](../enums/InputElement/index.md) `getInputElement()` | – (in [`PluginGeneralInfo`](../dtos/PluginGeneralInfo/index.md)) | `JAVASCRIPT` wenn `javaScript`, sonst `TextArea` | Eingabeelement der Subquestion |
| `String getHelp()` | – (in [`PluginGeneralInfo`](../dtos/PluginGeneralInfo/index.md)) | Inhalt aller `helpfiles` | HTML-Hilfe |
| `List<`[`JavascriptLibrary`](../dtos/JavascriptLibrary/index.md)`> javascriptLibraries()` | – (in [`PluginGeneralInfo`](../dtos/PluginGeneralInfo/index.md)) | leer | externe JS-Libraries mit vollständiger URL |
| `List<`[`JavascriptLibrary`](../dtos/JavascriptLibrary/index.md)`> javascriptLibrariesLocal()` | – (in [`PluginGeneralInfo`](../dtos/PluginGeneralInfo/index.md)) | Quelltext aller `javascriptLibs` | lokale JS-Libraries |
| [`PluginGeneralInfo`](../dtos/PluginGeneralInfo/index.md) `getPluginGeneralInfo()` | [`/open/generalinfo`](../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) | aus den Eigenschaften | allgemeine Informationen |
| [`PluginConfigurationInfoDto`](../dtos/PluginConfigurationInfoDto/index.md) `configurationInfo(String configurationID)` | [`/open/configurationinfo`](../rest-schnittstelle/ApiController/configurationInfo/index.md) | aus den Eigenschaften | Informationen zum Start des Konfigurationsdialogs |
| [`PluginConfigDto`](../dtos/PluginConfigDto/index.md) `setConfigurationData(String configuration,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q)` | [`/open/setconfigurationdata`](../rest-schnittstelle/ApiController/setConfigurationData/index.md) | setzt `config`, leeres [`PluginConfigDto`](../dtos/PluginConfigDto/index.md) | Daten für das Konfigurations-JavaScript |
| `String getConfiguration()` | [`/open/getconfiguration`](../rest-schnittstelle/ApiController/getConfiguration/index.md) | `config` | aktuelle Konfiguration (oder `"@ERROR: Meldung"`) |

### Hilfsmethoden in BasePlugin

| Methode | Zweck |
|---|---|
| `BufferedImage getAWTImage(String params,` [`PluginQuestionDto`](../dtos/PluginQuestionDto/index.md) `q,` [`PluginImageResultDto`](../dtos/PluginImageResultDto/index.md) `r)` | erzeugt das Bild über `paint`, bei Fehlern ein Fehlerbild |
| `void paintFehler(Graphics g, String msg)` | gibt eine Fehlermeldung im Bild aus |
| `String loadHelpFile(String resource)` | lädt eine Hilfedatei und ersetzt Umlaute durch HTML-Entitäten |
| `String getHelpMessageFromResource(String name)` | lädt den `<body>`-Inhalt einer HTML-Ressource, ersetzt `{% raw %}{{servicepath}}{% endraw %}` |
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
| `score` | Musterlösung `answerText` als Zeit in Anführungszeichen (z.B. `"10:30"`) oder als Zahl (Sekunden); Schülereingabe wird mit `Datum.parseTime` in Sekunden umgerechnet und mit `PluginToolsMath.equals` unter Berücksichtigung der Toleranz verglichen → [`Score.OK`](../enums/Score/index.md) mit vollen Punkten, sonst [`Score.FALSCH`](../enums/Score/index.md) |
| `loadPluginDto` | `new` [`PluginDto`](../dtos/PluginDto/index.md)`(params, this, q, nr)` – Bild, Größe und Tag-Name |
| `configurationInfo` | setzt `configurationMode`, `javaScriptMethode = configPluginJS` und `configurationID` |
| `setConfigurationData` | übergibt Testparameter (`TEST`, `help`, `vars`) in [`PluginConfigDto.params`](../dtos/PluginConfigDto/index.md) |
| `getVars`, `parserPlugin`, `parserPluginEinheit` | liefern `null` (nicht verwendet) |

Hinweis: Das Feld `handcolor` ist vorgesehen, wird derzeit aber nicht ausgewertet.

[Referenz-Plugin (Java)](../index.md)
