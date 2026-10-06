# pvforeachline

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvforeachline` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Führt für jedes Punktepaar eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

Führt für jedes Punktepaar einer Punktemenge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

### Anwendung und Besonderheiten

Die Implementierung erwartet 3 bis 4 Argumente.

## Syntax

```text
pvforeachline(punkte, variable, ausdruck)
pvforeachline(punkte, variable, ausdruck, aggregation)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `aggregation` | Parameter der Funktion. | Ausdruck | ja |

## Beispiele

**Beispiel:** `pvforeachline([[2,3],[4,5],[6,3],[-2,4]],p,pvlineabs(p),"+")`  
**Ergebnis:** 10.890684873

| Ausdruck | Ergebnis |
| --- | --- |
| pvforeachline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,p,pvlineabs(p),"+") | 10.890684873 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3416)

[DEMO-Beispiel](../../../../../demobsp.html?id=3485)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVForEachLine`.

[Zurück zu Berechnungen](../../../index.md)
