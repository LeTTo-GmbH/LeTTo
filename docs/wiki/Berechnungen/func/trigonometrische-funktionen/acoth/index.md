# acoth

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`acoth` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Area-Cotangens-Hyperbolicus

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `coth` im dafür gewählten Zweig. Für einen endlichen reellen Rückgabewert muss der Betrag von x größer 1 sein. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
acoth(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `acoth(1.313035)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| acoth(1.313035) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3319)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Acoth`.

[Zurück zu Berechnungen](../../../index.md)
