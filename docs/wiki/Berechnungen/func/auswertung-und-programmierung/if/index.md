# if

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`if` – Auswertung und Programmierung.

## Detaillierte Beschreibung

if(bedingung,wahr,falsch)

Bedingungsfunktion if(bedingung,wahrwert,falschwert)

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 3 Argumente.

Die erste Angabe ist eine Bedingung, die zweite der Ausdruck für den wahren und die dritte der Ausdruck für den falschen Fall. Die Funktionsschreibweise des Parsers unterscheidet sich von Maximas `if ... then ... else ...`.

## Syntax

```text
if(e1, e2, e3)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e3` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

## Beispiele

**Beispiel:** `Wenn-Funktion`  
**Ergebnis:** 10

| Ausdruck | Ergebnis |
| --- | --- |
| if(4&lt;6,10,12) | 10 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3476)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `IF`.

[Zurück zu Berechnungen](../../../index.md)
