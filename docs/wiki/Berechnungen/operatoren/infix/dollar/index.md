# $

[Zurück zu Berechnungen](../../../index.md)

## Name

`$` – Infix-Operatoren.

## Detaillierte Beschreibung

Trennzeichen zwischen mehreren Berechnungen. Die Parserpriorität beträgt **1**; die Bindung ist infix.

### Anwendung und Besonderheiten

Die Operatoren des internen Parsers sind teilweise anders als in Maxima definiert. Für eine symbolische Maxima-Berechnung sind gegebenenfalls die entsprechenden Funktionen zu verwenden.

Trennt mehrere Berechnungsanweisungen. Beispiel: `x:2; y:x+3` weist y den Wert 5 zu.

## Syntax

```text
x:2$ y:x+3
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruecke | Durch das Zeichen getrennte Ausdrücke bzw. Anweisungen. | Ausdruck | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| `x:2$ y:x+3` | Abhängig von den Operanden; siehe Beschreibung. |

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
