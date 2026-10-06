# qopt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`qopt` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Im Maximafeld wird alles innerhalb der Funktion nicht ausgewertet und die Funktion bleibt erhalten, bei der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. Anwendung findet die Funktion bei boolschen Fragen und Folgefehlerbehandlung.

## Syntax

```text
qopt(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `qopt(x+3)`  
**Ergebnis:** qopt(x+3)

| Ausdruck | Ergebnis |
| --- | --- |
| qopt(x+3) | qopt(x+3) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateViewFunctions.java`, Klasse `QOpt`.

[Zurück zu Berechnungen](../../../index.md)
