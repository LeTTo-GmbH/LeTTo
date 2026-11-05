# Setup-Service: Keycloak (SSO)

Keycloak ist die Grundlage für **Single Sign-On** (Anmeldung mit Microsoft oder Google) und die
**2-Faktor-Authentifizierung** von LeTTo. Das Setup-Service installiert Keycloak wie jeden anderen Service als
Docker-Container und richtet ihn für die Installation ein.

> **Stand:** Version 1.3, in Entwicklung. Umgesetzt sind die Installation und Einrichtung von Keycloak, die Anmeldung über SSO mit Google und
> Microsoft (Einrichtung der Anbieter im Setup-Service) und der [zweite Faktor](Zweiter-Faktor/index.md) bei der Anmeldung über SSO.
> ID Austria sowie der erzwungene zweite Faktor beim Teststart folgen in weiteren Schritten und stehen noch nicht zur Verfügung.

## Aufgabenteilung

Keycloak vermittelt nur die Identität und verwaltet die Faktoren. Alles andere bleibt, wie es ist:

| Aufgabe | zuständig |
|---|---|
| Anmeldung beim Anbieter (Microsoft, Google …), zweiter Faktor | Keycloak |
| LeTTo-Token, Sitzung, Mehrfach-Login, Lizenzprüfung | [Login-Service](../../Docker/Lettohub_letto-service-login/index.md) bzw. Setup-Service |
| Benutzer, Rollen, Schulen, Klassen, Passwörter | Data-Service der Schule |

Rollen werden nie aus Angaben eines fremden Anbieters übernommen. Der Login-Service prüft die Anmeldung bei Keycloak
selbst (Signatur, Aussteller, Stufe und Zeitpunkt der Anmeldung) und verlässt sich nicht darauf, dass Keycloak die
verlangte Sicherheitsstufe eingehalten hat.

## Installation

1. Im Setup unter **Konfiguration → Update-Konfiguration** erscheint `keycloak` in der Liste **Verfügbare yml-Dateien**.
2. **Service installieren** drücken. Das Setup
   * erzeugt zufällige Passwörter und trägt sie mit der öffentlichen Adresse in die `.env` ein (nur fehlende Werte, vorhandene bleiben),
   * legt die Datenbank `keycloak` und den Benutzer `keycloak` in `letto-mysql` an,
   * schreibt `docker-service-keycloak.yml` und die Proxy-Datei `keycloak.conf`,
   * startet den Container `letto-keycloak` und richtet danach den Realm `letto` ein (der erste Start dauert etwa eine Minute).
3. Im Tab [Services](../Services/index.md) erscheint Keycloak in der Statuszeile unter **SSO**: grün = läuft, rot = installiert, läuft aber nicht.

Die Einrichtung ist wiederholbar: Ein vorhandener Realm wird nie verändert, Anpassungen der Administratoren bleiben
erhalten.

## Was eingerichtet wird

* **Realm `letto`** mit dem Anmeldeablauf `letto-browser`:
  * Stufe 1 = Passwort (`acr` 1), Stufe 2 = Einmalcode/OTP (`acr` 2)
  * Ein Anbieter kann über `kc_idp_hint` direkt gewählt werden.
  * Stufe 2 muss bei jeder Anforderung neu nachgewiesen werden; Keycloak stuft nie still auf Stufe 1 ab.
* **Client `letto-login`** für den Login-Service (vertraulich, PKCE S256, Rücksprungadresse `https://<server>/login/open/sso/callback`).
* **Datenbank** `keycloak` im vorhandenen MySQL – es ist kein weiterer Datenbank-Container nötig.


Der Realm selbst wird nur beim ersten Mal angelegt; Änderungen der Administratoren bleiben erhalten. Der **Client `letto-login` gehört dem Setup-Service**: Seine Rücksprungadressen, sein Geheimnis (aus der `.env`) und das Dienstkonto werden bei jeder Installation auf den Sollzustand gebracht.

## Erreichbarkeit und Sicherheit

| Adresse | Erreichbar | Inhalt |
|---|---|---|
| `https://<server>/auth/realms/letto/…` | von außen | Anmeldung, Discovery-Dokument, Schlüssel |
| `https://<server>/auth/admin/…`, `/auth/realms/master/…`, `/auth/metrics`, `/auth/health` | **gesperrt** (404 im Proxy) | Admin-Konsole, Verwaltungs-Realm |
| `http://127.0.0.1:8480/auth` | nur am Server (`PORT_KEYCLOAK`, gebunden an `SERVICE_BIND`) | Admin-Konsole und Admin-API, von außen nur per ssh-Tunnel |

Ein ssh-Tunnel zur Admin-Konsole:

```bash
ssh benutzer@letto.meine-schule.at -L 8480:127.0.0.1:8480 -C -N
# danach im Browser: http://localhost:8480/auth
```

Der Benutzer der Admin-Konsole ist `KEYCLOAK_ADMIN_USER` (Standard `admin`) mit dem Passwort `KEYCLOAK_ADMIN_PASSWORD` aus der `.env`.

## Anmeldung über SSO

Ist Keycloak installiert, zeigt die Login-Seite unter dem Passwort-Login einen Bereich **Anmeldung über SSO** mit
Schulwahl und der Schaltfläche **Mit SSO anmelden**. Nach der Installation von Keycloak startet das Setup-Service den
Login-Service neu, damit er Adresse und Client-Geheimnis übernimmt.

- Der Login-Service prüft das ID-Token von Keycloak selbst (Signatur, Aussteller, Zielgruppe, Gültigkeit, `nonce`).
- Rollen, Schule und Rechte kommen **immer aus LeTTo**, nie aus dem Token des Anbieters.
- Es werden **keine Benutzer automatisch angelegt**. Beim ersten SSO-Login bestätigt der Benutzer einmal mit LeTTo-Benutzername
  und Passwort, dass das Konto ihm gehört; danach ist das SSO-Konto mit dem LeTTo-Benutzer verknüpft und der SSO-Login genügt.
  Gespeichert werden nur die Kennung des SSO-Kontos (Aussteller und `sub`) und die bestätigte E-Mail-Adresse.
- Ein SSO-Login durchläuft dieselbe Prüfung wie der Passwort-Login: Mehrfach-Login, Fingerprint und Lizenzprüfung
  (abgelaufene oder überschrittene Lizenz weist Schüler ab) gelten unverändert.
- **Gemeinsames Abmelden:** Wer sich in LeTTo abmeldet (Legacy-Server, Main-Service oder App – alle melden sich dabei beim
  Login-Service ab), wird auch in Keycloak abgemeldet. Der nächste Klick auf „Mit SSO anmelden“ verlangt dann wieder die
  Anmeldung, auch am selben Browser (wichtig für gemeinsam genutzte PCs). Dafür merkt sich der Login-Service zur LeTTo-Session
  die Keycloak-Sitzung und beendet sie beim Logout über die Admin-API von Keycloak. Das Dienstkonto des Clients `letto-login`
  hat dazu das Recht `manage-users` im Realm `letto`. Läuft Keycloak nicht, bleibt der Logout in LeTTo trotzdem wirksam;
  die Keycloak-Sitzung läuft dann von selbst ab (Standard: 30 Minuten Leerlauf).
- Nach dem Login (mit Passwort oder SSO) leitet der Login-Service wie LeTTo-Main zur **App** weiter
  (`/app/pages/token/&lt;Schule&gt;/&lt;Token&gt;`). Mit `LOGIN_REDIRECT_APP=false` in der `.env` geht es wie früher zum LeTTo-Server der Schule.
- Ist Keycloak nicht erreichbar, bleibt der Login mit Benutzername und Passwort möglich.
- Optional zeigt die Variable `SSO_PROVIDERS` (Aliasnamen der in Keycloak eingerichteten Anbieter, z. B. `google microsoft`)
  zusätzliche Schaltflächen je Anbieter.

## SSO und zweiten Faktor zentral ein- und ausschalten

Im Setup-Service unter **Konfiguration → SSO-Anbieter** gibt es im Abschnitt **Allgemein** zwei Schalter für den ganzen Server:

* **Anmeldung über SSO eingeschaltet:** Ist er aus, zeigt die Login-Seite nichts von SSO, die Anmeldung über SSO wird abgelehnt und das Profil bietet
  keine Verknüpfungen an. Verknüpfungen und Einstellungen der Benutzer bleiben gespeichert und gelten wieder, sobald SSO eingeschaltet wird.
* **Zweiter Faktor (2FA) eingeschaltet:** Ist er aus, wird kein zweiter Faktor verlangt, auch wenn Benutzer ihn für sich eingeschaltet haben. Das Profil bietet die
  Einstellung dann nicht an. Er gilt nur, wenn SSO eingeschaltet ist.

Beim Speichern wird der Login-Service neu gestartet. Beide Schalter sind ab Werk eingeschaltet (`SSO_ENABLED`, `SSO_MFA_ENABLED` in der `.env`).

## Google und Microsoft einrichten

Die Anbieter werden im Setup-Service unter **Konfiguration → SSO-Anbieter** eingetragen. Vorher muss beim Anbieter eine App
registriert werden. Eine ausführliche Schritt-für-Schritt-Anleitung (inklusive Fragen an die Schul-IT und Fehlersuche) steht unter
[Registrierungsdaten für Google und Microsoft besorgen](Registrierungsdaten/index.md). Die **Weiterleitungs-URI** dafür zeigt die Setup-Seite an, sie lautet
`https://&lt;Server&gt;/auth/realms/letto/broker/google/endpoint` bzw. `.../broker/microsoft/endpoint`.

**Google**

1. In der Google Cloud Console (console.cloud.google.com) ein Projekt anlegen.
2. Den **OAuth-Zustimmungsbildschirm** einrichten. Für Tests: Nutzertyp „Extern“, Status „Testing“ und die eigene Adresse als
   Testnutzer eintragen. Für Schulen mit Google Workspace for Education: Nutzertyp „Intern“.
3. Unter „Anmeldedaten“ eine **OAuth-Client-ID** vom Typ „Webanwendung“ anlegen und die Weiterleitungs-URI eintragen.
4. Client-ID und Client-Geheimnis in der Setup-Seite eintragen. Mit **Erlaubte Domain** (z. B. `schule.at`) dürfen sich nur
   Konten dieser Workspace-Domain anmelden.

**Microsoft (Schul-Tenant, Microsoft Entra ID)**

1. Im Azure-Portal unter „Microsoft Entra ID → App-Registrierungen“ eine neue Registrierung anlegen
   (Konten in diesem Organisationsverzeichnis). Dafür sind Rechte im Tenant nötig, sonst die IT der Schule fragen.
2. Die Weiterleitungs-URI (Typ Web) eintragen.
3. Unter „Zertifikate & Geheimnisse“ ein **Client-Geheimnis** anlegen und den **Wert** sofort kopieren (er wird nur einmal angezeigt).
4. Anwendungs-ID (Client-ID), Verzeichnis-ID (Tenant) und Geheimnis in der Setup-Seite eintragen. Statt der Verzeichnis-ID geht
   auch eine Domain des Tenants oder `organizations` (alle Schul- und Arbeitskonten). Private Microsoft-Konten sind nicht erlaubt.

Beim Speichern trägt das Setup-Service die Anbieter in Keycloak ein und startet den Login-Service neu; danach erscheinen auf
der Login-Seite die Schaltflächen „Mit Google anmelden“ bzw. „Mit Microsoft anmelden“. Wird ein Anbieter abgeschaltet, bleibt er
in Keycloak erhalten (nur deaktiviert), die Verknüpfungen der Benutzer gehen nicht verloren.

Die erste Anmeldung eines Benutzers mit einem Google- oder Microsoft-Konto führt wie oben beschrieben zur einmaligen Bestätigung mit dem
LeTTo-Passwort. Rollen, Schule und Rechte kommen immer aus LeTTo. Die Vertrauensstellung der E-Mail-Adresse des Anbieters wird nie
für die Zuordnung verwendet.

## Variablen in der .env

| Variable | Bedeutung |
|---|---|
| `KEYCLOAK_DB_NAME`, `KEYCLOAK_DB_USER` | Datenbank und Benutzer in `letto-mysql` (Standard `keycloak`) |
| `KEYCLOAK_DB_PASSWORD` | Passwort des Datenbank-Benutzers (wird bei der Installation erzeugt) |
| `KEYCLOAK_ADMIN_USER`, `KEYCLOAK_ADMIN_PASSWORD` | Administrator der Admin-Konsole |
| `KEYCLOAK_LOGIN_CLIENT_SECRET` | Geheimnis des Clients `letto-login` für den Login-Service |
| `KEYCLOAK_PUBLIC_URL` | Adresse für den Browser, z. B. `https://letto.meine-schule.at/auth` (aus `SERVER_NAME` und `USE_HTTP`) |
| `KEYCLOAK_ADMIN_URL` | Adresse der Admin-Konsole (Standard `http://localhost:8480/auth`) |
| `SSO_GOOGLE_CLIENT_ID`, `SSO_GOOGLE_CLIENT_SECRET`, `SSO_GOOGLE_DOMAIN` | Google-App und erlaubte Workspace-Domain (Setup-Seite SSO-Anbieter) |
| `SSO_MICROSOFT_CLIENT_ID`, `SSO_MICROSOFT_CLIENT_SECRET`, `SSO_MICROSOFT_TENANT` | Microsoft-App und Tenant (Setup-Seite SSO-Anbieter) |
| `SSO_PROVIDERS` | aktive Anbieter auf der Login-Seite (setzt das Setup-Service, z. B. `google microsoft`) |
| `SSO_ENABLED` | `false` schaltet SSO für alle Benutzer aus: Login-Seite, Profil und Apps zeigen nichts davon (Standard `true`; Setup-Seite SSO-Anbieter, Abschnitt Allgemein) |
| `SSO_MFA_ENABLED` | `false` schaltet den zweiten Faktor für alle Benutzer aus (Standard `true`) |
| `LOGIN_REDIRECT_APP` | `false` = nach dem Login zum LeTTo-Server der Schule statt zur App (Standard `true`) |
| `SSO_RETURN_PREFIXES` | zusätzliche Rücksprungadressen für das Verknüpfen im Profil, z. B. das Schema der App (Komma-getrennt, siehe [Zweiter Faktor](Zweiter-Faktor/index.md)) |
| `KEYCLOAK_MEMORY_LIMIT` | Speicherlimit des Containers (Standard 1500M) |
| `PORT_KEYCLOAK` | lokaler Port der Admin-Konsole (Standard 8480) |
| `KEYCLOAK_IMAGE` | Image (Standard `quay.io/keycloak/keycloak:26.8.1`) |

Die Passwörter nicht weitergeben. Ändert sich `SERVER_NAME` oder `USE_HTTP`, muss `KEYCLOAK_PUBLIC_URL` angepasst
und Keycloak neu gestartet werden.

## Betrieb

* **Ressourcen:** etwa 0,8–1 GB Arbeitsspeicher im Betrieb, der Start dauert wenige Sekunden (beim allerersten Start
  kommt das Anlegen des Datenbankschemas dazu, etwa 35 Sekunden).
* **Update:** wie die anderen Services über die [Update-Konfiguration](../Update-Konfiguration/index.md); das Image ist
  in der yml-Datei fest auf eine Version gesetzt.
* **Datensicherung:** Keycloak speichert alles in der Datenbank `keycloak` von `letto-mysql`. Sie ist in der Sicherung
  des MySQL-Containers (siehe [Datenbanken](../Datenbanken/index.md)) enthalten – es gibt keine zweite Sicherung.
* **Log:** Container-Log über den Button **out** der Zeile `keycloak`, Datei `storage/log/keycloak/keycloak.log`.
* **Ausfall:** Fällt Keycloak aus, funktionieren die Anmeldungen mit Passwort weiter. Tests mit erzwungenem zweitem
  Faktor bleiben dann gesperrt, bis Keycloak wieder läuft.

## Datenschutz

Keycloak speichert Benutzername, die verifizierte E-Mail-Adresse und die eingerichteten Faktoren. In LeTTo wird zur
Verknüpfung nur die Kennung des Anbieters (`sub`) und die verifizierte E-Mail gespeichert. Auf der Login-Seite
steht dazu ein Hinweistext.

## siehe auch

* [Zweiter Faktor bei der Anmeldung über SSO](Zweiter-Faktor/index.md)
* [Registrierungsdaten für Google und Microsoft besorgen](Registrierungsdaten/index.md)
* [Services](../Services/index.md) – Statuszeile und Container-Zeilen
* [Update-Konfiguration](../Update-Konfiguration/index.md) – Service installieren, Updates
* [Proxy-Konfiguration](../Proxy-Konfiguration/index.md) – Datei `keycloak.conf`
* [Datenbanken](../Datenbanken/index.md) – Sicherung von `letto-mysql`
