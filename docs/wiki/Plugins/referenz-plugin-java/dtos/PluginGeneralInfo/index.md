# PluginGeneralInfo
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Liefert allgemein Informationen zu einem Plugin, welche ohne Definition einer Plugin-Instanz allgemein gültig sind

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginGeneralInfo` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginGeneralInfo.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `version` | String | `""` | Version des Plugins |
| `wikiHelp` | String | `""` | Liefert den Namen der Wiki-Seite wenn eine Doku am LeTTo-Wiki vorliegt |
| `helpUrl` | String | `""` | Liefert eine Hilfe-URL für die Beschreibung des Plugins |
| `help` | String | `""` | Hilfetext für das Plugin |
| `defaultPluginConfig` | boolean | `true` | Gibt an ob die Standard-Plugin-Configuration verwendet werden soll |
| `math` | boolean | `false` | Gibt an ob das Plugin Ergebnisse und VarHash als JSON-String verarbeiten kann |
| `pluginType` | String | `""` | Klasse des Plugins |
| `initPluginJS` | String | `""` | Name der JAVA-Script Methode zur Plugin-Initialisierung für die interaktive Ergebniseingabe |
| `javaScript` | boolean | `false` | Gibt an ob das Plugin eine JavaScript Schnittstelle bei der Beispieldarstellung hat |
| `javascriptLibraries` | List&lt;[JavascriptLibrary](../../dtos/JavascriptLibrary/index.md)&gt; | `new ArrayList<>()` | Liste von JavaScript-Libraries, die im Header der HTML-Seite eingebunden werden müssen. Es muss die vollständige URL angegeben werden. für das Plugin notwendige JS-Libraries |
| `javascriptLibrariesLocal` | List&lt;[JavascriptLibrary](../../dtos/JavascriptLibrary/index.md)&gt; | `new ArrayList<>()` | Liste von LOKALEN JavaScript-Libraries, die im Header der HTML-Seite eingebunden werden müssen. Pfade werden relativ zum akt. Servernamen übergeben für das Plugin notwendige JS-Libraries |
| `inputElement` | String | [`InputElement.TextField.toString()`](../../enums/InputElement/index.md) | anzuzeigendes Eingabeelement als String |
| `cacheable` | boolean | `true` | Plugin ist stateless und liefert bei gleicher Angabe immer das gleiche Verhalten |
| `useVars` | boolean | `true` | Plugin benötigt zur Berechnung und Darstellung den VarHash der Datensätze |
| `useCVars` | boolean | `true` | Plugin benötigt zur Berechnung und Darstellung den VarHash der cvars - Konstante und Datensätze |
| `useVarsMaxima` | boolean | `true` | Plugin benötigt zur Berechnung und Darstellung den Varhash aller Maxima-Berechnungen ohne eingesetzte Datensatz-Variable |
| `useMVars` | boolean | `true` | Plugin benötigt zur Berechnung und Darstellung den Varhash aller Datensätze und Maxima-Ergebnisse mit eingesetzten Werten kombiniert in einem Hash |
| `pluginServiceURL` | String | `""` | URL des Plugin-Services für die direkte Kommunikation |

## Hinweise

* Das Feld `useVarsMaxima` heißt in `BasePlugin` und [`PluginConfigurationInfoDto`](../../dtos/PluginConfigurationInfoDto/index.md) `useMaximaVars`.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`GET /open/generalinfolist`](../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) | Response über [`PluginGeneralInfoList.pluginInfos`](../../dtos/PluginGeneralInfoList/index.md) | Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| [`POST /open/generalinfo`](../../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) | Response | Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin |
| [`GET /<endpoint>/api/open/generalinfolist`](../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfoList/index.md) | Response über [`PluginGeneralInfoList.pluginInfos`](../../dtos/PluginGeneralInfoList/index.md) | liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| [`POST /<endpoint>/api/open/generalinfo`](../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfo/index.md) | Response | liefert die allgemeinen Konfigurationsinformationen zu einem Plugin Body: String - Name des Plugins |

## Verwendet in DTOs

* [PluginGeneralInfoList](../../dtos/PluginGeneralInfoList/index.md) – Feld `pluginInfos`

## Verwendet in der Plugin-API

* [`getPluginGeneralInfo`](../../plugin-api/index.md): `PluginGeneralInfo getPluginGeneralInfo()`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
