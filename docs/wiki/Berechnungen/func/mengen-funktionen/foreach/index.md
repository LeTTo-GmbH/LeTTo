# foreach

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`foreach` – Mengen-Funktionen.

## Detaillierte Beschreibung

Führt für jedes Element eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

Führt für jedes Element einer Menge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

### Anwendung und Besonderheiten

Die Implementierung erwartet 3 bis 4 Argumente.

## Syntax

```text
foreach(menge, variable, ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `foreach([2,-3,5,-6],p,cabs(p),"+")`  
**Ergebnis:** 16

| Ausdruck | Ergebnis |
| --- | --- |
| foreach(&#91;2,-3,5,-6&#93;,p,cabs(p),"+") | 16 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3383)

[DEMO-Beispiel](../../../../../demobsp.html?id=3484)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `ForEach`.

[Zurück zu Berechnungen](../../../index.md)
