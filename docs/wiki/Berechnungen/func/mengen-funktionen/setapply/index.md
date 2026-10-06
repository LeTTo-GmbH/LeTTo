# setapply

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setapply` – Mengen-Funktionen.

## Detaillierte Beschreibung

wendet einen Ausdruck oder Funktion auf alle Elemente einer Menge an

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
setapply(variable, menge, ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `setapply(y,[1,2,3],y*2)`  
**Ergebnis:** [2,4,6]

| Ausdruck | Ergebnis |
| --- | --- |
| setapply(y,&#91;1,2,3&#93;,y*2) | &#91;2,4,6&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3347)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 5965

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetApply`.

[Zurück zu Berechnungen](../../../index.md)
