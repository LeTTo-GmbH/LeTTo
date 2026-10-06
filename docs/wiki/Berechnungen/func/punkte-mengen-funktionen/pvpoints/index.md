# pvpoints

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvpoints` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Anzahl der Punkte

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvpoints(punkte)
pvpoints(punkte, reserviert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `reserviert` | Optionaler zusätzlicher Parameter; wird von der aktuellen Implementierung akzeptiert, aber nicht ausgewertet. | Ausdruck / passender Datentyp | ja |

## Beispiele

**Beispiel:** `pvpoints([[2,3],[4,5],[6,3],[-2,4]])`  
**Ergebnis:** 4

| Ausdruck | Ergebnis |
| --- | --- |
| pvpoints(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) | 4 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3401)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6075

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVPoints`.

[Zurück zu Berechnungen](../../../index.md)
