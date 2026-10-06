# number

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`number` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Erzwingt die numerische Auswertung aller numerisch berechenbaren Teile. Bleibt bei einem weiterhin symbolischen Ergebnis als Funktion erhalten.

## Syntax

```text
number(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `number(2+3+x)`  
**Ergebnis:** number(5+x)

| Ausdruck | Ergebnis |
| --- | --- |
| number(2+3+x) | number(5+x) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NumberOpt`.

[Zurück zu Berechnungen](../../../index.md)
