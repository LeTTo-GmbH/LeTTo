# pvline

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvline` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Geradengleichung einer Geraden durch das n-te Punktepaar

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvline(punkte)
pvline(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvline([[2,3],[4,5],[6,3],[-2,4]]) pvline([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [y=1+x,y=3.75−0.125⋅x] y=x+1

| Ausdruck | Ergebnis |
| --- | --- |
| pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;y=1+x,y=3.75−0.125⋅x&#93;<br>y=x+1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3400)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVLine`.

[Zurück zu Berechnungen](../../../index.md)
