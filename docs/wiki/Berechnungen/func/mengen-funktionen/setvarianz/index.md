# setvarianz

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setvarianz` – Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die empirische Varianz einer Menge

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
setvarianz(v1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `setvarianz([3,1,2,5,4])`  
**Ergebnis:** ((3-3)^2+(1-3)^2+(2-3)^2+(5-3)^2+(4-3)^2)/5=2

| Ausdruck | Ergebnis |
| --- | --- |
| setvarianz(&#91;3,1,2,5,4&#93;) | ((3-3)^2+(1-3)^2+(2-3)^2+(5-3)^2+(4-3)^2)/5=2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3359)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetVarianz`.

[Zurück zu Berechnungen](../../../index.md)
