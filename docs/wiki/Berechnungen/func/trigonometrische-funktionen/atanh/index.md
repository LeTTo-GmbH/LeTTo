# atanh

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`atanh` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Area-Tangens-Hyperbolicus

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `tanh` im dafür gewählten Zweig. Für einen endlichen reellen Rückgabewert muss der Betrag von x kleiner 1 sein. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
atanh(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `atanh(0.7615941)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| atanh(0.7615941) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3318)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Atanh`.

[Zurück zu Berechnungen](../../../index.md)
