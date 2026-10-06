# kill

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`kill` – Variable.

## Detaillierte Beschreibung

löscht Variable aus dem Variablenspeicher

## Syntax

```text
kill(variable1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable1` | Parameter der Funktion. | Variable | nein |

## Beispiele

**Beispiel:** `kill(x,y) kill(allbut(y)) kill(all)`  
**Ergebnis:** löscht die Variablen x und y löscht alle Variablen mit Ausnahme von y löscht alle Variable

| Ausdruck | Ergebnis |
| --- | --- |
| kill(x,y) <br> kill(allbut(y)) <br> kill(all) | löscht die Variablen x und y <br> löscht alle Variablen mit Ausnahme von y <br> löscht alle Variable |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3471)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Kill`.

[Zurück zu Berechnungen](../../../index.md)
