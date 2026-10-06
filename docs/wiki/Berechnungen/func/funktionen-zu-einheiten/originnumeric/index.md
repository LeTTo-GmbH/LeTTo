# originnumeric

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`originnumeric` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

liefert immer den Zahlenwert einer einheitenbehafteten Größe bezogen auf die vorhandene Einheit. Gibt es keine Originaleinheit da der Wert berechnet wurde wird der Zahlenwert bezogen auf die SI-Grundeinheit genommen. originnumeric(x)*originunit(x) liefert wieder x

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Bezieht sich auf die ursprüngliche Darstellungseinheit: Aus 2.3 mA wird 2.3. Der Unterschied zu `numeric` ist bei Einheitenpräfixen entscheidend. Mit `originunit(x)` kann die ursprüngliche Größe wieder zusammengesetzt werden.

## Syntax

```text
originnumeric(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `originnumeric(2.3mA) originnumeric(2.3mA*2Ohm) originnumeric(15°)`  
**Ergebnis:** 2.3 0.0046 15

| Ausdruck | Ergebnis |
| --- | --- |
| originnumeric(2.3mA) <br> originnumeric(2.3mA*2Ohm) <br> originnumeric(15°) | 2.3 <br> 0.0046 <br> 15 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3178)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `OriginNumeric`.

[Zurück zu Berechnungen](../../../index.md)
