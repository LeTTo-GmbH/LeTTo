# setunion

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setunion` – Mengen-Funktionen.

## Detaillierte Beschreibung

Fügt mehrere Mengen zu einer neuen Menge zusammen

### Anwendung und Besonderheiten

Die Funktion verkettet die Elemente der übergebenen Werte und Vektoren. Mehrfach vorkommende Elemente bleiben erhalten; für eine Vereinigung ohne Duplikate wird `setunionnd` verwendet. Ohne Parameter entsteht ein leerer Vektor.

## Syntax

```text
setunion()
setunion(menge1, menge2, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| mengen | Werte oder Vektoren, welche zusammengeführt werden sollen. Ohne Argumente wird ein leerer Vektor geliefert. | Wert / Vektor | ja, beliebig oft |

## Beispiele


**Beispiel:** `setunion([1,3,2,4],[3,7])`  
**Ergebnis:** [1,3,2,4,3,7]

| Ausdruck | Ergebnis |
| --- | --- |
| setunion(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;1,3,2,4,3,7&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3364)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetUnion`.

[Zurück zu Berechnungen](../../../index.md)
