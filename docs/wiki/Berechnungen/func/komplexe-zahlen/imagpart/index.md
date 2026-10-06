# imagpart

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`imagpart` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert den Imaginärteil einer komplexen Zahl

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` wird `b` zurückgegeben, also der Koeffizient von `%i`, nicht das Produkt `b*%i`.

## Syntax

```text
imagpart(re)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `imagpart(3+4*%i)`  
**Ergebnis:** 4

| Ausdruck | Ergebnis |
| --- | --- |
| imagpart(3+4*%i) | 4 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3333)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Im`.

[Zurück zu Berechnungen](../../../index.md)
