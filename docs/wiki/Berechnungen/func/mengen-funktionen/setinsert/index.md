# setinsert

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setinsert` – Mengen-Funktionen.

## Detaillierte Beschreibung

fügt ein Element in eine Menge an eine gegebene Stelle ein

## Syntax

```text
setinsert(menge, index, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `setinsert([12,13,14],1,25)`  
**Ergebnis:** [12,25,13,14]

| Ausdruck | Ergebnis |
| --- | --- |
| setinsert(&#91;12,13,14&#93;,1,25) | &#91;12,25,13,14&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3344)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VInsert`.

[Zurück zu Berechnungen](../../../index.md)
