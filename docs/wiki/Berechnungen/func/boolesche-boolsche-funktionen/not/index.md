# not

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`not` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen lnot )

logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen **lnot** )

### Anwendung und Besonderheiten

Die mitgelieferte Klasse NOT liefert bei booleschen Werten die logische Negation. Bei Ganzzahlen wird hingegen die bitweise Negation einer 64-Bit-long-Zahl berechnet. Für eine ausschließlich boolesche Negation ist die Variante lnot beschrieben.

Die Implementierung erwartet 1 bis 1 Argumente.

## Syntax

```text
not(bedingung)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `bedingung` | Parameter der Funktion. | Ausdruck | nein |

## Beispiele

**Beispiel:** `not(a<b)`

| Ausdruck | Ergebnis |
| --- | --- |
| not(a&lt;b) | In der Übersicht nicht angegeben. |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3192)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateLogicalOperators.java`, Klasse `NOT`.

[Zurück zu Berechnungen](../../../index.md)
