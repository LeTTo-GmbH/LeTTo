# ilt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ilt` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Bestimmt die inverse Laplace-Transformierte eine Laplace-Funktion

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
ilt(funktion, variable, zielvariable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck in der Laplace-Domäne. | Ausdruck | nein |
| `variable` | Variable der Laplace-Domäne. | Variable | nein |
| `zielvariable` | Zielvariable der inversen Transformation. | Variable | nein |

## Beispiele

**Beispiel:** `ilt(1/(1+s),s,t)`  
**Ergebnis:** e^(-t)

| Ausdruck | Ergebnis |
| --- | --- |
| ilt(1/(1+s),s,t) | e^(-t) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3265)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `InverseLaplace`.

[Zurück zu Berechnungen](../../../index.md)
