# Registrierungsdaten für Google und Microsoft besorgen

Damit sich Benutzer mit ihrem Google- oder Microsoft-Konto bei LeTTo anmelden können, muss **jeder LeTTo-Server einmal beim
Anbieter registriert** werden. Der Anbieter vergibt dabei die Zugangsdaten, die im Setup-Service unter
**Konfiguration → SSO-Anbieter** eingetragen werden (siehe [Keycloak](../index.md)):

| Anbieter | Was Sie brauchen | Wo es im Setup eingetragen wird |
|---|---|---|
| Google | **Client-ID** und **Client-Geheimnis** | Abschnitt Google |
| Microsoft | **Anwendungs-ID (Client-ID)**, **Verzeichnis-ID (Tenant)** und **Client-Geheimnis (Wert)** | Abschnitt Microsoft |

> **Wer macht das?** Hat Ihre Schule einen **eigenen LeTTo-Server**, richtet der Administrator der Schule die Registrierung
> selbst ein – mit dieser Anleitung. Für Schulen auf den von LeTTo betriebenen Servern (**s1.letto.at**, **s2.letto.at**)
> übernimmt LeTTo die Registrierung, dort ist nichts zu tun.

Die Registrierung ist **kostenlos**. Sie wird pro Server einmal gemacht, nicht pro Benutzer. Benutzer geben später nur ihr
eigenes Passwort beim Anbieter ein, LeTTo sieht es nie.

## Vorbereitung: die Weiterleitungs-URI

Beide Anbieter wollen wissen, **wohin sie den Benutzer nach der Anmeldung zurückschicken** dürfen. Diese Adresse
(Weiterleitungs-URI, englisch *Redirect URI*) zeigt die Setup-Seite **Konfiguration → SSO-Anbieter** bei jedem Anbieter an. Sie
lautet:

| Anbieter | Weiterleitungs-URI |
|---|---|
| Google | `https://<Ihr-Server>/auth/realms/letto/broker/google/endpoint` |
| Microsoft | `https://<Ihr-Server>/auth/realms/letto/broker/microsoft/endpoint` |

`<Ihr-Server>` ist die öffentliche Adresse des LeTTo-Servers, genau so wie sie im Browser steht (z. B. `letto.meine-schule.at`).
Die Adresse muss **mit `https://`** erreichbar sein, Google akzeptiert für öffentliche Server kein `http://`. Am besten
kopieren Sie die Adresse direkt aus der Setup-Seite, jedes Zeichen muss stimmen (auch ein Schrägstrich am Ende zu viel oder zu wenig
führt zu einem Fehler).

Voraussetzung ist, dass **Keycloak** im Setup-Service bereits installiert ist (Update-Konfiguration → keycloak installieren).

## Google

Sie brauchen ein Google-Konto, mit dem Sie sich in der Google Cloud Console anmelden. Das kann auch ein normales Gmail-Konto
sein. Besser ist ein Konto, das auch später noch der Schule bzw. dem Betrieb des Servers zur Verfügung steht (z. B. ein
Funktionskonto der Schul-IT), damit die Registrierung nicht an einer einzelnen Person hängt.

Die Google Cloud Console verlangt beim ersten Mal die Zustimmung zu den Nutzungsbedingungen. Eine Kreditkarte ist für diese
Anmeldefunktion nicht nötig, es entstehen keine Kosten. Die Menüs der Konsole werden von Google gelegentlich umbenannt, die
Bezeichnungen unten können daher leicht abweichen.

### 1. Projekt anlegen

1. Öffnen Sie <https://console.cloud.google.com> und melden Sie sich an.
2. Oben neben dem Google-Cloud-Logo auf die Projektauswahl klicken → **Neues Projekt**.
3. Name z. B. `LeTTo Anmeldung`, **Erstellen**, danach das Projekt oben auswählen.

### 2. Zustimmungsbildschirm einrichten (Google Auth Platform)

Das ist der Bildschirm, den Benutzer bei der ersten Anmeldung sehen („LeTTo möchte auf Ihre Daten zugreifen“).

1. Menü → **APIs & Dienste → OAuth-Zustimmungsbildschirm** (in neueren Konsolen: **Google Auth Platform**), **Los geht’s**.
2. **App-Name** (z. B. `LeTTo`), **Support-E-Mail** (Ihre Adresse).
3. **Zielgruppe**:
   * **Extern**: Benutzer mit beliebigen Google-Konten, auch Gmail. Das ist der Standard für Schulen ohne Google Workspace.
   * **Intern**: nur Konten Ihrer eigenen Google-Workspace-Organisation. Diese Wahl gibt es nur, wenn Sie mit einem Workspace-Konto
     angemeldet sind. Dann sind Prüfung und Testnutzer nicht nötig.
4. **Kontaktdaten** (E-Mail für Benachrichtigungen) eintragen und die Richtlinien bestätigen, **Erstellen**.

Unter **Branding** können Sie Logo, Link zur Datenschutzerklärung und die **autorisierten Domains** (z. B. die Domain Ihres Servers)
eintragen. Für die ersten Tests ist das nicht nötig.

Unter **Datenzugriff** brauchen Sie **keine** zusätzlichen Bereiche (Scopes). LeTTo verwendet nur die Standardbereiche
`openid`, `email` und `profile`.

### 3. Anmeldedaten (OAuth-Client) erstellen

1. **APIs & Dienste → Anmeldedaten** (bzw. in der Google Auth Platform **Clients**) → **Anmeldedaten erstellen → OAuth-Client-ID**.
2. Anwendungstyp: **Webanwendung**. Name z. B. `LeTTo Server`.
3. **Autorisierte Weiterleitungs-URIs → URI hinzufügen**: die Google-Adresse aus der Setup-Seite einfügen
   (`https://<Ihr-Server>/auth/realms/letto/broker/google/endpoint`).
   Das Feld „Autorisierte JavaScript-Quellen“ bleibt leer.
4. **Erstellen**. Google zeigt jetzt die **Client-ID** (endet auf `.apps.googleusercontent.com`) und das **Clientschlüssel**
   (Client-Geheimnis, beginnt meist mit `GOCSPX-`). Kopieren Sie beide.

> **Das Geheimnis wie ein Passwort behandeln.** Nicht in E-Mails, Chats oder ein Repository schreiben. Wenn Sie die heruntergeladene
> JSON-Datei nicht brauchen, löschen Sie sie nach dem Eintragen im Setup. Ist das Geheimnis doch einmal bekannt geworden, kann es
> in der Console beim Client neu erzeugt und im Setup ersetzt werden.

### 4. Veröffentlichen

Solange der Zustimmungsbildschirm den Status **Testing** (Test) hat, dürfen sich nur Konten anmelden, die Sie unter **Zielgruppe →
Testnutzer** eingetragen haben (höchstens 100). Das ist ideal zum Ausprobieren. Für den Echtbetrieb stellen Sie den Status auf
**In production** (**App veröffentlichen**). Da LeTTo nur die Standardbereiche `openid`, `email` und `profile` verwendet,
ist keine aufwendige Prüfung durch Google nötig. Bei der **Intern**-Variante (Workspace) entfällt der Schritt.

### 5. Im Setup eintragen

Unter **Konfiguration → SSO-Anbieter → Google**: **Aktiv** anhaken, Client-ID und Geheimnis eintragen. Optional bei
**Erlaubte Domain** die Workspace-Domain der Schule (z. B. `schule.at`): Dann können sich nur Konten dieser Domain anmelden.
**Speichern** drücken. Das Setup trägt Google in Keycloak ein und startet den Login-Service neu. Auf der Login-Seite erscheint
„Mit Google anmelden“.

## Microsoft (Schul-Konto, Microsoft 365 / Entra ID)

Hier melden sich die Benutzer mit dem **Schul- oder Arbeitskonto** an (z. B. `vorname.nachname@schule.at` bei Microsoft 365). Private
Microsoft-Konten (outlook.com, hotmail.com) werden aus Sicherheitsgründen nicht zugelassen.

Die Registrierung findet im **Verzeichnis (Tenant) der Schule** statt. Was das ist und was Sie dafür von Ihrer IT brauchen,
steht im nächsten Abschnitt.

### Was ist ein Tenant?

Ein **Tenant** (deutsch etwa *Mandant* oder *Verzeichnis*) ist der abgetrennte Bereich, den eine Organisation bei Microsoft hat.
Wenn eine Schule Microsoft 365 / Office 365 einführt, bekommt sie genau **einen Tenant** in **Microsoft Entra ID** (früher
„Azure Active Directory“). In diesem Tenant liegen alle Benutzerkonten, Gruppen und die registrierten Anwendungen der Schule.

* Der Tenant hat eine eindeutige **Verzeichnis-ID** (eine GUID wie `1b2c3d4e-…`) und mindestens einen Domainnamen
  (`schule.onmicrosoft.com` plus die eigene Domain, z. B. `schule.at`).
* Die Konten `@schule.at` gehören zu diesem Tenant. Ein Konto in einem anderen Tenant (andere Schule) oder ein privates Konto
  gehört nicht dazu.
* LeTTo bindet den Anmelde-Anbieter **fest an einen Tenant**. So können sich nur Konten dieser Schule anmelden.

Ihre **Verzeichnis-ID** finden Sie im Entra Admin Center unter **Identität → Übersicht → Eigenschaften** (Feld
„Mandanten-ID“) oder in der App-Registrierung (siehe unten). Statt der ID kann im Setup auch eine **Domain des Tenants**
(z. B. `schule.at`) oder `organizations` (Konten aus beliebigen Schul- und Arbeits-Tenants) eingetragen werden. `common` und
`consumers` sind nicht erlaubt.

### Was Sie Ihre IT fragen müssen

Eine App-Registrierung kann nur anlegen, wer im Tenant dazu berechtigt ist. In vielen Schulen ist das nur die IT. Fragen Sie den
**Microsoft-365-Administrator** Ihrer Schule:

1. **Haben wir einen Microsoft-Entra-Tenant, und wie lautet die Verzeichnis-ID (Mandanten-ID)?** Jede Schule mit Office 365 hat einen.
2. **Darf ich (oder darf die IT) eine App-Registrierung anlegen?** Standardmäßig dürfen das alle Benutzer, viele Schulen
   schalten es aber ab („Benutzer können Anwendungen registrieren“ = Nein). Dann muss die IT die Registrierung selbst anlegen oder
   Ihnen die Rolle **Anwendungsentwickler** (Application Developer) zuweisen.
3. **Bitte eine App-Registrierung „LeTTo“ anlegen** mit
   * unterstützte Kontotypen: **nur Konten in diesem Organisationsverzeichnis** (einzelner Mandant),
   * Plattform **Web** mit der Weiterleitungs-URI `https://<Ihr-Server>/auth/realms/letto/broker/microsoft/endpoint`,
   * Berechtigung **Microsoft Graph → User.Read (delegiert)** (ist meist schon voreingestellt).
4. **Bitte einen Client-Geheimnis-Wert erzeugen** und mir mit der **Anwendungs-ID (Client-ID)** und der **Verzeichnis-ID** sicher
   zukommen lassen (nicht per unverschlüsselter E-Mail).
5. **Ist für diese Berechtigung eine Administratorzustimmung nötig?** Für `User.Read` meist nicht. Falls Ihre Schule Zustimmungen
   an Administratoren gebunden hat, muss die IT einmal „Administratorzustimmung erteilen“.
6. **Wie lange gilt das Geheimnis, und wer erneuert es?** Client-Geheimnisse laufen ab (höchstens 24 Monate). Dann muss ein neues
   erzeugt und im Setup eingetragen werden, sonst funktioniert die Anmeldung nicht mehr. Bitte den Ablauftermin notieren.
7. **Gibt es Richtlinien für bedingten Zugriff (Conditional Access)**, z. B. nur aus dem Schulnetz oder nur mit MFA? Diese gelten
   auch für die Anmeldung bei LeTTo.

### Schritte für die Registrierung (für IT oder berechtigte Benutzer)

1. Melden Sie sich im **Microsoft Entra Admin Center** (<https://entra.microsoft.com>) bzw. im Azure-Portal an.
2. **Identität → Anwendungen → App-Registrierungen → Neue Registrierung**.
3. **Name**: `LeTTo`. **Unterstützte Kontotypen**: *Nur Konten in diesem Organisationsverzeichnis*.
4. **Umleitungs-URI**: Plattform **Web**, Adresse aus der Setup-Seite. **Registrieren**.
5. Auf der Übersichtsseite der App stehen **Anwendungs-ID (Client)** und **Verzeichnis-ID (Mandant)**. Kopieren Sie beide.
6. **Zertifikate & Geheimnisse → Neuer geheimer Clientschlüssel**: Beschreibung `LeTTo`, Gültigkeit wählen (z. B. 24 Monate).
   Kopieren Sie sofort den **Wert**. Er wird nur **einmal** angezeigt. Die Spalte „Geheime ID“ ist **nicht** das Geheimnis.
7. Unter **API-Berechtigungen** sollte **Microsoft Graph → User.Read** (delegiert) stehen. Eine weitere Berechtigung ist nicht nötig.
8. Im Setup unter **Konfiguration → SSO-Anbieter → Microsoft**: **Aktiv**, Client-ID, **Tenant** (Verzeichnis-ID) und Geheimnis eintragen,
   **Speichern**.

## Wenn etwas nicht funktioniert

| Meldung | Ursache und Lösung |
|---|---|
| Google: `redirect_uri_mismatch` | Die Weiterleitungs-URI im Google-Client stimmt nicht genau mit der Adresse aus dem Setup überein (http/https, Server-Name, Schrägstrich am Ende). Bei Änderungen dauert es manchmal einige Minuten, bis Google sie übernimmt. |
| Google: `access_denied` / „App wurde nicht überprüft“ | Status **Testing**: Das Konto ist nicht als Testnutzer eingetragen, oder die App muss veröffentlicht werden. Die Warnung „nicht überprüft“ kann bei einer Anmeldung durch **Erweitert → Weiter** übergangen werden. |
| Google: `invalid_client` | Client-ID oder Geheimnis sind falsch eingetragen (Leerzeichen, abgeschnitten) oder der Client wurde gelöscht. |
| Google: Konto wird abgewiesen, obwohl die Anmeldung klappt | Im Setup ist bei **Erlaubte Domain** eine Domain eingetragen, die das Konto nicht hat. |
| Microsoft: `AADSTS50011` | Die Umleitungs-URI der App-Registrierung stimmt nicht mit der Adresse aus dem Setup überein. |
| Microsoft: `AADSTS7000215` / `invalid_client_secret` | Es wurde die „Geheime ID“ statt des **Werts** eingetragen, oder das Geheimnis ist abgelaufen. |
| Microsoft: `AADSTS700016` | Anwendungs-ID falsch oder die App liegt in einem anderen Tenant als eingetragen. |
| Microsoft: `AADSTS65001` | Es fehlt die Zustimmung zur Berechtigung: Administratorzustimmung erteilen lassen. |
| Microsoft: `AADSTS50020` | Das Konto gehört nicht zum eingetragenen Tenant (z. B. privates Konto oder anderer Schul-Tenant). |
| Nach der Anmeldung erscheint die LeTTo-Verknüpfungsseite | Normal bei der ersten Anmeldung: einmal mit LeTTo-Benutzername und -Passwort bestätigen. Danach genügt die Anmeldung mit dem Konto des Anbieters. |
| Auf der Login-Seite fehlt der Button | Der Anbieter ist im Setup nicht aktiv oder Client-ID/Geheimnis fehlen. Beim Speichern prüft das Setup die Eingaben und zeigt eine Meldung. Danach den Login-Service neu starten lassen (geschieht beim Speichern automatisch). |

Weitere Informationen zum Ablauf der Anmeldung, zum gemeinsamen Abmelden und zu den Variablen in der `.env` stehen auf der Seite
[Keycloak](../index.md).
