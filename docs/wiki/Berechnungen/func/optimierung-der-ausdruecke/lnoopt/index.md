# lnoopt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`lnoopt` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {= wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nicht mehr optimiert.

## Syntax

```text
lnoopt(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `lnoopt(x+3+2)`  
**Ergebnis:** lnoopt(x+5)

| Ausdruck | Ergebnis |
| --- | --- |
| lnoopt(x+3+2) | lnoopt(x+5) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateViewFunctions.java`, Klasse `LNoOpt`.

[Zurück zu Berechnungen](../../../index.md)
