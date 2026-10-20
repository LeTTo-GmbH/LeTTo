# PluginConfigurationInfoDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Information vom Plugin an LeTTo welche Informationen für die Konfiguration des Plugins benötigt werden und wie die Konfiguration des Plugins erfolgen soll.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginConfigurationInfoDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginConfigurationInfoDto.html` |

## Konstanten

| Konstante | Typ | Wert | Bedeutung |
|---|---|---|---|
| `CONFIGMODE_STRING` | int | `0` | Es gibt keinen expliziten Konfigurations-Dialog, sondern nur den Konfigurations-String |
| `CONFIGMODE_JSF` | int | `1` | Das Plugin ist im Edit-Service direkt eingebunden und wird über eine JSF-Seite direkt im Edit-Service konfiguriert |
| `CONFIGMODE_JAVASCRIPT` | int | `2` | Das Plugin wird über eine JavaScript - Funktion konfiguriert |
| `CONFIGMODE_URL` | int | `3` | Das Plugin wird über einen Dialog in einem iframe oder in einem eigenen Browser-TAB welches vom Plugin-Service über eine URL zur Verfügung gestellt wird konfiguriert |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `configurationID` | String | `""` | Konfigurations ID |
| `configurationMode` | int | `CONFIGMODE_STRING` | Konfigurations-Mode für die Konfiguration des Plugins |
| `useQuestion` | boolean | `true` | Gibt an ob im Plugin für die Konfiguration die Frage benötigt wird |
| `useVars` | boolean | `false` | Gibt an ob im Plugin für die Konfiguration der Vars Varhash benötigt wird |
| `useCVars` | boolean | `false` | Gibt an ob im Plugin für die Konfiguration der cVars Varhash benötigt wird |
| `useMaximaVars` | boolean | `false` | Gibt an ob im Plugin für die Konfiguration der MaximaVars Varhash benötigt wird |
| `useMVars` | boolean | `false` | Gibt an ob im Plugin für die Konfiguration der MVars Varhash benötigt wird |
| `addDataSet` | boolean | `false` | Gibt an, ob im Plugin-Konfig-Dialog Datensätze hinzugefügt werden können. =&gt; Button AddDataset in Fußzeile des umgebenden Dialogs, (nicht vom Plugin) |
| `calcMaxima` | boolean | `false` | Gibt an ob im Plugin bei der Konfiguration die Maxima-Berechnung durchlaufen werden kann. =&gt; Button Maxima in Fußzeile des umgebenden Dialogs, (nicht vom Plugin) |
| `externUrl` | boolean | `false` | Gibt an, ob das Plugin über den Browser direkt erreichbar ist |
| `javaScriptMethode` | String | `null` | JavaScript-Methode, die beim Konfigurieren des Plugins aufgerufen wird. Als Parameter wird ein [PluginConfigDto](../PluginConfigDto/index.md) übergeben (Konfigurationsstring des Plugins an diese Methode übergeben. JS-Code ist in den javascriptLibraries enthalten. |
| `configurationUrl` | String | `""` | Konfigurations-URL für den Konfigurationsdialog im Mode CONFIGMODE_URL |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/configurationinfo`](../../rest-schnittstelle/ApiController/configurationInfo/index.md) | Response | Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert |

## Verwendet in DTOs

* [PluginConfigurationConnection](../PluginConfigurationConnection/index.md) – Feld `pluginConfigurationInfoDto`

## Verwendet in der Plugin-API

* [`configurationInfo`](../../plugin-api/index.md): `PluginConfigurationInfoDto configurationInfo(String configurationID)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
