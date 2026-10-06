# viewpow

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`viewpow` – Anzeige und Lösungsberechnung.

## Detaillierte Beschreibung

Gibt alle Wurzeln als Potenzen aus, und stellt alle Potenzen im Nenner als negativen Exponenten im Zähler dar

### Anwendung und Besonderheiten

Der optionale Modus bestimmt, ob die Umschreibung bei Lösung und Anzeige (0), nur bei Lösung (1) oder nur bei Anzeige (2) erfolgt. Während normaler Berechnungen bleibt die Funktion erhalten.

## Syntax

```text
viewpow(ausdruck)
viewpow(ausdruck, modus)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Darzustellender Ausdruck. | Ausdruck | nein |
| modus | 0: Lösung und Anzeige; 1: nur Lösung; 2: nur Anzeige. Vorgabe 0. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `viewpow(sqrt(x))`  
**Ergebnis:** x^(1/2)

| Ausdruck | Ergebnis |
| --- | --- |
| viewpow(sqrt(x)) | x^(1/2) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3495)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateViewFunctions.java`, Klasse `ViewPow`.

[Zurück zu Berechnungen](../../../index.md)
