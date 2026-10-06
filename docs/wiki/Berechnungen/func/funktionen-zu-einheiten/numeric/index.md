# numeric

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`numeric` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

verwirft die Einheit, wenn eine vorhanden ist und liefert nur den Zahlenwert (bezogen auf die Einheit!). Bei einer SI-Einheit wird der Zahlenwert bezogen auf die Basiseinheit geliefert, bei dimensonslosen Größen wird der Zahlenwert bezogen auf die verwendete dimensionslose Einheit gewählt. numeric(x)*unit(x) liefert wieder x

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Für SI-Einheiten bezieht sich der Wert auf die Basiseinheit: 2.3 mA werden zu 0.0023. Für eine dimensionslose Größe mit Darstellungseinheit kann die Darstellung erhalten bleiben, etwa `numeric(5%) = 5`. Mit `unit(x)` kann die Größe wieder zusammengesetzt werden.

## Syntax

```text
numeric(oE)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `numeric(2.3mA) numeric(5%)`  
**Ergebnis:** 0.0023 5

| Ausdruck | Ergebnis |
| --- | --- |
| numeric(2.3mA) <br> numeric(5%) | 0.0023 <br> 5 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3177)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Numeric`.

[Zurück zu Berechnungen](../../../index.md)
