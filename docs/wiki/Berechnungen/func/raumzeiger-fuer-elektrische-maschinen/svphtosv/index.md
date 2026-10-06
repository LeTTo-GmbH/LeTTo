# svphtosv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`svphtosv` – Raumzeiger für elektrische Maschinen.

## Detaillierte Beschreibung

berechnet aus den Stranggrößen (a,b,c) einen komplexen Raumzeiger

## Syntax

```text
svphtosv(phaseA)
svphtosv(phaseA, phaseB, phaseC)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `phaseA` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `phaseB` | Parameter der Funktion. | Zahl / Ausdruck | ja (bei 3 Parametern) |
| `phaseC` | Parameter der Funktion. | Zahl / Ausdruck | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `svphtosv(0.5,0.5,-1)`  
**Ergebnis:** 1arg60°

| Ausdruck | Ergebnis |
| --- | --- |
| svphtosv(0.5,0.5,-1) | 1arg60° |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3512)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateRaumzeigerFunctions.java`, Klasse `SvPhtoSv`.

[Zurück zu Berechnungen](../../../index.md)
