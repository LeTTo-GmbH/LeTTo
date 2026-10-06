# wenn

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`wenn` – Auswertung und Programmierung.

## Detaillierte Beschreibung

if(bedingung,wahr,falsch)

Alias/Kompatibilitätsname zu `if`.

Bedingungsfunktion wenn(bedingung,wahrwert,falschwert). Im Prinzip identisch wie if, jedoch kann if mit Maxima nicht verwendet werden.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [if](../if/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 3 Argumente.

Die erste Angabe ist eine Bedingung, die zweite der Ausdruck für den wahren und die dritte der Ausdruck für den falschen Fall. Die Funktionsschreibweise des Parsers unterscheidet sich von Maximas `if ... then ... else ...`.

## Syntax

```text
wenn(e1, e2, e3)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e3` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

## Beispiele

**Beispiel:** `wenn(4<6,10,12)`  
**Ergebnis:** 10

| Ausdruck | Ergebnis |
| --- | --- |
| wenn(4&lt;6,10,12) | 10 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3477)

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
