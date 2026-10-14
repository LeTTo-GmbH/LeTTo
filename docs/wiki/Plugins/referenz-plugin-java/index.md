# Referenz-Plugin (Java)
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Das Projekt **plugin-demo-java** ist die Referenzimplementierung eines LeTTo-Plugin-Services in Java (Spring Boot).
Es dient als Vorlage für eigene Plugins und enthält als Beispiel das Plugin **Uhr1** – ein Uhrblatt, auf dem eine Uhrzeit
eingestellt und mit der Musterlösung verglichen wird. Das Uhr-Plugin dient nur zur Veranschaulichung und ist nicht für den Unterricht gedacht.

## Allgemeines

* Ein Plugin-Service läuft als eigener Docker-Container im Netzwerk `nw-letto` neben dem LeTTo-Server.
* Ein Service kann mehrere Plugins (Plugin-Typen) bereitstellen.
* LeTTo kommuniziert mit dem Plugin ausschließlich über eine REST-Schnittstelle (JSON).
* Beim Start registriert sich der Service selbst am Setup-Service des LeTTo-Servers.
* Das Plugin liefert
  * die Darstellung in der Frage (Bild, HTML, JavaScript),
  * optional eine Maxima-Berechnung, Angabetexte und Datensätze,
  * einen Konfigurationsdialog für Lehrende,
  * die Bewertung der Schülereingabe.

## Technische Daten

| Eigenschaft | Wert |
|---|---|
| Sprache | Java 25 |
| Framework | Spring Boot 4.0.8 |
| API-Doku | springdoc-openapi 3.0.3, Beschreibungen aus der JavaDoc (therapi-runtime-javadoc) |
| Docker-Image | `lettohub/letto-service-<endpoint>:stable` (Basis `eclipse-temurin:25-jdk-jammy`) |
| Endpoint-Pfad im Demo | `/plugindemo` |
| Service-Name | `letto-plugindemo`, Version 1.0 |

## Links

* Quellcode: [https://github.com/LeTTo-GmbH/plugin-demo-java](https://github.com/LeTTo-GmbH/plugin-demo-java)
* Python-Portierung mit derselben REST-Schnittstelle: [Referenz-Plugin (Python)](../referenz-plugin-python/index.md)
* Am eigenen Server (bei installiertem Plugin, `<endpoint>` z.B. `plugindemo`):
  * Hilfeseite: `https://<servername>/<endpoint>/help`
  * Swagger-UI: `https://<servername>/<endpoint>/swagger-ui.html`
  * OpenAPI-Beschreibung (JSON): `https://<servername>/<endpoint>/v3/api-docs`
  * JavaDoc: `https://<servername>/<endpoint>/open/javadoc/index.html`
* Plugintester zum Testen: `https://<servername>/plugintester` (über das Setup-Service installierbar)

## Inhalt

* [Architektur](architektur/index.md): Aufbau des Services, Paketstruktur, Ablauf zwischen LeTTo-Server und Plugin
* [Eigenes Plugin erstellen](eigenes-plugin/index.md): Schritt-für-Schritt-Anleitung aus dem Demoprojekt
* [Plugin-API](plugin-api/index.md): `BasePlugin` und `PluginService` – welche Methoden ein Plugin überschreibt, am Beispiel Uhr
* [REST-Schnittstelle](rest-schnittstelle/index.md): alle Controller und Endpunkte, je Endpunkt eine eigene Seite mit Request, Response, Ablauf und Fehlerfällen
* [DTOs](dtos/index.md): Datenklassen der Schnittstelle, je DTO eine Seite mit Feldern und allen Endpunkten, in denen es vorkommt
* [Enums](enums/index.md): Aufzählungstypen der Schnittstelle, je Enum eine Seite mit Werten und Verwendung
* [Build und Deployment](build-deployment/index.md): Build-Scripts, Docker, Proxy, Registrierung, Debugging

[Plugins](../index.md)
