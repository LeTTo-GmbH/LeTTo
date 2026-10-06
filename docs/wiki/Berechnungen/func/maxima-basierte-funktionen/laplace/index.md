# laplace

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`laplace` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Bestimmt die Laplace-Transformierte einer Funktion.

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
laplace(funktion, variable, zielvariable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Zu transformierender Ausdruck. | Ausdruck | nein |
| `variable` | Ursprüngliche Variable, meist Zeitvariable. | Variable | nein |
| `zielvariable` | Variable der Laplace-Domäne. | Variable | nein |

## Beispiele

**Beispiel:** `laplace(sin(t),t,s)`  
**Ergebnis:** 1/(1+s^2)

| Ausdruck | Ergebnis |
| --- | --- |
| laplace(sin(t),t,s) | 1/(1+s^2) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3264)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `Laplace`.

[Zurück zu Berechnungen](../../../index.md)
