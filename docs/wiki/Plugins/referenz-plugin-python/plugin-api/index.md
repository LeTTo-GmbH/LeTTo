# Plugin-API (Python)
<!-- erstellt aus plugin-demo-python @ 7902099 (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

Anders als in Java gibt es keine Basisklasse mit überschreibbaren Methoden. Die Plugin-Logik besteht aus drei Teilen:

* den `CONF_*`-Konstanten am Anfang von `app/main.py`,
* der Plugin-Klasse `PluginDemo`,
* den Endpunkt-Funktionen in `mount_internal_open`, die die Methoden von `PluginDemo` aufrufen oder feste Antworten liefern.

## CONF-Konstanten

| Konstante | Wert im Demo | Bedeutung | Java-Gegenstück |
|---|---|---|---|
| `CONF_STANDARD_SERVICEPATH` | `/plugindemopython` | Servicepfad, wenn die Umgebungsvariable `SERVICEPATH` fehlt; muss zur `location` der Proxy-Konfiguration passen | `Endpoint.servicepath` |
| `CONF_APPLICATION_NAME` | `plugindemopython` | Name des Plugin-Services | `spring.application.name` |
| `CONF_PLUGIN_NAME` | `letto-plugindemopython` | Name, unter dem der Service am Setup registriert wird | `PluginConfiguration.PLUGIN_NAME` |
| `CONF_PLUGIN_AUTHOR`, `CONF_PLUGIN_LICENSE` | `LeTTo GmbH`, `OpenSource` | Autor und Lizenz | `PLUGIN_AUTHOR`, `PLUGIN_LICENSE` |
| `CONF_PLUGIN` | `UhrPy` | Plugin-Typ, unter dem das Plugin in LeTTo erscheint | Name in `registerPlugin` |
| `CONF_VERSION` | `1.0` | Version | `version` |
| `CONF_INIT_JS` | `initPluginUhrPy` | JavaScript-Methode zur Initialisierung | `initPluginJS` |
| `CONF_CONFIG_JS` | `configPluginUhrPy` | JavaScript-Methode für den Konfigurationsdialog | `configPluginJS` |
| `CONF_HELPFILES` | `["plugins/uhr/UhrPy.html"]` | Hilfedateien (relativ zu `resources/`) | `helpfiles` |
| `CONF_JSLIBS` | `["plugins/uhr/uhrPyScript.js", "plugins/uhr/uhrPyConfigScript.js"]` | JavaScript-Dateien, deren Quelltext an LeTTo übergeben wird | `javascriptLibs` |
| `CONF_wikiHelp`, `CONF_helpUrl` | `Plugins`, `""` | Wiki-Seite bzw. Hilfe-URL | `wikiHelp`, `helpUrl` |
| `CONF_defaultPluginConfig` | `False` | Standard-Plugin-Konfiguration verwenden | `defaultPluginConfig` |
| `CONF_width`, `CONF_height` | 500, 500 | Größe des Plugin-Bereichs im `PluginDto` | `width`, `height` |
| `CONF_math` | `False` | Plugin kann CalcErgebnis und VarHash als JSON verarbeiten | `math` |
| `CONF_cacheable` | `True` | Plugin ist stateless | `cacheable` |
| `CONF_useQuestion`, `CONF_useVars`, `CONF_useCVars`, `CONF_useMaximaVars`, `CONF_useMVars` | alle `True` | benötigte Daten der Frage | gleichnamige Felder |
| `CONF_configurationMode` | 2 | Standard-Konfigurations-Modus: 0 String, 1 JSF, 2 JavaScript, 3 URL | `configurationMode` |
| `CONF_addDataSet`, `CONF_calcMaxima` | `True`, `True` | Buttons „AddDataset" und „Maxima" im umgebenden Dialog | `addDataSet`, `calcMaxima` |
| `CONF_externUrl` | `False` | Plugin ist über den Browser direkt erreichbar | `externUrl` |
| `CONF_pluginServiceURL` | `""` | URL des Plugin-Services für die direkte Kommunikation | `pluginServiceURL` |

## Klasse PluginDemo

| Methode | Zweck | Endpunkt | Java-Gegenstück |
|---|---|---|---|
| `__init__(name, params)` | wertet die durch `;` getrennten Konfigurationsparameter aus | – (jede Anfrage) | Konstruktor |
| `get_help()` | Inhalt aller `CONF_HELPFILES` | – (in `PluginGeneralInfo`) | `getHelp()` |
| `plugin_general_info(typ)` | allgemeine Informationen, JavaScript-Dateien als Quelltext (`local="JAVASCRIPT"`) | [generalinfo](../../referenz-plugin-java/rest-schnittstelle/ApiController/pluginGeneralInfo/index.md), [generalinfolist](../../referenz-plugin-java/rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) | `getPluginGeneralInfo()` |
| `get_image_base64(params, q)` | Uhrblatt als PNG (320 × 320 Pixel), Base64-codiert | [image](../../referenz-plugin-java/rest-schnittstelle/ApiController/getImage/index.md), [loadplugindto](../../referenz-plugin-java/rest-schnittstelle/ApiController/loadPluginDto/index.md) | `getImageDto()` |
| `get_html(params, q)` | kurzer HTML-Hinweis „Gib die Zeit im Format HH:MM ein." | [gethtml](../../referenz-plugin-java/rest-schnittstelle/ApiController/getHtml/index.md), [renderpluginresult](../../referenz-plugin-java/rest-schnittstelle/ApiController/renderPluginResult/index.md) | `getHTML()` |
| `get_angabe()` | fester Angabetext „Stelle die Uhr ab und gib die Zeit im Format HH:MM ein." | [angabe](../../referenz-plugin-java/rest-schnittstelle/ApiController/getAngabe/index.md) | `getAngabe()` |
| `score(antwort, toleranz, answerDto, grade)` | Bewertung der Schülereingabe, siehe unten | [score](../../referenz-plugin-java/rest-schnittstelle/ApiController/score/index.md) | `score()` |

Alle anderen Plugin-Endpunkte liefern feste Antworten direkt aus der Endpunkt-Funktion – siehe [REST-Schnittstelle](../rest-schnittstelle/index.md).
Für ein eigenes Plugin dort die entsprechende Methode von `PluginDemo` aufrufen.

Die Konfigurationssitzungen verwenden zusätzlich `build_configuration_info(plugin, configurationID)`; sie erzeugt das
`PluginConfigurationInfoDto` aus den `CONF_*`-Werten und dem Konfigurations-Modus des Plugins (Java: `configurationInfo()`).

## Beispiel: Uhr-Plugin UhrPy

### Konfigurationsparameter

Durch `;` getrennt, z.B. `mode=js;bgcolor=green`:

| Parameter | Bedeutung |
|---|---|
| `mode=js` / `mode=iframe` / `mode=string` / `mode=jsf` | Konfigurations-Modus JavaScript (Standard) / URL / String / JSF. Der URL-Modus ist in der Python-Version nicht implementiert. |
| `bgcolor=<farbe>` | Hintergrundfarbe: `white` (Standard), `black`, `red`, `green`, `blue`, `yellow`. Ungültige Werte landen in `configMessage` und werden als `error` beim Bild geliefert. |

Gegenüber Java fehlen der Parameter `w<Prozent>` und die Bildparameter `size=` im PIG-Tag; die erlaubten Farben unterscheiden sich (`white`, `black` statt `gray`).

### Bild und JavaScript

* Das Uhrblatt **ohne Zeiger** wird mit Pillow als PNG erzeugt; die Zeiger und die Eingabe zeichnet `initPluginUhrPy(dtoString, active)` im Browser.
* Der Konfigurationsdialog `configPluginUhrPy(dtoString)` zeigt eine Live-Vorschau; dafür holt er per Ajax ein neues `PluginDto` von `dto.pluginDtoUri`.
* Für die JavaScript-Schnittstelle gelten dieselben Vorgaben wie beim Java-Plugin (`#<tagName>_div`, `.<tagName>_inp`, `#configform_div`, `.configform_config`) –
  siehe [Eigenes Plugin erstellen (Java)](../../referenz-plugin-java/eigenes-plugin/index.md).

### Bewertung

| Regel | Python | Java |
|---|---|---|
| Musterlösung | `answerDto.answerText` als Uhrzeit `HH:MM`, `HH:MM:SS` oder `HH:MM:SS.sss` | zusätzlich als Zahl in Sekunden |
| zusätzlich richtig | wenn die Antwort genau `answerDto.ergebnis.string` entspricht | – |
| Vergleich | nach Zeigerstellung: 12- und 24-Stunden-Angabe gleich (`3:15` = `15:15`), Abstand über 12 Uhr hinweg (`11:59` und `0:01` liegen 2 Minuten auseinander) | direkter Vergleich der Sekunden |
| Toleranz `RELATIV` | bezogen auf eine Stunde: 1 % = 36 Sekunden | relativ zum größeren Wert |
| Toleranz `ABSOLUT` | in Sekunden | in Sekunden |
| ohne Toleranz | `1e-10` relativ, also praktisch exakt | nicht gesondert behandelt |
| Ergebnis | `OK` mit vollen Punkten, sonst `FALSCH`; `htmlScoreInfo = "Wert:<antwort>"` | gleich |

[Referenz-Plugin (Python)](../index.md)
