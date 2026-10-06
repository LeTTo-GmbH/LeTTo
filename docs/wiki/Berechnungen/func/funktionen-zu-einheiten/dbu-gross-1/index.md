# dBu

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dBu` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. Hinweis: Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V.

Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. **Hinweis:** Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
dBu(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `dBu(1uW)`  
**Ergebnis:** 0dBu

| Ausdruck | Ergebnis |
| --- | --- |
| dBu(1uW) | 0dBu |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `DBu`.

[Zurück zu Berechnungen](../../../index.md)
