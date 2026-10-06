# parser

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`parser` – Spezialfunktionen LeTTo.

## Detaillierte Beschreibung

Markierungsfunktion für Ausdrücke, die von Maxima unverändert an den internen Parser weitergereicht werden sollen. Im internen Parser selbst wird lediglich der einzelne Parameter ausgewertet.

## Syntax

```text
parser(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `parser(x+1)`  
**Ergebnis:** x+1

| Ausdruck | Ergebnis |
| --- | --- |
| parser(x+1) | x+1 |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NoOp`.

[Zurück zu Berechnungen](../../../index.md)
