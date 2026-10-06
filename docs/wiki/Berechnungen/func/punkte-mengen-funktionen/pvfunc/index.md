# pvfunc

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvfunc` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Erzeugt aus einer Funktionen in einer Variablen (x-Achse) eine Punktmatrix der Funktionswerte (y-Achse). pvfunc(funktion,variable,minx,maxx,deltax)

### Anwendung und Besonderheiten

Erzeugt eine Matrix aus Wertepaaren `[x,f(x)]`. Die Parameter sind Funktion, Variable, Startwert, Endwert und Schrittweite. Der Endwert wird im mitgelieferten Code nicht eingeschlossen. Das Vorzeichen der Schrittweite wird an die Laufrichtung angepasst; bei Schrittweite 0 erfolgt keine numerische Punktgenerierung.

Die Implementierung erwartet genau 5 Argumente.

## Syntax

```text
pvfunc(funktion, variable, von, bis, schrittweite)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| funktion | Auszuwertender Ausdruck. | Ausdruck | nein |
| variable | Unabhängige Variable des Ausdrucks. | Variable | nein |
| von | Erste Auswertungsstelle. | Zahl | nein |
| bis | Grenze des Bereichs; wird nicht eingeschlossen. | Zahl | nein |
| schrittweite | Abstand der Auswertungsstellen, ungleich 0. | Zahl | nein |

## Beispiele

**Beispiel:** `pvfunc(x^2,x,-2,2,0.5)`  
**Ergebnis:** [[−2,4],[−1.5,2.25],[−1,1],[−0.5,0.25],[0,0],[0.5,0.25],[1,1],[1.5,2.25]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvfunc(x^2,x,-2,2,0.5) | &#91;&#91;−2,4&#93;,&#91;−1.5,2.25&#93;,&#91;−1,1&#93;,&#91;−0.5,0.25&#93;,&#91;0,0&#93;,&#91;0.5,0.25&#93;,&#91;1,1&#93;,&#91;1.5,2.25&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3417)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6080

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVFunc`.

[Zurück zu Berechnungen](../../../index.md)
