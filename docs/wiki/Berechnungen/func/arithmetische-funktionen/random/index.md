# random

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`random` – arithmetische Funktionen.

## Detaillierte Beschreibung

Zufallszahl aus einem definierten Zahlenbereich random(minimal,maximal) VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet, weshalb sich der Wert bei jedem Anzeigevorgang einer Frage ändert. Sollte sich der berechnete Wert für eine Schülerangabe zwischen Fragestellung und Ergebniskontrolle nicht ändern dürfen (ist der Normalfall) muss man einen Datensatz statt einer Zufallszahl verwenden! Zufallszahlen haben in der Ergebnisberechnung keinen Sinn, und sollten maximal für angezeigte zufällige Werte verwendet werden!

Zufallszahl aus einem definierten Zahlenbereich random(minimal,maximal)<br>VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet, weshalb sich der Wert bei jedem Anzeigevorgang einer Frage ändert. Sollte sich der berechnete Wert für eine Schülerangabe zwischen Fragestellung und Ergebniskontrolle nicht ändern dürfen (ist der Normalfall) muss man einen **Datensatz statt einer Zufallszahl** verwenden! <br> Zufallszahlen haben in der Ergebnisberechnung keinen Sinn, und sollten maximal für angezeigte zufällige Werte verwendet werden!

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
random(minimum)
random(minimum, maximum)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Kleinster möglicher Wert. | Zahl / Ausdruck | nein |
| `maximum` | Größter möglicher Wert. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `random(2,8)`  
**Ergebnis:** 3.4532

| Ausdruck | Ergebnis |
| --- | --- |
| random(2,8) | 3.4532 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3244)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Random`.

[Zurück zu Berechnungen](../../../index.md)
