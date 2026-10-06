# polgrad

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`polgrad` – komplexe Zahlen.

## Detaillierte Beschreibung

Erzeugt aus Betrag und einem Winkel im Gradmaß eine komplexe Zahl.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
polgrad(betrag, winkel)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `betrag` | Parameter der Funktion. | Zahl | nein |
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `polgrad(5,53.130102°/1°)`  
**Ergebnis:** 3+4*%i

| Ausdruck | Ergebnis |
| --- | --- |
| polgrad(5,53.130102°/1°) | 3+4*%i |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `PolGrad`.

[Zurück zu Berechnungen](../../../index.md)
