# Zweiter Faktor (2FA) bei der Anmeldung über SSO

Wer sich mit Google oder Microsoft bei LeTTo anmeldet ([Anmeldung über SSO](../index.md)), kann zusätzlich einen **zweiten Faktor** verlangen:
einen Einmalcode aus einer Authenticator-App (TOTP, z. B. Microsoft Authenticator, Google Authenticator, FreeOTP). Der Code kommt **nach** der
Anmeldung beim Anbieter. Er ersetzt sie nicht.

> **Stand:** Version 1.3, in Entwicklung. Der zweite Faktor gilt **nur für den Weg über SSO**. Die Anmeldung mit LeTTo-Benutzername und Passwort
> bleibt wie sie ist, dort gibt es noch keinen zweiten Faktor. Ein erzwungener zweiter Faktor beim Start eines Tests folgt in einem späteren Schritt.

> **Zentraler Schalter:** Der Administrator des Servers kann den zweiten Faktor (und SSO insgesamt) im Setup-Service für alle Benutzer aus- und einschalten
> (Konfiguration → SSO-Anbieter → Allgemein, siehe [Keycloak](../index.md)). Ist er aus, gibt es in Profil und App keine Einstellung dazu und es wird kein Code verlangt.

## Für Benutzer

### Zweiten Faktor einschalten

Der zweite Faktor wird im **Profil** ein- und ausgeschaltet (im bisherigen Main über das
Schlüssel-Symbol in der Werkzeugleiste, Seite „Anmeldung und Sicherheit“; in der LeTTo-App folgt dieselbe Funktion im Profil):

1. Zuerst muss ein SSO-Konto verknüpft sein (Abschnitt „Anmeldung über SSO“, Knopf **Mit Google verknüpfen** bzw. **Mit Microsoft verknüpfen**).
2. **Zweiten Faktor verlangen** wählen.
3. Beim **nächsten** Login über SSO zeigt Keycloak nach der Anmeldung beim Anbieter die Einrichtung:
   * Authenticator-App öffnen und den **QR-Code** scannen (oder den angezeigten Schlüssel eintippen),
   * den angezeigten **Einmalcode** eingeben,
   * einen **Gerätenamen** vergeben (z. B. „Handy“), damit man den Faktor später erkennt.
4. Danach fragt jeder SSO-Login nach der Anmeldung beim Anbieter nach dem aktuellen Code. Der Code wechselt alle 30 Sekunden und gilt nur einmal.

**Ausschalten:** im Profil **Zweiten Faktor nicht mehr verlangen**. Der eingerichtete Faktor bleibt gespeichert, bei erneutem Einschalten muss er
nicht noch einmal eingerichtet werden.

### Handy verloren oder Code geht nicht

* Wiederherstellungscodes gibt es in dieser Version noch nicht. Wenden Sie sich an den **Administrator Ihrer Schule**, er setzt den zweiten Faktor zurück
  (siehe unten). Danach richten Sie ihn bei der nächsten Anmeldung neu ein.
* Wenn der Code abgelehnt wird, prüfen Sie die Uhrzeit des Handys (automatische Zeit einschalten) und warten Sie auf den nächsten Code.

## Für Administratoren der Schule

### Zweiten Faktor eines Benutzers zurücksetzen

Der Administrator der Schule kann für **Benutzer seiner Schule**

* den **zweiten Faktor zurücksetzen**: Alle Faktoren des Benutzers (Authenticator-App, Wiederherstellungscodes, Passkeys) werden in Keycloak entfernt.
  Die Einstellung „zweiten Faktor verlangen“ bleibt unverändert, der Benutzer richtet ihn bei der nächsten Anmeldung wie beim ersten Mal neu ein;
* alle **SSO-Verknüpfungen lösen**, z. B. wenn der Benutzer sein Google-Konto verloren hat. Er bestätigt dann beim nächsten SSO-Login wieder
  einmal mit seinem LeTTo-Passwort.

Beides geschieht über die Administrator-Schnittstelle des Login-Service (Token eines Administrators im Header `Authorization`):

| Aktion | Aufruf |
|---|---|
| Zustand eines Benutzers (Verknüpfungen, zweiter Faktor) | `GET /login/api/admin/sso_admin_info?username=…` |
| Alle Verknüpfungen lösen | `POST /login/api/admin/sso_admin_unlink` mit `{"username":"…"}` |
| Zweiten Faktor zurücksetzen | `POST /login/api/admin/sso_admin_mfa_reset` mit `{"username":"…"}` |

Die Oberfläche dafür entsteht in der LeTTo-App (Benutzerverwaltung). Benutzer und Lehrer ohne Administratorrecht bekommen auf diese Aufrufe
**403**. Ein Administrator kann nur Benutzer der **eigenen Schule** verwalten. Jede Aktion steht im Log des Login-Service.

### Notfall: Zurücksetzen in Keycloak

Ist der Login-Service nicht verfügbar, kann der Server-Administrator den Faktor in der Keycloak-Konsole entfernen
(`http://127.0.0.1:8480/auth`, nur am Server erreichbar, siehe [Erreichbarkeit und Sicherheit](../index.md)):
Realm `letto` → Users → Benutzer wählen → Credentials → den Eintrag „OTP“ löschen.

## Wie es funktioniert

* In Keycloak gibt es den Ablauf **`letto-postbroker`**. Er läuft nach der Anmeldung beim externen Anbieter und kennt zwei Stufen:
  Stufe 1 gilt mit dem Anbieter-Login, Stufe 2 verlangt zusätzlich den Code und richtet ihn beim ersten Mal ein.
  Das Setup-Service legt den Ablauf an und trägt ihn bei jedem Anbieter ein (Setup → Konfiguration → SSO-Anbieter → Speichern). Auf einer
  bestehenden Installation also einmal **Speichern** drücken.
* Verlangt ein Benutzer den zweiten Faktor, fordert der Login-Service nach der Anmeldung beim Anbieter bei Keycloak die Stufe 2 an
  (`acr_values=mfa`). Er prüft **selbst** am ID-Token, dass die Stufe erreicht wurde und dass es dasselbe Konto ist. Ein Token ohne
  Stufe 2 wird abgewiesen. Der Login-Service verlässt sich dabei nicht darauf, dass Keycloak den Code abgefragt hat.
* Ohne die Einstellung „zweiten Faktor verlangen“ kommt kein Code. Ein Konto ohne lokales Passwort kann nie „nur mit Code“ anmelden,
  weil der Anbieter-Login immer vorausgeht.
* Die Einstellung je Benutzer liegt im Login-Service (Mongo, Sammlung `ssousersettings`), die Faktoren selbst in Keycloak.
  Sie sind im MySQL-Backup (Datenbank `keycloak`) enthalten.

## Hinweise und Grenzen

* **Erste Einrichtung:** Solange noch kein Faktor eingerichtet ist, kann jeder mit Zugang zum Konto beim Anbieter den ersten Faktor einrichten
  (der erste Benutzer gewinnt). Der Schutz beginnt also, sobald das Konto seinen Faktor hat. Lehrer und Administratoren sollten ihn deshalb gleich
  bei der Einführung einrichten.
* **Wiederherstellungscodes** und **Passkeys** sind in Keycloak vorhanden, aber noch nicht eingerichtet und nicht erprobt.
* Der Code wird bei jeder Anforderung der Stufe 2 neu verlangt. Im Alltag ist das jeder SSO-Login eines Benutzers mit eingeschaltetem zweiten Faktor.
* Ohne den Schalter oder bei ausgeschaltetem SSO ändert sich nichts an der bisherigen Anmeldung.

## Rücksprungadressen (für die App)

Beim Verknüpfen im Profil leitet der Login-Service nach der Anmeldung beim Anbieter zu einer Adresse zurück, die die Anwendung mitgibt.
Erlaubt sind Adressen auf dem Server der Installation. Weitere (z. B. das Adressschema der nativen App) trägt der Server-Administrator in der `.env`
ein: `SSO_RETURN_PREFIXES`, mehrere Präfixe mit Komma getrennt (ein Schema mit `://`, eine Adresse mit `/` am Ende). Alles andere wird abgelehnt,
damit der Login-Service nicht als offene Weiterleitung missbraucht werden kann.

## siehe auch

* [Keycloak (SSO)](../index.md): Installation, Anmeldung über SSO, Variablen
* [Registrierungsdaten für Google und Microsoft besorgen](../Registrierungsdaten/index.md)
