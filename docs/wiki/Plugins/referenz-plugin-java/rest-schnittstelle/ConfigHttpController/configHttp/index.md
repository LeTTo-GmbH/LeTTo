# GET /&lt;endpoint&gt;/open/confighttp
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ConfigHttpController](../index.md) |
| Java-Methode | `configHttp` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>/open/confighttp` |
| Erreichbarkeit | extern über den Proxy |
| Content-Type | `text/html` |
| Query-Parameter | `typ` (String) |
| Query-Parameter | `configurationID` (String) |
| Response | String |

## Beschreibung

Liefert die HTML-Seite des Konfigurationsdialogs.

## Request

* `typ` (String): Typ des Plugins
* `configurationID` (String): ID der zuvor mit configurationInfo angelegten Konfigurations-Verbindung

## Response

Typ: String

HTML-Seite des Dialogs oder 404, wenn keine gültige Verbindung existiert

Die Antwort ist eine HTML-Seite.

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getConfigurationConnection`, `getUriGetPluginDto`.
* Die Seite bindet `<endpoint>/open/js/jquery-3.6.0.min.js` und den Quelltext aller lokalen JavaScript-Libraries des Plugins (`javascriptLibrariesLocal()`) ein.
* Sie enthält `<div id="configform_div">`, das versteckte Feld `.configform_config` mit der aktuellen Konfiguration und das [`PluginConfigDto`](../../../dtos/PluginConfigDto/index.md) als JSON in `<script id="pluginConfigDto">`.
* Anschließend wird die Konfigurations-Methode des Plugins (`javaScriptMethode` aus [`PluginConfigurationInfoDto`](../../../dtos/PluginConfigurationInfoDto/index.md)) mit dem JSON-String aufgerufen. Der Methodenname muss ein gültiger JavaScript-Bezeichner sein.
* Fehlt im [`PluginConfigDto`](../../../dtos/PluginConfigDto/index.md) die `pluginDtoUri`, wird sie auf den externen `reloadplugindto`-Endpunkt gesetzt.

## Fehlerfälle

* 404 Not Found, wenn die Konfigurations-Sitzung fehlt oder abgelaufen ist.
* 500 Internal Server Error, wenn das Plugin keine gültige Konfigurations-Methode angibt.

## Siehe auch

* [`POST /open/configurationinfo`](../../../rest-schnittstelle/ApiController/configurationInfo/index.md) – Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert
* [`POST /open/setconfigurationdata`](../../../rest-schnittstelle/ApiController/setConfigurationData/index.md) – Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration
* [`POST /<endpoint>/api/open/reloadplugindto`](../../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/getconfiguration`](../../../rest-schnittstelle/ApiController/getConfiguration/index.md) – Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet


[ConfigHttpController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
