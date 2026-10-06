# pvdistance

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvdistance` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Abstände als Vektoren zwischen den Punkten. pvdistance([A,B,C]) liefert [AB,BC,CA]

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
pvdistance(punkte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

## Beispiele

**Beispiel:** `pvdistance([[1,2],[3,4],[10,10]])`  
**Ergebnis:** [[2,2],[7,6],[-9,-8]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvdistance(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;10,10&#93;&#93;) | &#91;&#91;2,2&#93;,&#91;7,6&#93;,&#91;-9,-8&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3395)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6569

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVDistance`.

[Zurück zu Berechnungen](../../../index.md)
