# and

[Zurück zu Berechnungen](../../../index.md)

## Name

`and` – Infix-Operatoren.

## Detaillierte Beschreibung

Bitweise oder logisches UND. Die Parserpriorität beträgt **21**; die Bindung ist infix.

### Anwendung und Besonderheiten

Die Operatoren des internen Parsers sind teilweise anders als in Maxima definiert. Für eine symbolische Maxima-Berechnung sind gegebenenfalls die entsprechenden Funktionen zu verwenden.

Mit Ganzzahlen erfolgt eine bitweise Verknüpfung, mit booleschen Werten eine logische Verknüpfung. Die Java-Implementierung verwendet für Ganzzahlen BigInteger. Numerische Werte anderer Art können den Fehler „Bitweise oder logische Operation nicht möglich!“ auslösen.

## Syntax

```text
x and y
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Operand bzw. Ausdruck (links). | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |
| y | Operand bzw. Ausdruck (rechts). | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| 13 and 10 | 8 |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

[Zurück zu Berechnungen](../../../index.md)
