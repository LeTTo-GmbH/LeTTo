# curveunits

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`curveunits` – Funktionen für importierte Tabellen.

## Detaillierte Beschreibung

Liefert einen Vektor aller Einheiten der Spalten einer Matrix

## Syntax

```text
curveunits(mat)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mat` | Parameter der Funktion. | Matrix / Vektor | nein |

## Beispiele

**Beispiel:** `curveunits(curvepv([[3A,7V,2],[2A,2V,3],[2A,2.2V],[3A,1.4V]])`  
**Ergebnis:** [1A,1V]

| Ausdruck | Ergebnis |
| --- | --- |
| curveunits(curvepv(&#91;&#91;3A,7V,2&#93;,&#91;2A,2V,3&#93;,&#91;2A,2.2V&#93;,&#91;3A,1.4V&#93;&#93;) | &#91;1A,1V&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTable.java`, Klasse `CurveUnits`.

[Zurück zu Berechnungen](../../../index.md)
