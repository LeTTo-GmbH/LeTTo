# pvinsert

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvinsert` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Fügt einen Punkt in die Punktemenge ein

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
pvinsert(punkte, punkt, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |

## Beispiele

**Beispiel:** `pvinsert([[2,3],[4,5],[6,3],[-2,4]],[7,8],2)`  
**Ergebnis:** [[2,3],[4,5],[7,8],[6,3],[-2,4]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvinsert(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;,2) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;7,8&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3392)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6678

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVInsert`.

[Zurück zu Berechnungen](../../../index.md)
