# parseip

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`parseip` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

Wandelt einen String mit einer IP-Adresse in einen Long-Wert

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
parseip(ipAdresse)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ipAdresse` | Parameter der Funktion. | String | nein |

## Beispiele

**Beispiel:** `parseip("91.119.43.5")`  
**Ergebnis:** 1534536453

| Ausdruck | Ergebnis |
| --- | --- |
| parseip("91.119.43.5") | 1534536453 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3502)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `ParseIP`.

[Zurück zu Berechnungen](../../../index.md)
