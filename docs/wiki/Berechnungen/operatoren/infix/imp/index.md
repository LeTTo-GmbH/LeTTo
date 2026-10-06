# imp

[Zurück zu Berechnungen](../../../index.md)

## Name

`imp` – Infix-Operatoren.

## Detaillierte Beschreibung

Bitweise oder logisches impliziert IMP. Die Parserpriorität beträgt **23**; die Bindung ist infix.

### Anwendung und Besonderheiten

Die Operatoren des internen Parsers sind teilweise anders als in Maxima definiert. Für eine symbolische Maxima-Berechnung sind gegebenenfalls die entsprechenden Funktionen zu verwenden.

Die aktuelle Java-Implementierung berechnet bei Ganzzahlen `(~a) | b` mit BigInteger ohne feste Bitbreite. Daher liefert `bimp(13,10)` den Wert **-5**, nicht 8. Bei booleschen Parametern implementiert der Code derzeit `!(a || b)` (NOR), etwa `bimp(false,false) = true`; das entspricht nicht der üblichen Implikation `!a || b`. Der Name beschreibt die beabsichtigte Operation, diese Angaben beschreiben den mitgelieferten Code.

## Syntax

```text
x imp y
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Operand bzw. Ausdruck (links). | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |
| y | Operand bzw. Ausdruck (rechts). | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| 13 imp 10 | -5 |

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
