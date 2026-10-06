# lnot

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`lnot` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen lnot )

Alias/Kompatibilitätsname zu `not`.

logisches NICHT, wie not jedoch wird es von Maxima nicht ausgewertet

### Anwendung und Besonderheiten

Die logische Negation erwartet in der mitgelieferten Klasse LNOT einen booleschen Wert. Bei anderen numerischen Typen wirft sie einen Datentypfehler.

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [not](../not/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
lnot(bedingung)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `bedingung` | Parameter der Funktion. | Ausdruck | nein |

## Beispiele

**Beispiel:** `lnot(a<b)`

| Ausdruck | Ergebnis |
| --- | --- |
| lnot(a&lt;b) | In der Übersicht nicht angegeben. |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3193)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateLogicalOperators.java`, Klasse `LNOT`.

[Zurück zu Berechnungen](../../../index.md)
