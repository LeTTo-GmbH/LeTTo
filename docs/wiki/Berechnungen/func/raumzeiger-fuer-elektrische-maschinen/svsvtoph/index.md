# svsvtoph

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`svsvtoph` – Raumzeiger für elektrische Maschinen.

## Detaillierte Beschreibung

berechnet aus einem komplexen Raumzeiger die Stranggrössen berechnet aus einem komplexen Raumzeiger die Stranggrössen, index selektiert Stranggröße als Rückgabewert

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
svsvtoph(raumzeiger)
svsvtoph(raumzeiger, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `raumzeiger` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `svsvtoph(1arg60°) svsvtoph(1arg60°,3)`  
**Ergebnis:** [0.5,0.5,-1] -1

| Ausdruck | Ergebnis |
| --- | --- |
| svsvtoph(1arg60°)<br> svsvtoph(1arg60°,3) | &#91;0.5,0.5,-1&#93; <br> -1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3513)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateRaumzeigerFunctions.java`, Klasse `SvSvtoPh`.

[Zurück zu Berechnungen](../../../index.md)
