# setcomparend

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setcomparend` – Mengen-Funktionen.

## Detaillierte Beschreibung

vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist und doppelte Werte als einfach behandelt werden.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
setcomparend(p1, p2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setcomparend([1,3,2,4],[3,7]) setcomparend([1,3,2],[1,2,3]) setcomparend([1,3,2],[1,3,2,3]) setcomparend([1,2,3],[1,2,3])`  
**Ergebnis:** false true true true

| Ausdruck | Ergebnis |
| --- | --- |
| setcomparend(&#91;1,3,2,4&#93;,[3,7&#93;) <br> setcomparend([1,3,2&#93;,[1,2,3&#93;) <br> setcomparend([1,3,2&#93;,[1,3,2,3&#93;) <br> setcomparend([1,2,3&#93;,[1,2,3&#93;) | false <br> true <br> true <br> true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3369)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetCompareNoDuplicate`.

[Zurück zu Berechnungen](../../../index.md)
