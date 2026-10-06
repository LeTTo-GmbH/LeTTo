# pvsorty

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvsorty` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Sortiert die Punkte nach steigender y-Koordinate

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
pvsorty(punkte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

## Beispiele

**Beispiel:** `pvsorty([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−7,−9],[2,3],[6,3],[−2,4],[4,5],[−3,5]]

| Ausdruck | Ergebnis |
| --- | --- |
| pvsorty(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;4,5&#93;,&#91;−3,5&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3404)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `CompareVector`.

[Zurück zu Berechnungen](../../../index.md)
