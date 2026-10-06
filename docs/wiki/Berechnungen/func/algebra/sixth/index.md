# sixth

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`sixth` – Algebra.

## Detaillierte Beschreibung

liefert das sechste Element mit dem Index 5 eines Vektors

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
sixth()
sixth(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

## Beispiele

**Beispiel:** `sixth ([12,13,14,15,16,17,18])`  
**Ergebnis:** 17

| Ausdruck | Ergebnis |
| --- | --- |
| sixth (&#91;12,13,14,15,16,17,18&#93;) | 17 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3434)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Sixth`.

[Zurück zu Berechnungen](../../../index.md)
