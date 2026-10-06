# acosh

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`acosh` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Area-Cosinus-Hyperbolicus

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `cosh` im dafür gewählten Zweig. Für den reellen Hauptwert muss x mindestens 1 sein. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
acosh(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `acosh(1.5430806)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| acosh(1.5430806) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3317)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Acosh`.

[Zurück zu Berechnungen](../../../index.md)
