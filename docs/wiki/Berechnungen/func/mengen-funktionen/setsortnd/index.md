# setsortnd

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setsortnd` – Mengen-Funktionen.

## Detaillierte Beschreibung

Sortiert die Elemente einer Menge aufsteigend und entfernt alle mehrfach vorkommenden Elemente

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
setsortnd(v1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setsortnd([31,-3,2,31,0,5,2])`  
**Ergebnis:** [-3,0,2,5,31]

| Ausdruck | Ergebnis |
| --- | --- |
| setsortnd(&#91;31,-3,2,31,0,5,2&#93;) | &#91;-3,0,2,5,31&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3351)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetSortNoDuplicate`.

[Zurück zu Berechnungen](../../../index.md)
