# pvlinek

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvlinek` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Steigung der zugehörigen Geraden dem n-ten Punktepaar

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvlinek(punkte)
pvlinek(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvlinek([[2,3],[4,5],[6,3],[-2,4]]) pvlinek([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [1,−0.125] 1

| Ausdruck | Ergebnis |
| --- | --- |
| pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;1,−0.125&#93;<br>1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3398)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVLineK`.

[Zurück zu Berechnungen](../../../index.md)
