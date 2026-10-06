# ln

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ln` – Exponentialfunktionen.

## Detaillierte Beschreibung

natürlicher Logarythmus

Alias/Kompatibilitätsname zu `log`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [log](../log/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Berechnet den natürlichen Logarithmus zur Basis `%e`. Für positive reelle Werte gilt `exp(log(x)) = x`; `log(1) = 0` und `log(%e) = 1`.

## Syntax

```text
ln(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `ln(%e)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| ln(%e) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3327)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Ln`.

[Zurück zu Berechnungen](../../../index.md)
