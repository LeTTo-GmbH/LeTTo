# curveHTML

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`curveHTML` – Funktionen für importierte Tabellen.

## Detaillierte Beschreibung

Liefert eine HTML-Ansicht einer Tabelle.

## Syntax

```text
curveHTML(mat, variable, variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mat` | Parameter der Funktion. | Matrix / Vektor | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `curvHTML(KL,KL_names,curveunits(KL))`  
**Ergebnis:** HTML-Code der Tabelle

| Ausdruck | Ergebnis |
| --- | --- |
| curvHTML(KL,KL_names,curveunits(KL)) | HTML-Code der Tabelle |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTable.java`, Klasse `CurveHTML`.

[Zurück zu Berechnungen](../../../index.md)
