# floor

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`floor` – arithmetische Funktionen.

## Detaillierte Beschreibung

Rundet auf die größte ganze Zahl, welche kleiner oder gleich x ist

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Rundet in Richtung minus unendlich. Deshalb ergibt `floor(-2.3)` den Wert -3. Dies unterscheidet sich vom Abschneiden der Nachkommastellen mit `trunc`.

## Syntax

```text
floor(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `floor(24.5)`  
**Ergebnis:** 24

| Ausdruck | Ergebnis |
| --- | --- |
| floor(24.5) | 24 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3224)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Floor`.

[Zurück zu Berechnungen](../../../index.md)
