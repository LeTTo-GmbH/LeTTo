# setboxplot

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setboxplot` – Mengen-Funktionen.

## Detaillierte Beschreibung

Liefert die Werte des Boxplot einer Menge (Minimum, unteres Quartil, Median, oberes Quartil, Maximum) als Vektor verwendbar für das Plot-Plugin#definierte-zeichenelemente-

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
setboxplot(v1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setboxplot([1,2,3,10,8,9]`  
**Ergebnis:** [1,2,5.5,9,10]

| Ausdruck | Ergebnis |
| --- | --- |
| setboxplot(&#91;1,2,3,10,8,9&#93; | &#91;1,2,5.5,9,10&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3349)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetBoxPlot`.

[Zurück zu Berechnungen](../../../index.md)
