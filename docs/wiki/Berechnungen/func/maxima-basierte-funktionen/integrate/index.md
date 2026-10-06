# integrate

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`integrate` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Berechnet das unbestimmte oder bestimmte Integral einer Funktion.

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
integrate(funktion, variable)
integrate(funktion, variable, untergrenze, obergrenze)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Zu integrierender Ausdruck. | Ausdruck | nein |
| `variable` | Integrationsvariable. | Variable | nein |
| `untergrenze` | Untere Integrationsgrenze. | Zahl / Ausdruck | ja (bei 4 Parametern) |
| `obergrenze` | Obere Integrationsgrenze. | Zahl / Ausdruck | ja (bei 4 Parametern) |

## Beispiele

**Beispiel:** `integrate(x^2,x) integrate(x^2,x,0,2)`  
**Ergebnis:** x^3/3 8/3

| Ausdruck | Ergebnis |
| --- | --- |
| integrate(x^2,x) <br> integrate(x^2,x,0,2) | x^3/3 <br> 8/3 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3250)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `Integrate`.

[Zurück zu Berechnungen](../../../index.md)
