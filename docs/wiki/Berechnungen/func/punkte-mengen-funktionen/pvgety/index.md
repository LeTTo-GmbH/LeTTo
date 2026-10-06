# pvgety

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvgety` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die y-Koordinate eines Punktes oder aller Punkte.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvgety(punkte)
pvgety(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvgety([[2,3],[4,5],[6,3],[-2,4]]) pvgety([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [3,5,3,4] 3

| Ausdruck | Ergebnis |
| --- | --- |
| pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;3,5,3,4&#93;<br>3 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3391)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVGetY`.

[Zurück zu Berechnungen](../../../index.md)
