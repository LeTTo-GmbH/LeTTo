# curvepv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`curvepv` – Funktionen für importierte Tabellen.

## Detaillierte Beschreibung

Liest aus einer gespeicherten Tabelle die Spalte "spalteX" für die x-Werte und die Spalte "spalteY" für die Y-Werte eines pv-Vektors

## Syntax

```text
curvepv(tabelle, xSpalte, ySpalte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Matrix / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Matrix / Zahl | nein |

## Beispiele

**Beispiel:** `curvepv([[0,0,2],[1,2,3],[2,2.2,1.5],[3,1.4,1.8]],0,1)`  
**Ergebnis:** [[0,0],[1,2],[2,2.2],[3,1.4]]

| Ausdruck | Ergebnis |
| --- | --- |
| curvepv(&#91;&#91;0,0,2&#93;,&#91;1,2,3&#93;,&#91;2,2.2,1.5&#93;,&#91;3,1.4,1.8&#93;&#93;,0,1) | &#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3384)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `CurvePointvector`.

[Zurück zu Berechnungen](../../../index.md)
