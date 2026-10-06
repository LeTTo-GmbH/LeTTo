# setshuffle

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setshuffle` – Mengen-Funktionen.

## Detaillierte Beschreibung

Mischt eine Menge in eine andere Reihenfolge. VORSICHT, ohne zweiten Parameter (ganze Zahl) ändert sich die Reihenfolge bei jedem mal neu Laden automatisch und ist nicht nachvollziehbar, weshalb sie dann für Schülerbeispiele nicht einsetzbar ist! Daher ist es für eine praktische Anwendung in einem Schülerbeispiel erforderlich, dass der zweite Parameter determiniert (beispielsweise über einen Integer-Datensatz-Wert zwischen 0 und 1000) festgelegt wird.

Mischt eine Menge in eine andere Reihenfolge. VORSICHT, ohne zweiten Parameter (ganze Zahl) ändert sich die Reihenfolge bei jedem mal neu Laden automatisch und ist nicht nachvollziehbar, weshalb sie dann für Schülerbeispiele nicht einsetzbar ist! Daher ist es für eine praktische Anwendung in einem Schülerbeispiel **erforderlich**, dass der zweite Parameter determiniert (beispielsweise über einen Integer-Datensatz-Wert zwischen 0 und 1000) festgelegt wird.

## Syntax

```text
setshuffle(v1)
setshuffle(v1, nummer)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `nummer` | Nummer bzw. Auswahlindex. | Ganzzahl | ja (bei 2 Parametern) |

## Beispiele

**Beispiel:** `setshuffle([3,-3,2,0,5,2],5)`  
**Ergebnis:** [2,3,−3,2,0,5]

| Ausdruck | Ergebnis |
| --- | --- |
| setshuffle(&#91;3,-3,2,0,5,2&#93;,5) | &#91;2,3,−3,2,0,5&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3356)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6082

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetShuffle`.

[Zurück zu Berechnungen](../../../index.md)
