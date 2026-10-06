# pvequals

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvequals` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Prüft ob zwei Punktevektoren gleich sind. Die Genauigkeit wird als dritter Parameter angegeben, oder bei einem Antwortfeld von der Antworttoleranz genommen. Prozentangaben der Genauigkeit beziehen sich auf die Breite bzw. Höhe des Punktefeldes im karthesischen Koordinatensystem.

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 3 Argumente.

## Syntax

```text
pvequals(referenz, eingabe)
pvequals(referenz, eingabe, toleranz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `referenz` | Parameter der Funktion. | Vektor / Zahl | nein |
| `eingabe` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

## Beispiele

**Beispiel:** `pvequals([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[4,5],[6.01,3],[-2,3.99],[-3,5],[-7,-9]],2%)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| pvequals(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,&#91;6.01,3&#93;,&#91;-2,3.99&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,2%) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3412)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVEquals`.

[Zurück zu Berechnungen](../../../index.md)
