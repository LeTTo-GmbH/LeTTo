# lopt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`lopt` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {= wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert.

## Syntax

```text
lopt(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `lopt(x+3)`  
**Ergebnis:** lopt(x+3)

| Ausdruck | Ergebnis |
| --- | --- |
| lopt(x+3) | lopt(x+3) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3493)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateViewFunctions.java`, Klasse `LOpt`.

[Zurück zu Berechnungen](../../../index.md)
