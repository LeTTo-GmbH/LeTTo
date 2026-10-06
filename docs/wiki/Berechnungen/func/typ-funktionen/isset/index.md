# isset

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`isset` – Typ-Funktionen.

## Detaillierte Beschreibung

Prüft ob es sich um eine Menge handelt.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Prüft die Form des übergebenen Wertes als Menge bzw. Vektor. Das ist von einer Prüfung auf ausschließlich numerische Elemente (`issetnumeric`) oder ausschließlich ganzzahlige Elemente (`issetlong`) zu unterscheiden.

## Syntax

```text
isset(wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `isset([12,13,14])`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| isset(&#91;12,13,14&#93;) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3422)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `IsSet`.

[Zurück zu Berechnungen](../../../index.md)
