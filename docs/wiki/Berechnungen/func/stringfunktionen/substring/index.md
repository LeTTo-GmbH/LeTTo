# substring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`substring` – Stringfunktionen.

## Detaillierte Beschreibung

Liefert einen Teil eines Strings substring(string,startindex,endindex). Index beginnt bei 0 und endindex ist optional.

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 3 Argumente.

## Syntax

```text
substring(string, startindex)
substring(string, startindex, endindex)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `startindex` | Parameter der Funktion. | Ganzzahl | nein |
| `endindex` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `substring("abcdefg",2,3)`  
**Ergebnis:** "cd"

| Ausdruck | Ergebnis |
| --- | --- |
| substring("abcdefg",2,3) | "cd" |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=5025)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `SubString`.

[Zurück zu Berechnungen](../../../index.md)
