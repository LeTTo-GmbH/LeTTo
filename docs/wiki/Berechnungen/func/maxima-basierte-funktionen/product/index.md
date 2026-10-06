# product

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`product` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Produktbildung

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
product(funktion, variable, untergrenze, obergrenze)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck des Faktors. | Ausdruck | nein |
| `variable` | Laufvariable des Produkts. | Variable | nein |
| `untergrenze` | Erster Wert der Laufvariable. | Zahl / Ausdruck | nein |
| `obergrenze` | Letzter Wert der Laufvariable. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `product(1/k,k,1,3)`  
**Ergebnis:** 1/6

| Ausdruck | Ergebnis |
| --- | --- |
| product(1/k,k,1,3) | 1/6 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3267)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `Product`.

[Zurück zu Berechnungen](../../../index.md)
