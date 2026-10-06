# pvrect

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvrect` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Liefert aus einer Punktewolke ein Rechteck als zwei Eckpunkte links-unten und rechts-oben.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
pvrect(punkte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

## Beispiele

**Beispiel:** `pvrect([[1,2],[4,5],[2,3]])`  
**Ergebnis:** [[1,2],[4,5]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvrect(&#91;&#91;1,2&#93;,&#91;4,5&#93;,&#91;2,3&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;4,5&#93;&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVRect`.

[Zurück zu Berechnungen](../../../index.md)
