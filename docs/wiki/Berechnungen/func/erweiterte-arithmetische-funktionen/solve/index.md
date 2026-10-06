# solve

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`solve` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen

## Syntax

```text
solve(gleichungen, varlist)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `gleichungen` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `varlist` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |

## Beispiele

**Beispiel:** `solve([2*x+y=3,x-y=0],[x,y])`  
**Ergebnis:** [[ x=1,y=1 ]]

| Ausdruck | Ergebnis |
| --- | --- |
| solve(&#91;2*x+y=3,x-y=0&#93;,&#91;x,y&#93;) | &#91;&#91; x=1,y=1 &#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3277)

[DEMO-Beispiel](../../../../../demobsp.html?id=3283)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Solve`.

[Zurück zu Berechnungen](../../../index.md)
