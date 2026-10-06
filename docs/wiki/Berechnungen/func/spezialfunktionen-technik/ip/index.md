# ip

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ip` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

Wandelt eine Long-Zahl in einen String als IP-Adresse um, oder 4 Byte-Zahlen in eine Long Zahl als IP-32-bit-Adresse

## Syntax

```text
ip(e1)
ip(e1, e2, e3, e4)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | String / Ganzzahl | nein |
| `e2` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |
| `e3` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |
| `e4` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |

## Beispiele

**Beispiel:** `ip(1534536453) ip(10,20,30,40)`  
**Ergebnis:** "91.119.43.5" 169090600

| Ausdruck | Ergebnis |
| --- | --- |
| ip(1534536453)<br>ip(10,20,30,40) | "91.119.43.5"<br>169090600 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3501)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `IP`.

[Zurück zu Berechnungen](../../../index.md)
