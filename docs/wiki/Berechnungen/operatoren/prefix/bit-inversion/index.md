# ~

[Zurück zu Berechnungen](../../../index.md)

## Name

`~` – Prefix-Operatoren.

## Detaillierte Beschreibung

bitweise Inversion einer 64bit-Ganzzahl. Die Parserpriorität beträgt **95**; die Bindung ist prefix.

### Anwendung und Besonderheiten

Die Operatoren des internen Parsers sind teilweise anders als in Maxima definiert. Für eine symbolische Maxima-Berechnung sind gegebenenfalls die entsprechenden Funktionen zu verwenden.

Die Übersicht beschreibt den Operator als Inversion einer 64-Bit-Ganzzahl. Die Klasse NOT berechnet bei Ganzzahlen `~wert` auf einer Java-long-Zahl mit 64 Bit. Das Ergebnis ist vorzeichenbehaftet; beispielsweise entspricht `~0` dem Wert -1. Die Hexadezimaldarstellung zeigt die 64-Bit-Bitfolge.

## Syntax

```text
~x
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Operand bzw. Ausdruck. | Zahl / Ausdruck / boolescher Wert je nach Operator | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| ~0x0F0F | 0xFFFFFFFFFFFFF0F0 |

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
