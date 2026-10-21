# Setup-Service: E-Mail

![Email Konfiguration](email-konfiguration.png)

Aufruf: Menü **Konfiguration → E-Mail** auf der [Hauptseite](../Hauptseite/index.md).

Hier wird der Mailserver (SMTP) eingestellt, über den alle LeTTo-Services Mails verschicken – z. B. beim Zurücksetzen
von Passwörtern. Mit einer Test-Mail lässt sich prüfen, ob die Einstellungen stimmen.

## Buttons oben

| Button | Wirkung |
|---|---|
| reload | Einstellungen neu aus der `.env` laden (nicht gespeicherte Eingaben gehen verloren) |
| save | Einstellungen in der `.env` speichern |
| Abbruch | zurück zur Hauptseite, ohne zu speichern |

## Mailserver

| Feld | Variable in der `.env` | Bedeutung |
|---|---|---|
| host | `spring_mail_host` | Name des SMTP-Servers, z. B. `smtp.meine-schule.at` |
| Port | `spring_mail_port` | Port des SMTP-Servers, meist 465 (SSL) oder 587 (STARTTLS) |
| Benutzername | `spring_mail_username` | Anmeldename am SMTP-Server |
| password | `spring_mail_password` | Passwort am SMTP-Server (verdeckt, mit dem Auge-Symbol sichtbar) |
| authentication enabled | `spring_mail_properties_mail_smtp_auth` | Anmeldung am SMTP-Server verwenden |
| TTLS enabled | `spring_mail_properties_mail_smtp_starttls_enable` | Verbindung mit STARTTLS verschlüsseln |
| ssl enabled | `spring_mail_properties_mail_smtp_ssl_enable` | Verbindung mit SSL verschlüsseln |
| no reply address | `spring_mail_address_noreply` | Absenderadresse für Mails, auf die nicht geantwortet werden soll |
| reply address | `spring_mail_address_reply` | Adresse für Antworten |

Die anderen Services lesen diese Werte beim Start. Nach einer Änderung müssen sie neu gestartet werden
(z. B. `login-service` im Tab [Services](../Services/index.md)).

## Test-Email

| Element | Beschreibung |
|---|---|
| send testmail to | Empfänger der Test-Mail (Vorgabe: Admin-E-Mail des Servers) |
| testmail subject | Betreff |
| testmail text | Text der Mail |
| sende Test-Email | sendet die Test-Mail mit den **eingegebenen** Werten, auch wenn sie noch nicht gespeichert sind |
| sende mit gespeicherter Konfiguration | sendet die Test-Mail mit den **gespeicherten** Werten aus der `.env` |
| sende mit gespeicherter Konfiguration als html | wie oben, aber als HTML-Mail |

Die Meldung „Email wurde gesendet“ bedeutet nur, dass das Senden angestoßen wurde. Ob die Mail wirklich ankommt, zeigt
erst das Postfach des Empfängers.

Zurück zur Übersicht: [Setup-Service](../index.md)
