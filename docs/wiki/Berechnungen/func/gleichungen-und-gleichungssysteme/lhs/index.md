# lhs

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`lhs` – Gleichungen und Gleichungssysteme.

## Detaillierte Beschreibung

liefert die linke Seite einer Gleichung, Ungleichung oder eines Infix Operators

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
lhs(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `lhs(x+y=c+2)`  
**Ergebnis:** x+y

| Ausdruck | Ergebnis |
| --- | --- |
| lhs(x+y=c+2) | x+y |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3284)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6521

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `Lhs`.

[Zurück zu Berechnungen](../../../index.md)
