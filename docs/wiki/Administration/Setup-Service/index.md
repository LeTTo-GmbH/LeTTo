# Setup-Service

Das Setup-Service ist die Verwaltungsoberfläche eines LeTTo-Servers. Damit werden alle Docker-Container (Datenbanken,
Proxy, Services, Plugins, Schulen) gestartet, gestoppt und aktualisiert, die zentrale Konfigurationsdatei `.env` und die
Compose-Dateien bearbeitet, Schulen angelegt, Datensicherungen eingerichtet und der Server überwacht.
Es ist für **globale Administratoren** des Servers gedacht, nicht für Lehrer oder Schul-Administratoren.

Diese Seite beschreibt Version 1.3. Die frühere Beschreibung (Setup direkt am Host) liegt im
[Archiv](../Archiv/Setup-Service-alt/index.md).

## Verbindung zum Setup-Service

Das Setup-Service läuft als Docker-Container `letto-setup` am LeTTo-Server. Ein eigenes Setup direkt am Host (ohne
Docker) gibt es seit Version 1.3 nicht mehr.

| Weg | Adresse | Wann |
|---|---|---|
| über den Reverse-Proxy | `https://<server>/config` | Normalfall |
| direkt am Container | `https://<server>:3096/config` | wenn der Proxy nicht läuft; Port 3096 (`PORT_SETUP` in der `.env`) darf nicht aus dem Internet erreichbar sein |
| per ssh-Tunnel | `https://127.0.0.1:13096/config` | Port 3096 ist in der Firewall gesperrt, ssh ist erreichbar |

Ein ssh-Tunnel auf den Port 3096 des Servers:

```bash
# Linux, macOS, Windows-PowerShell
ssh benutzer@letto.meine-schule.at -L 13096:127.0.0.1:3096 -C -N
```

Im Container selbst lauscht das Setup auf Port 9096 (HTTPS). Dieser Port ist am Host als 3096 veröffentlicht.

## Anmeldung

Angemeldet wird auf der Seite [Anmeldung](Anmeldung/index.md):

* Benutzer **`admin`** mit dem Passwort `ADMIN_PASSWORD` aus der `.env` – der lokale Administrator des Setups.
  Solange noch keine Schule eingerichtet ist, kann sich nur dieser Benutzer anmelden.
* LeTTo-Benutzer mit **globalen Administratorrechten** (z. B. `adminglobal<schulkürzel>`), angemeldet über den
  Login-Service. Andere Benutzer werden abgewiesen.

## Aufbau der Oberfläche

Nach der Anmeldung erscheint die [Hauptseite](Hauptseite/index.md). Sie hat eine Titelleiste mit den Menüs
**Werkzeuge**, **Konfiguration**, **Verwaltung** und **Hilfe** und vier Tabs:

* [Systeminformation](Hauptseite/index.md#tab-systeminformation) – Zustand des Servers (Speicher, Festplatte, CPU, Erreichbarkeit)
* [Services](Services/index.md) – alle Docker-Container von LeTTo mit Start, Stop, Update, Zertifikat, Weiterleitung
* [Schulen](Schulen/index.md) – die installierten Schulen
* [Question-Services](Question-Services/index.md) – externe Question-Services (Fragesammlungen)

Alle anderen Seiten haben oben rechts die Buttons **Übersicht** (zurück zur Hauptseite) und **Abmelden** und meist einen
Button **zurück** bzw. **Abbruch**. Das Ergebnis einer Aktion steht in einer Statusleiste am unteren Fensterrand
(grün = in Ordnung, rot = Fehler, gelb = Warnung, blau = Information). Länger laufende Aktionen öffnen die
[Befehlsausgabe](Befehlsausgabe/index.md).

## Alle Seiten

| Menü / Aufruf | Seite | Inhalt |
|---|---|---|
| – | [Anmeldung](Anmeldung/index.md) | Login am Setup |
| – | [Hauptseite](Hauptseite/index.md) | Titelleiste, Menüs, Tab Systeminformation |
| Tab Services | [Services](Services/index.md) | Docker-Container, Zertifikat, LTI-Datenbank, Restkey, Weiterleitung |
| Tab Schulen | [Schulen](Schulen/index.md) | installierte Schulen, Logs, Updates, SQL-Dumps, Lizenzen |
| Tab Question-Services | [Question-Services](Question-Services/index.md) | externe Question-Services |
| Werkzeuge → Kommando-Eingabe | [Kommandoeingabe](Kommandoeingabe/index.md) | Shell-Befehle im Setup-Container |
| Werkzeuge → MySQL-Kommando | [MySQL-Befehl](MySQL-Befehl/index.md) | SQL-Befehle an die MySQL-Datenbanken |
| Werkzeuge → Explorer | [Explorer](Explorer/index.md) | Dateien anzeigen, bearbeiten, hoch- und herunterladen |
| Konfiguration → Backup/Cronjob | [Datensicherung](Datensicherung/index.md) | automatisches Backup, Datenbank-Dumps |
| Konfiguration → Allgemein | [Allgemeine Einstellungen](Allgemeine-Einstellungen/index.md) | Standardsprache |
| Konfiguration → E-Mail | [E-Mail](E-Mail/index.md) | SMTP-Server, Test-Mail |
| Konfiguration → Update-Konfiguration | [Update-Konfiguration](Update-Konfiguration/index.md) | Image-Tags, Updates aller Container, neue Services |
| Konfiguration → Server-Token | [Server-Token](Server-Token/index.md) | Tokens für fremde Server |
| Konfiguration → Plugins | [Plugins](Plugins/index.md) | registrierte Plugin-Services |
| Plugins → hinzufügen | [Plugin hinzufügen](Plugin-hinzufuegen/index.md) | neues Plugin aus Proxy- und Compose-Datei |
| Verwaltung → Benutzer | [Benutzer](Benutzer/index.md) | angemeldete Benutzer, Benutzerdetails |
| Benutzer → Benutzer suchen | [Benutzersuche](Benutzersuche/index.md) | Benutzer aller Schulen suchen, Statistik |
| Benutzer → LDAP/AD Login | [LDAP/AD](LDAP-AD/index.md) | Anmeldung über Active Directory/LDAP |
| Verwaltung → Datenbanken | [Datenbanken](Datenbanken/index.md) | MySQL, Mongo, Redis, LTI, Schul-Datenbanken: Backup, Reparatur, Upgrade |
| Verwaltung → Host | [Host](Host/index.md) | Betriebssystem, Ressourcen, Docker |
| Verwaltung → System-Status | [System-Status](System-Status/index.md) | Verlauf von CPU, Speicher und Festplatte |
| Hilfe → Dokumentation | [Dokumentation](Dokumentation/index.md) | Doku und Swagger der Services |
| Services → STATUS | [Docker-Status](Docker-Status/index.md) | alle Container, Netzwerke und Volumes |
| Services → Proxy Konfiguration | [Proxy-Konfiguration](Proxy-Konfiguration/index.md) | nginx-Konfiguration des Proxy |
| Schulen → Schule hinzufügen / edit Daten | [Schule bearbeiten](Schule-bearbeiten/index.md) | Schule anlegen, bearbeiten, importieren, löschen |
| Question-Services → Konfiguration | [Externes Questionservice](Externes-Questionservice/index.md) | Question-Service anlegen und konfigurieren |
| EDIT YAML, EDIT .env, out, Log … | [Datei-Editor](Datei-Editor/index.md) | Dateien bearbeiten und Logs anzeigen |
| Start, Stop, Update, Backup … | [Befehlsausgabe](Befehlsausgabe/index.md) | Ausgabe laufender Aktionen |

## Wichtige Dateien und Verzeichnisse

| Pfad am Host | Inhalt |
|---|---|
| `/opt/letto/docker/compose/letto/.env` | zentrale Konfiguration (Servername, Passwörter, Schulen, Mail, Backup …); im Setup als `EDIT .env` |
| `/opt/letto/docker/compose/letto/*.yml` | Compose-Dateien aller Container (`docker-compose-*.yml`, `docker-service-*.yml`, `docker-lettoserver-<schule>.yml`, `docker-data-<schule>.yml`) |
| `/opt/letto/docker/proxy` | nginx-Konfiguration des Proxy |
| `/opt/letto/docker/storage/backup` | tägliche Datensicherungen |
| `/opt/letto/docker/storage/database-dump` | SQL-Dumps der Schulen, die in Schulen importiert werden können |
| `/opt/letto/docker/storage/database-backup` | Sicherungen der Datenbank-Container (MySQL, Mongo, Redis) |
| `/opt/letto/docker/storage/log` | Logdateien aller Services |

Änderungen an der `.env` und an den Compose-Dateien wirken erst, wenn der betroffene Container neu gestartet wird.

## siehe auch

* [Administration](../index.md)
* [Installation](../Installation/index.md)
* [Datensicherung-Docker](../Datensicherung-Docker/index.md)
* [Https-Zertifikat](../Https-Zertifikat/index.md)
* [Container Struktur](../Docker/ContainerStruktur/index.md)
* [Setup-Service (alte Beschreibung)](../Archiv/Setup-Service-alt/index.md)
