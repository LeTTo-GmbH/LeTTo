# pvget

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvget` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Liefert einen Punkt der Punkteliste.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
pvget(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |

## Beispiele

**Beispiel:** `pvget([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [4,5]

| Ausdruck | Ergebnis |
| --- | --- |
| pvget(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;4,5&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3389)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVGet`.

[Zurück zu Berechnungen](../../../index.md)
