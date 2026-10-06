# pvlineabs

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvlineabs` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt aus dem n-ten Punktepaar den Absolutbetrag des Abstandes.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvlineabs(punkte)
pvlineabs(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvlineabs([[2,3],[4,5],[6,3],[-2,4]]) pvlineabs([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [2.8284,8.0623] 2.82842712475

| Ausdruck | Ergebnis |
| --- | --- |
| pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;2.8284,8.0623&#93;<br>2.82842712475 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3396)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVLineAbs`.

[Zurück zu Berechnungen](../../../index.md)
