# originunit

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`originunit` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 zurück. originnumeric(x)*originunit(x) liefert wieder x

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Gibt die ursprüngliche Darstellungseinheit als Größe mit Zahlenwert 1 zurück. Das Präfix bleibt erhalten: `originunit(3.1kA)` ergibt 1 kA.

## Syntax

```text
originunit(oE)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `originunit(3.1kA) originunit(5%)`  
**Ergebnis:** 1kA 1%

| Ausdruck | Ergebnis |
| --- | --- |
| originunit(3.1kA) <br> originunit(5%) | 1kA <br> 1% |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3181)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `OriginUnit`.

[Zurück zu Berechnungen](../../../index.md)
