# setunionnd

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setunionnd` – Mengen-Funktionen.

## Detaillierte Beschreibung

Fügt mehrere Mengen zu einer neuen Menge zusammen, sortiert diese und entfernt alle mehrfachen Elemente

Vereinigt die Elemente der übergebenen Mengen und entfernt Mehrfachvorkommen. Dies unterscheidet sich von `setunion`, das gleiche Elemente mehrfach enthalten kann.

## Syntax

```text
setunionnd()
```

## Parameterbeschreibung

In der bereitgestellten Parameterreferenz ist keine separate Parametertabelle enthalten. Die Aufrufvarianten sind im Abschnitt Syntax angegeben.

## Beispiele


**Beispiel:** `setunionnd([1,3,2,4],[3,7])`  
**Ergebnis:** [1,2,3,4,7]

| Ausdruck | Ergebnis |
| --- | --- |
| setunionnd(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;1,2,3,4,7&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3365)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetUnionNoDuplicate`.

[Zurück zu Berechnungen](../../../index.md)
