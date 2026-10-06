# tailstring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`tailstring` – Stringfunktionen.

## Detaillierte Beschreibung

liefert den letzten Teil eines Strings teilstring(tailstring,zeichenanzahl)

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
tailstring(string, length)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `length` | Parameter der Funktion. | String / Ganzzahl | nein |

## Beispiele

**Beispiel:** `tailstring("abcdefg",2)`  
**Ergebnis:** "fg"

| Ausdruck | Ergebnis |
| --- | --- |
| tailstring("abcdefg",2) | "fg" |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=5026)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `TailString`.

[Zurück zu Berechnungen](../../../index.md)
