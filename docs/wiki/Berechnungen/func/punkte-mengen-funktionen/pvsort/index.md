# pvsort

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvsort` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Sortiert die Punkte zuerst nach steigender x-Koordinate und bei gleicher x-Koordinate nach steigender y-Koordinate.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
pvsort(punkte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

## Beispiele

**Beispiel:** `pvsort([[2,3],[1,5],[1,2]])`  
**Ergebnis:** [[1,2],[1,5],[2,3]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvsort(&#91;&#91;2,3&#93;,&#91;1,5&#93;,&#91;1,2&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;1,5&#93;,&#91;2,3&#93;&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `CompareVector`.

[Zurück zu Berechnungen](../../../index.md)
