# pvunion

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvunion` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

hängt mehrere Punktevektoren zu einem größereren Punktevektor zusammen

## Syntax

```text
pvunion(punktevektor1, wert2, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punktevektor1` | Parameter der Funktion. | Vektor / Matrix | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `pvunion([[1,2],[3,4]],[[5,6],[7,8]],[9,10])`  
**Ergebnis:** [[1,2],[3,4],[5,6],[7,8],[9,10]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvunion(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;,&#91;&#91;5,6&#93;,&#91;7,8&#93;&#93;,&#91;9,10&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;,&#91;9,10&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3421)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6569

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `PVunion`.

[Zurück zu Berechnungen](../../../index.md)
