# asinh

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`asinh` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Area-Sinus-Hyperbolicus

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `sinh` im dafür gewählten Zweig. Für jeden reellen Eingabewert ist ein reeller Rückgabewert definiert. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
asinh(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `asinh(1.1752012)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| asinh(1.1752012) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3316)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Asinh`.

[Zurück zu Berechnungen](../../../index.md)
