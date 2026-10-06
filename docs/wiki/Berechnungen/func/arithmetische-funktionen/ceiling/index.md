# ceiling

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ceiling` – arithmetische Funktionen.

## Detaillierte Beschreibung

ceiling(x) Rundet auf die kleinste ganze Zahl, welche größer oder gleich x ist

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Rundet in Richtung plus unendlich. Deshalb ergibt `ceiling(-2.3)` den Wert -2. Für eine bereits ganze Zahl bleibt deren Wert erhalten.

## Syntax

```text
ceiling(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `ceiling(13.2)`  
**Ergebnis:** 14

| Ausdruck | Ergebnis |
| --- | --- |
| ceiling(13.2) | 14 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3227)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Ceiling`.

[Zurück zu Berechnungen](../../../index.md)
