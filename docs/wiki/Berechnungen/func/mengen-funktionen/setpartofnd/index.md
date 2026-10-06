# setpartofnd

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setpartofnd` – Mengen-Funktionen.

## Detaillierte Beschreibung

prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge und mehrfache Werte egal sind

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
setpartofnd(p1, p2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setpartofnd([1,4],[1,3,7]) setpartofnd([1,3],[1,2,3]) setpartofnd([1,3,3],[1,3,5,7]) setpartofnd([1,4,4],[1,2,3,4])`  
**Ergebnis:** false true true true

| Ausdruck | Ergebnis |
| --- | --- |
| setpartofnd(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartofnd(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartofnd([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartofnd([1,4,4&#93;,[1,2,3,4&#93;) | false <br> true <br> true <br> true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3372)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetPartOfNoDuplicate`.

[Zurück zu Berechnungen](../../../index.md)
