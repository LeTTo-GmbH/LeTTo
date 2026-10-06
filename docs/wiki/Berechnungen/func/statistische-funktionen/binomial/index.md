# binomial

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`binomial` – statistische Funktionen.

## Detaillierte Beschreibung

Liefert den Binomialkoeffizienten von zwei positiven ganzen Zahlen

Der Binomialkoeffizient zählt die Möglichkeiten, `k` Elemente aus `n` Elementen ohne Beachtung der Reihenfolge auszuwählen: `n!/(k!*(n-k)!)`. Der Code erwartet zwei nicht negative Ganzzahlen unter 1000000000; für `k > n` wird 0 geliefert.

## Syntax

```text
binomial(x, y)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl | nein |
| `y` | Y-Wert bzw. Ausdruck. | Ganzzahl | nein |

## Beispiele

**Beispiel:** `binomial(5,2)`  
**Ergebnis:** 10

| Ausdruck | Ergebnis |
| --- | --- |
| binomial(5,2) | 10 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3340)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStatistik.java`, Klasse `Binomial`.

[Zurück zu Berechnungen](../../../index.md)
