# pvhasline

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvhasline` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Prüft ob sich eine Linie innerhalb des Punktefeldes von Linien befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden.

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 3 Argumente.

## Syntax

```text
pvhasline(punkte, linie)
pvhasline(punkte, linie, toleranz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `linie` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

## Beispiele

**Beispiel:** `pvhasline([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[[6,3],[-2,4]],2%)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| pvhasline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;&#91;6,3&#93;,&#91;-2,4&#93;&#93;,2%) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3414)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6078

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVHasLine`.

[Zurück zu Berechnungen](../../../index.md)
