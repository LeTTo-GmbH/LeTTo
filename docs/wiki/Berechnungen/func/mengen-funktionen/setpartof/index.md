# setpartof

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setpartof` – Mengen-Funktionen.

## Detaillierte Beschreibung

prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge egal ist aber mehrfache Werte berücksichtigt werden

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
setpartof(p1, p2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setpartof([1,4],[1,3,7]) setpartof([1,3],[1,2,3]) setpartof([1,3,3],[1,3,5,7]) setpartof([1,4,4],[1,2,3,4])`  
**Ergebnis:** false true false false

| Ausdruck | Ergebnis |
| --- | --- |
| setpartof(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartof(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartof([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartof([1,4,4&#93;,[1,2,3,4&#93;) | false <br> true <br> false <br> false |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3370)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetPartOf`.

[Zurück zu Berechnungen](../../../index.md)
