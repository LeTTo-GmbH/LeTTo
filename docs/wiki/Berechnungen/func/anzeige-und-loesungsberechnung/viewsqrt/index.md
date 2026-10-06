# viewsqrt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`viewsqrt` – Anzeige und Lösungsberechnung.

## Detaillierte Beschreibung

Gibt Potenzen welche als Wurzel darstellbar sind auch als als Wurzeln mit der Funktion sqrt oder root aus

### Anwendung und Besonderheiten

Der optionale Modus bestimmt, ob die Umschreibung bei Lösung und Anzeige (0), nur bei Lösung (1) oder nur bei Anzeige (2) erfolgt. Während normaler Berechnungen bleibt die Funktion erhalten.

## Syntax

```text
viewsqrt(ausdruck)
viewsqrt(ausdruck, modus)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Darzustellender Ausdruck. | Ausdruck | nein |
| modus | 0: Lösung und Anzeige; 1: nur Lösung; 2: nur Anzeige. Vorgabe 0. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `viewsqrt(x^(1/2))`  
**Ergebnis:** sqrt(x)

| Ausdruck | Ergebnis |
| --- | --- |
| viewsqrt(x^(1/2)) | sqrt(x) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3496)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateViewFunctions.java`, Klasse `ViewSqrt`.

[Zurück zu Berechnungen](../../../index.md)
