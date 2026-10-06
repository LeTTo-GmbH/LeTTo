# pvarg

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvarg` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt den Winkel eines Punktes oder aller Ortsvektoren zu den Punkten.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvarg(punkte)
pvarg(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvarg([[2,3],[4,5],[6,3],[-2,4]]) pvarg([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [0.98279,0.89606,0.46365,2.0344] 0.89606

| Ausdruck | Ergebnis |
| --- | --- |
| pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;0.98279,0.89606,0.46365,2.0344&#93; <br> 0.89606 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3388)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVArg`.

[Zurück zu Berechnungen](../../../index.md)
