# sigma

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`sigma` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Sprungfunktion: sigma(x) liefert 0 für x<0 und 1 für x>=0

Sprungfunktion: sigma(x) liefert 0 für x&lt;0 und 1 für x&gt;=0

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
sigma(x)
sigma(x, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `sigma(243.3)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| sigma(243.3) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3268)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Sigma`.

[Zurück zu Berechnungen](../../../index.md)
