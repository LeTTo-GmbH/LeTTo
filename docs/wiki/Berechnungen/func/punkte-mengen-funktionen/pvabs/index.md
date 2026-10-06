# pvabs

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvabs` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt den Betrag eines Punktes oder aller Ortsvektoren zu den Punkten.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
pvabs(punkte)
pvabs(punkte, index)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `pvabs([[2,3],[4,5],[6,3],[-2,4]]) pvabs([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [3.6056,6.4031,6.7082,4.4721] 6.4031

| Ausdruck | Ergebnis |
| --- | --- |
| pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;3.6056,6.4031,6.7082,4.4721&#93; <br> 6.4031 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3387)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVAbs`.

[Zurück zu Berechnungen](../../../index.md)
