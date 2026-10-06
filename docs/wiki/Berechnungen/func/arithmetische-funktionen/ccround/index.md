# ccround

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ccround` – arithmetische Funktionen.

## Detaillierte Beschreibung

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, bei komplexe Zahlen wird Real und Imaginärteil gerundet.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
ccround(wert)
ccround(wert, kommastellen)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `kommastellen` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `ccround(2.4534+5.645*%i,2)`  
**Ergebnis:** 2.45+5.65i

| Ausdruck | Ergebnis |
| --- | --- |
| ccround(2.4534+5.645*%i,2) | 2.45+5.65i |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3221)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `CCRound`.

[Zurück zu Berechnungen](../../../index.md)
