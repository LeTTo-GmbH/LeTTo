# %

[Zurück zu Berechnungen](../../../index.md)

## Name

`%` – Prefix-Operatoren.

## Detaillierte Beschreibung

Prefix für Namen, welche als Konstante definiert sind. Die Parserpriorität beträgt **200**; die Bindung ist prefix.

### Anwendung und Besonderheiten

Die Operatoren des internen Parsers sind teilweise anders als in Maxima definiert. Für eine symbolische Maxima-Berechnung sind gegebenenfalls die entsprechenden Funktionen zu verwenden.

Als Infixoperator bezeichnet `%` den Divisionsrest; als Prefix kennzeichnet es eine benannte Konstante wie `%pi`. Diese Bedeutungen hängen von der Position ab.

## Syntax

```text
%x
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Operand bzw. Ausdruck. | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| %pi | 3.141592653589793 |

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
