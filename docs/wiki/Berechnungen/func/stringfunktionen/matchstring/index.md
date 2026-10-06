# matchstring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`matchstring` – Stringfunktionen.

## Detaillierte Beschreibung

Prüft ob eine String einem regulären Ausdruck entspricht.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
matchstring(string, regexp)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `regexp` | Parameter der Funktion. | Boolean/Ausdruck | nein |

## Beispiele

**Beispiel:** `matchstring("abcdefg","b.*e")`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| matchstring("abcdefg","b.*e") | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=5029)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `MatchString`.

[Zurück zu Berechnungen](../../../index.md)
