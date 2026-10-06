# declare

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`declare` – Spezialfunktionen LeTTo.

## Detaillierte Beschreibung

Deklariert Variablentypen für die Maxima-Kompatibilität. Die Funktion ist im internen Parser derzeit noch nicht funktional umgesetzt und liefert dort `false`.

## Syntax

```text
declare(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `declare(x,real)`  
**Ergebnis:** false

| Ausdruck | Ergebnis |
| --- | --- |
| declare(x,real) | false |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Declare`.

[Zurück zu Berechnungen](../../../index.md)
