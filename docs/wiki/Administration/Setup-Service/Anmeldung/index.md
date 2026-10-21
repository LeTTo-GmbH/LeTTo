# Setup-Service: Anmeldung

![Anmeldung am Setup-Service](anmeldung.png)

Die Anmeldeseite ist unter `https://<server>/config` erreichbar (genau: `/config/open/loginletto`). Ins Setup dürfen nur
Benutzer mit **globalen Administratorrechten**.

## Felder und Buttons

| Element | Beschreibung |
|---|---|
| Benutzername | `admin` für den lokalen Setup-Administrator oder ein LeTTo-Benutzer mit globaler Rolle (z. B. `adminglobal<schulkürzel>`) |
| Passwort | Passwort des Benutzers; mit dem Auge-Symbol wird es sichtbar |
| Anmelden | meldet an und öffnet die [Hauptseite](../Hauptseite/index.md) mit dem Tab [Services](../Services/index.md) |
| Sprache | Sprache der Oberfläche (Deutsch, English, Français, Español); wird im Browser gespeichert |

## Wer sich anmelden kann

* **`admin`**: Das Passwort ist `ADMIN_PASSWORD` aus der `.env` (`/opt/letto/docker/compose/letto/.env`), es wird bei der
  Installation festgelegt. Solange keine Schule eingerichtet ist, kann sich nur `admin` anmelden.
* **globale LeTTo-Administratoren**: Die Anmeldung läuft über den Login-Service (`letto-login`), dort wirkt auch ein
  eingerichteter [LDAP/AD-Login](../LDAP-AD/index.md). Benutzer ohne globale Rolle werden abgewiesen
  („Anmeldung fehlgeschlagen – für das Setup sind globale Administratorrechte nötig!“).

## Meldungen

| Meldung | Bedeutung |
|---|---|
| Benutzername oder Passwort falsch! | Anmeldedaten stimmen nicht |
| Anmeldung fehlgeschlagen – für das Setup sind globale Administratorrechte nötig! | gültiger Benutzer, aber kein globaler Administrator |
| Ihre Sitzung ist abgelaufen (z. B. nach einem Neustart des Setups). Bitte melden Sie sich neu an. | nach einem Neustart oder Update des Setup-Containers bzw. nach einem Timeout |
| Sie wurden abgemeldet. | nach **Abmelden** |

Nach jedem Neustart des Setup-Containers (z. B. durch ein Update) ist die Sitzung ungültig; der nächste Klick führt
wieder hierher. Auch bei einem Fehler in einer Seite (außer „Seite nicht gefunden“) wird man aus Sicherheitsgründen
abgemeldet. Alle Anmeldungen und Fehlversuche stehen im Log des Setups.

Zurück zur Übersicht: [Setup-Service](../index.md)
