# solvevalue

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`solvevalue` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

löst eine Gleichung oder ein Gleichungssystem nach einer Variablen und liefert genau die erste Lösung wenn sie numerisch berechenbar ist

## Syntax

```text
solvevalue(cc, varlist, ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `cc` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `varlist` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `solvevalue([ 2*x+y=3,x-y=0 ],[ x,y ],x)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| solvevalue(&#91; 2*x+y=3,x-y=0 &#93;,&#91; x,y &#93;,x) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3278)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `SolveValue`.

[Zurück zu Berechnungen](../../../index.md)
