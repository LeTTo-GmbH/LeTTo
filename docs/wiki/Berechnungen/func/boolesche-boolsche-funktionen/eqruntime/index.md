# eqruntime

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`eqruntime` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

symbolischer Vergleich, welcher symbolisch erst bei der Ergebnisberechnung ausgeführt wird. Muss verwendet werden, wenn bei Vergleichen symbolische Antworten von Schülern (Q0,Q1,...) verwendet werden.

symbolischer Vergleich, welcher **symbolisch erst bei der Ergebnisberechnung** ausgeführt wird. Muss verwendet werden, wenn bei Vergleichen symbolische Antworten von Schülern (Q0,Q1,...) verwendet werden.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
eqruntime(x1, x2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `x2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

## Beispiele

**Beispiel:** `eqruntime(x+3*y,3*y+x)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| eqruntime(x+3*y,3*y+x) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3183)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `EqRuntime`.

[Zurück zu Berechnungen](../../../index.md)
