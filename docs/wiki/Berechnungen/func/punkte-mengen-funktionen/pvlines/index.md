# pvlines

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvlines` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Anzahl der Linien bzw. Punktepaare eines Punktevektors.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvlines(punkte)
pvlines(punkte, reserviert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `reserviert` | Optionaler zusätzlicher Parameter; wird von der aktuellen Implementierung akzeptiert, aber nicht ausgewertet. | Ausdruck / passender Datentyp | ja |

## Beispiele

**Beispiel:** `pvlines([[1,2],[3,4],[5,6],[7,8]])`  
**Ergebnis:** 2

| Ausdruck | Ergebnis |
| --- | --- |
| pvlines(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;&#93;) | 2 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVLines`.

[Zurück zu Berechnungen](../../../index.md)
