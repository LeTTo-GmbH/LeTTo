# Setup-Service: Benutzer

![Benutzer](benutzer.png)

Aufruf: Menü **Verwaltung → Benutzer** auf der [Hauptseite](../Hauptseite/index.md).

Die Seite zeigt, wer gerade an LeTTo angemeldet ist – über alle Schulen des Servers und auch im Setup selbst – und wer
sich in der letzten Stunde abgemeldet hat. Einzelne Benutzer können abgemeldet werden, z. B. vor einem Update.

## Buttons in der Kopfzeile

| Button | Wirkung |
|---|---|
| Zurück | zurück zur Hauptseite |
| Aktualisieren | Liste neu laden |
| LDAP/AD Login | öffnet die [LDAP/AD-Konfiguration](../LDAP-AD/index.md) |
| Benutzer suchen | öffnet die [Benutzersuche](../Benutzersuche/index.md) |
| Neuer Benutzer | öffnet [Neuer Benutzer](../Benutzer-anlegen/index.md): Benutzer an einer Schule anlegen |
| Archivierte Benutzer | öffnet die Liste der [archivierten Benutzer](../Archivierte-Benutzer/index.md) mit Wiederherstellen |

## Angemeldete Benutzer

| Spalte | Bedeutung |
|---|---|
| Benutzername, Schulkürzel, E-Mail, ID | der Benutzer und seine Schule (`config` = Setup-Service) |
| Letzter Logout, Letzter Logout durch Timeout | Zeitpunkt der letzten Abmeldung bzw. automatischen Abmeldung |
| Sessions/Tokens | Anzahl der offenen Sitzungen und gültigen Tokens |
| IP:Ablauf | IP-Adresse und verbleibende Gültigkeit |
| Rollen | z. B. Admin, Teacher, Student, Global |
| Aktion | **Abmelden** meldet den Benutzer sofort ab (ohne Rückfrage); **Benutzer** öffnet die Benutzerdetails |
| Fingerprint, Service, Infos, User-Agent | Kennung des Browsers, verwendeter Service und Browser |

## Innerhalb der letzten Stunde abgemeldete Benutzer

Benutzername, Schulkürzel, E-Mail, ID, letzter Logout (auch durch Timeout) und letzter Login der Benutzer, die sich in
der letzten Stunde abgemeldet haben.

## Benutzerdetails

![Benutzerdetails](benutzerdetails.png)

Die Benutzerdetails öffnen sich mit **Benutzer** hier oder in der [Benutzersuche](../Benutzersuche/index.md).

| Element | Beschreibung |
|---|---|
| Zurück | in der Kopfzeile: zurück zur vorigen Seite; bei ungespeicherten Änderungen mit Rückfrage |
| Aktualisieren | in der Kopfzeile: Daten neu laden |
| Speichern | bleibt auf der Seite; speichert die Änderungen über den Data-Service in der Datenbank der Schule (nur bei Benutzern einer Schule); bestätigt der Data-Service das Speichern nicht, erscheint eine Fehlermeldung |
| Archivieren | archiviert den Benutzer nach einer Rückfrage (siehe [Archivierte Benutzer](../Archivierte-Benutzer/index.md)); der Button fehlt bei Administratoren |
| Bestätigen und speichern | erscheint, wenn eine **sicherheitsrelevante Änderung** vorliegt (siehe unten) |
| Benutzerdaten | Stammdaten des Benutzers: Schulkürzel, User-ID, Benutzername, Vor- und Nachname, Active-Directory-Name, Personalnummer, Sokrates-ID, E-Mail, Geburtsdatum, Telefon, Sprache, die Rollen (Student, Lehrer/Vortragender, Administrator, globaler Administrator), Lizenz-Einstellungen und Abo-Einstellungen. Im Feld **Passwort** kann ein neues Passwort gesetzt werden – leer lassen, wenn es unverändert bleiben soll. Beim Setup-Benutzer `admin` gibt es nur den Benutzernamen |
| Tokens | gültige Anmelde-Tokens mit Erstellt, Ablauf, gültig, Issuer, Audience, Benutzername, ursprünglicher Benutzer, Schulkürzel, Rollen, Session-ID und Token |
| Sessions | Sitzungen des Benutzers mit Anmeldung, Abmeldung, IP-Adresse, Service und Browser; **Abmelden** beendet eine aktive Sitzung, **löschen** entfernt eine beendete (ohne Rückfrage), die eigene Sitzung ist als „aktuell“ markiert |

### Kontrolliertes Bearbeiten

Das Speichern prüft die Eingaben und schützt Zugang und Rechte:

* **Eingaben:** Der Login muss gültig sein (Buchstaben, Ziffern und `.` `_` `-` `@` `+`) und in der Schule **noch frei** (auch Logins archivierter Benutzer gelten als vergeben),
  die E-Mail-Adresse muss ein gültiges Format haben, ein neues Passwort braucht mindestens 8 Zeichen. Bei einem Fehler wird nichts gespeichert und die Eingaben bleiben im Formular.
* **Bestätigung:** Änderungen von **Login, Administrator, globalem Administrator, Lehrer, Schüler, Deaktiviert und Passwort** werden erst nach **Bestätigen und speichern** übernommen.
  Die Seite listet dazu die Änderungen (zum Beispiel „Administrator: false → true“) und speichert noch nichts. Andere Änderungen (Name, E-Mail …) werden sofort gespeichert.
* **Protokoll:** Jede gespeicherte Änderung steht im Änderungsprotokoll.

## Änderungsprotokoll {#aenderungsprotokoll}

Die Benutzerverwaltung des Setup schreibt jede Änderung in eine Protokolldatei auf dem Server:
`/opt/letto/docker/storage/setup/benutzer-protokoll/benutzer-aenderungen-<Jahr>-<Monat>.log` (eine Datei je Monat, sie bleibt bei einem Update erhalten).
Eine Zeile enthält Zeitpunkt, den angemeldeten Administrator des Setup, die Aktion (`anlegen`, `aendern`, `archivieren`, `wiederherstellen`), Schule, Benutzer-ID, Login
und die geänderten Felder als `Feld: alt -> neu`. **Passwörter und andere Geheimnisse stehen nie im Protokoll**, nur der Hinweis „geändert“.
Die letzten Einträge zeigt die Seite [Neuer Benutzer](../Benutzer-anlegen/index.md).

Zurück zur Übersicht: [Setup-Service](../index.md)
