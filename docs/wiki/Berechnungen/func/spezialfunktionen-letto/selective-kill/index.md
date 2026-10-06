# selective_kill

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`selective_kill` – Spezialfunktionen LeTTo.

## Detaillierte Beschreibung

Löscht alle Variablen aus dem Variablenspeicher außer den angegebenen Variablen bzw. Variablenvektoren und liefert die Anzahl der gelöschten Variablen.

## Syntax

```text
selective_kill(...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable1` | Parameter der Funktion. | Variable | ja, beliebig oft |

## Beispiele

**Beispiel:** `selective_kill(x,y)`  
**Ergebnis:** Anzahl der gelöschten Variablen

| Ausdruck | Ergebnis |
| --- | --- |
| selective_kill(x,y) | Anzahl der gelöschten Variablen |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `SKill`.

[Zurück zu Berechnungen](../../../index.md)
