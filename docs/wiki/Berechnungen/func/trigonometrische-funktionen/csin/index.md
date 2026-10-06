# csin

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`csin` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Erzeugt aus einer komplexen Zahl (Effektivwert) und einer Frequenz einen Sinusfunktion in der Zeit

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 3 Argumente.

Der komplexe Zeiger beschreibt den Effektivwert. Die Amplitude des erzeugten Sinus ist daher `sqrt(2)*cabs(zeiger)`. Ohne weitere Argumente werden die Variablen `f` und `t` verwendet; eine Frequenz kann als zweiter und eine Zeitvariable als dritter Parameter angegeben werden.

## Syntax

```text
csin(zeiger)
csin(zeiger, frequenz)
csin(zeiger, frequenz, zeitvariable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeiger` | Parameter der Funktion. | Zahl/Ausdruck | nein |
| `frequenz` | Parameter der Funktion. | Zahl / Ausdruck | ja |
| `zeitvariable` | Parameter der Funktion. | Variable | ja |

## Beispiele

**Beispiel:** `csin(U)`  
**Ergebnis:** sqrt(2)*cabs(U)*sin(2*pi*f*t+carg(U))

| Ausdruck | Ergebnis |
| --- | --- |
| csin(U) | sqrt(2)*cabs(U)*sin(2*pi*f*t+carg(U)) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3320)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `CSin`.

[Zurück zu Berechnungen](../../../index.md)
