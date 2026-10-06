# cssin

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cssin` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Erzeugt aus einer komplexen Zahl, die als Spitzenwert interpretiert wird, eine Sinusfunktion. `cssin(U)`, `cssin(U,f)` oder `cssin(U,f,x)`.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 3 Argumente.

Der komplexe Zeiger beschreibt den Spitzenwert. Daher lautet die Amplitude direkt `cabs(zeiger)`, ohne den Faktor sqrt(2). Ohne weitere Argumente werden die Variablen `f` und `t` verwendet.

## Syntax

```text
cssin(zeiger)
cssin(zeiger, frequenz)
cssin(zeiger, frequenz, zeitvariable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeiger` | Parameter der Funktion. | Zahl/Ausdruck | nein |
| `frequenz` | Parameter der Funktion. | Zahl / Ausdruck | ja |
| `zeitvariable` | Parameter der Funktion. | Variable | ja |

## Beispiele

**Beispiel:** `cssin(U)`  
**Ergebnis:** cabs(U)*sin(2*pi*f*t+carg(U))

| Ausdruck | Ergebnis |
| --- | --- |
| cssin(U) | cabs(U)*sin(2*pi*f*t+carg(U)) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `CSSin`.

[Zurück zu Berechnungen](../../../index.md)
