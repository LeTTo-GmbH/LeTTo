# sum

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`sum` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Summenbildung

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
sum(funktion, variable, untergrenze, obergrenze)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck des Summanden. | Ausdruck | nein |
| `variable` | Laufvariable der Summe. | Variable | nein |
| `untergrenze` | Erster Wert der Laufvariable. | Zahl / Ausdruck | nein |
| `obergrenze` | Letzter Wert der Laufvariable. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `sum(1/k,k,1,2)`  
**Ergebnis:** 3/2

| Ausdruck | Ergebnis |
| --- | --- |
| sum(1/k,k,1,2) | 3/2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3266)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `Sum`.

[Zurück zu Berechnungen](../../../index.md)
