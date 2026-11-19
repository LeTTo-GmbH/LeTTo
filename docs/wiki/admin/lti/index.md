# LTI-Konfiguration

Die Seite **LTI-Verwaltung** konfiguriert, wie Benutzer und Kurse/Klassen beim Zugriff über LTI automatisch in LeTTo angelegt und zugeordnet werden.

![LTI-Verwaltung in der LeTTo-App](LTI-config.jpg)

## Schüler / Studierende

Für Lernende stehen zwei getrennte Optionen zur Verfügung:

- **Benutzer automatisch anlegen** – ein noch nicht vorhandener Benutzer wird beim ersten LTI-Zugriff automatisch am LeTTo-Server angelegt.
- **Automatisch in Kurs oder Klasse einschreiben** – der Benutzer wird dem über LTI verwendeten Kurs bzw. der Klasse zugeordnet.

## Vortragende

Für Professoren, Lehrer, Assistenten und weitere Vortragende können folgende Automatismen aktiviert werden:

- **Benutzer automatisch anlegen** – neue Vortragende werden als LeTTo-Benutzer erzeugt.
- **Kurse / Klassen automatisch anlegen** – ein über LTI aufgerufener, noch nicht vorhandener Kurs bzw. eine Klasse wird automatisch erstellt.
- **In bestehende Kurse einschreiben** – Vortragende können sich in bestehende Kurse/Klassen einschreiben und verwenden dabei einen eigenen Kursbereich.
- **Bestehendem Kurs direkt zuordnen** – Vortragende werden dem vorhandenen Kurs bzw. der Klasse direkt zugeordnet und verwenden den gemeinsamen Kursbereich.

## Eindeutiger Bezeichner für Benutzer

Diese Einstellung bestimmt, anhand welcher LTI-Information LeTTo einen Benutzer wiedererkennt. Zur Auswahl stehen:

- **Moodle-Name**
- **E-Mail-Adresse**
- **Vollständiger Name**

Die Wahl sollte zur Benutzerverwaltung der angebundenen Lernplattform passen, damit bei wiederholten LTI-Aufrufen keine unerwünschten Doppelkonten entstehen.

## Hinweise zum Verhalten

- **Schüler brauchen einen vorhandenen Kurs:** „Benutzer automatisch anlegen“ und „In Kurs einschreiben“ wirken nur, wenn der Kurs in LeTTo schon existiert
  (über die Moodle-Kurs-ID, die Klassen-ID oder einen Test gefunden). Den Kurs legt am einfachsten ein Vortragender an, der die Aktivität zuerst startet
  (Option „Kurse / Klassen automatisch anlegen“).
- **Neue Vortragende werden deaktiviert angelegt** und müssen von einem Administrator freigeschaltet werden, bevor die Anmeldung gelingt.
- **Archivierte oder deaktivierte Benutzer** können sich über LTI nicht anmelden; es wird auch kein neuer Benutzer mit demselben Namen angelegt
  (siehe [Archivierte Benutzer](../../Administration/Setup-Service/Archivierte-Benutzer/index.md)).
- Der Parameter `school` (Schulkürzel) muss im externen Tool von Moodle gesetzt sein, siehe [LTI-Service](../LTIVerbindung/index.md#fehlersuche).

## Speichern und neu laden

**Speichern** überträgt die aktuelle schulbezogene Konfiguration. **Neu laden** verwirft nicht gespeicherte Änderungen und liest die Daten erneut vom Backend. Kann die Konfiguration nicht vollständig geladen werden, zeigt die Seite einen Warnhinweis und verwendet zunächst Standardwerte.
