# bitstream

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`bitstream` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Erzeugt aus einer Ganzzahl einen Bitstrom als String mit einer definierten Anzahl von Bit (MSB werden nötigenfalls mit 0 gefüllt) : bitstream(Daten,Bitanzahl,Gruppengröße)

### Anwendung und Besonderheiten

Die Ausgabe enthält die Bits vom höchstwertigen zum niedrigstwertigen Bit. Positive Werte werden bei positiver Bitanzahl auf die unteren Bits begrenzt und links mit Nullen aufgefüllt. Eine negative Bitanzahl wird positiv genommen. Bei negativen Datenwerten bildet die Implementierung eine Zweierkomplementdarstellung. Eine positive Gruppengröße gruppiert von rechts, eine negative von links. Bei Gruppengröße 0 liefert der mitgelieferte Code derzeit einen leeren String; zum Verzicht auf Gruppierung daher den dritten Parameter weglassen.

Die Implementierung erwartet 2 bis 3 Argumente.

## Syntax

```text
bitstream(x, bit)
bitstream(x, bit, groupSize)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Ganzzahl, deren Bits ausgegeben werden sollen. | Ganzzahl | nein |
| bit | Ausgabebreite in Bit; negative Werte werden positiv genommen. | Ganzzahl | nein |
| groupSize | Anzahl Bits je Gruppe; positiv: von rechts, negativ: von links. Zum Verzicht auf Gruppierung weglassen. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `bitstream(0x184,12,4)`  
**Ergebnis:** "0001 1000 0100"

| Ausdruck | Ergebnis |
| --- | --- |
| bitstream(0x184,12,4) | "0001 1000 0100" |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `BitStream`.

[Zurück zu Berechnungen](../../../index.md)
