# norm

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`norm` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

rundet einen Zahlenwert auf den nächstliegenden Wert einer gegebenen Wertereihe oder Normreihe. Die Rundung erfolgt geometrisch wenn es sich um eine logarithmisch aufgeteilte Normreihe handelt, oder sonst linear.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
norm(wert, normreihe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `norm(700Ohm,E12)`  
**Ergebnis:** 680Ohm

| Ausdruck | Ergebnis |
| --- | --- |
| norm(700Ohm,E12) | 680Ohm |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3507)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `NORM`.

[Zurück zu Berechnungen](../../../index.md)
