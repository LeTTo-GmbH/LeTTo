# replacestring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`replacestring` – Stringfunktionen.

## Detaillierte Beschreibung

Ersetzt alle Vorkommen einer Zeichenkette in einem String durch eine andere Zeichenkette.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
replacestring(string, sold, snew)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `sold` | Parameter der Funktion. | String | nein |
| `snew` | Parameter der Funktion. | String | nein |

## Beispiele

**Beispiel:** `replacestring("abcdefg","bc","xy")`  
**Ergebnis:** "axydefg"

| Ausdruck | Ergebnis |
| --- | --- |
| replacestring("abcdefg","bc","xy") | "axydefg" |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=5027)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `ReplaceString`.

[Zurück zu Berechnungen](../../../index.md)
