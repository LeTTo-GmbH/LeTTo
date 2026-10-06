# pvinsertlast

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvinsertlast` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Fügt am Ende der Punktemenge einen Punkt ein

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
pvinsertlast(punkte, punkt)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor | nein |

## Beispiele

**Beispiel:** `pvinsertlast([[2,3],[4,5],[6,3],[-2,4]],[7,8])`  
**Ergebnis:** [[2,3],[4,5],[6,3],[-2,4],[7,8]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvinsertlast(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;7,8&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3393)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6678

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVInsertLast`.

[Zurück zu Berechnungen](../../../index.md)
