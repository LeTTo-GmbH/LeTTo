# randomC

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`randomC` – arithmetische Funktionen.

## Detaillierte Beschreibung

komplexe Zufallszahl aus einem definierten Zahlenbereich für den Betrag VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet!

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
randomC(minimum)
randomC(minimum, maximum)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Kleinster möglicher Betrag. | Zahl / Ausdruck | nein |
| `maximum` | Größter möglicher Betrag. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `randomC(2,8)`  
**Ergebnis:** 3.4532arg40.3°

| Ausdruck | Ergebnis |
| --- | --- |
| randomC(2,8) | 3.4532arg40.3° |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3245)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `RandomC`.

[Zurück zu Berechnungen](../../../index.md)
