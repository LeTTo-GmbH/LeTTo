# setcut

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setcut` – Mengen-Funktionen.

## Detaillierte Beschreibung

Bildet die Schnittmenge aus mehreren Mengen

### Anwendung und Besonderheiten

Die Funktion bildet die Schnittmenge der übergebenen Werte und Vektoren. Ohne Parameter entsteht ein leerer Vektor. Die aus der Hilfe übernommene Kurzsyntax `setcut()` beschreibt nur diesen Sonderfall; für eine Schnittmenge werden mehrere Mengen angegeben.

## Syntax

```text
setcut()
setcut(menge1, menge2, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| mengen | Werte oder Vektoren, welche zusammengeführt werden sollen. Ohne Argumente wird ein leerer Vektor geliefert. | Wert / Vektor | ja, beliebig oft |

## Beispiele


**Beispiel:** `setcut([1,3,2,4],[3,7])`  
**Ergebnis:** [3]

| Ausdruck | Ergebnis |
| --- | --- |
| setcut(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;3&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3366)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetCut`.

[Zurück zu Berechnungen](../../../index.md)
