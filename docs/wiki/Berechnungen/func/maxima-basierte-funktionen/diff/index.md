# diff

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`diff` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Berechnet die Ableitung einer Funktion.

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
diff(funktion, variable)
diff(funktion, variable, anzahl)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck, der abgeleitet wird. | Ausdruck | nein |
| `variable` | Variable, nach der abgeleitet wird. | Variable | nein |
| `anzahl` | Ordnung der Ableitung. | Ganzzahl | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `diff(x^2,x) diff(3*x^2,x,2)`  
**Ergebnis:** 2*x; 6

| Ausdruck | Ergebnis |
| --- | --- |
| diff(x^2,x)<br>diff(3*x^2,x,2) | 2*x <br> 6 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3251)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `Diff`.

[Zurück zu Berechnungen](../../../index.md)
