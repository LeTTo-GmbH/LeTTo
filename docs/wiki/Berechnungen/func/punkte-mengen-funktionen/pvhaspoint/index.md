# pvhaspoint

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvhaspoint` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Prüft ob sich ein Punkt innerhalb des Punktefeldes befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden.

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 3 Argumente.

## Syntax

```text
pvhaspoint(punkte, punkt)
pvhaspoint(punkte, punkt, toleranz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

## Beispiele

**Beispiel:** `pvhaspoint([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[4,5],2%)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| pvhaspoint(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,2%) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3413)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVHasPoint`.

[Zurück zu Berechnungen](../../../index.md)
