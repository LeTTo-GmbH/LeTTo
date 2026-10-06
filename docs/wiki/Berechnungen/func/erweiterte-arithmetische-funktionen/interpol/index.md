# interpol

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`interpol` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Interpolationsfunktion zwischen mehreren Stützpunkten in einem Koordinatensystem. interpol(WerteX,WerteY,x)

Interpoliert Zwischenwerte durch lineare Interpolation in einer als PV-Vektor gegebenen Tabelle

## Syntax

```text
interpol(pv, py)
interpol(pv, py, x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `pv` | Parameter der Funktion. | Matrix / Vektor | nein |
| `py` | Parameter der Funktion. | Matrix / Vektor | nein |
| `x` | X-Wert bzw. Ausdruck. | Vektor / Zahl | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `interpol([0,1,2],[0,3,3],1.5)`  
**Ergebnis:** 3

| Ausdruck | Ergebnis |
| --- | --- |
| interpol(&#91;0,1,2&#93;,&#91;0,3,3&#93;,1.5) | 3 |

| Ausdruck | Ergebnis |
| --- | --- |
| interpol(&#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93;,1.5) | 2.1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3272)

[DEMO-Beispiel](../../../../../demobsp.html?id=3273)

[DEMO-Beispiel](../../../../../demobsp.html?id=3386)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Interpol`.

[Zurück zu Berechnungen](../../../index.md)
