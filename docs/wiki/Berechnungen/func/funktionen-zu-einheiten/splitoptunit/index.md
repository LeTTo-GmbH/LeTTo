# splitoptunit

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`splitoptunit` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Zerlegt einen numerischen Wert in Zahlenwert und die optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
splitoptunit(oE)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | Vektor / Ganzzahl | nein |

## Beispiele

**Beispiel:** `splitoptunit(1300kVA)`  
**Ergebnis:** [1.3,1MVA]

| Ausdruck | Ergebnis |
| --- | --- |
| splitoptunit(1300kVA) | &#91;1.3,1MVA&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `SplitOptUnit`.

[Zurück zu Berechnungen](../../../index.md)
