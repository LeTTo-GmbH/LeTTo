# removeunit

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`removeunit` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

entfernt bei einem Ausdruck alle Einheiten und ersetzt dabei alle einheitenbehafteten Größen durch den Zahlenwert bezogen auf die BasisEinheit des SI-Systems

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
removeunit(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `removeunit(t*5'm/s'+4cm)`  
**Ergebnis:** t*5+0.04

| Ausdruck | Ergebnis |
| --- | --- |
| removeunit(t*5'm/s'+4cm) | t*5+0.04 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3179)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `RemoveUnit`.

[Zurück zu Berechnungen](../../../index.md)
