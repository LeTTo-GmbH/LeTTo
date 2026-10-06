# nv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`nv` – Auswertung und Programmierung.

## Detaillierte Beschreibung

Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Im Gegensatz zu ev werden bestehende Variable nur in den Gleichungen, aber nicht im Ausdruck selbst eingesetzt!

## Syntax

```text
nv(ausdruck, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `zuweisungen` | Parameter der Funktion. | Ausdruck | ja, beliebig oft |

## Beispiele

**Beispiel:** `nv(x*y,y=4)`  
**Ergebnis:** x*4

| Ausdruck | Ergebnis |
| --- | --- |
| nv(x*y,y=4) | x*4 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3475)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Nv`.

[Zurück zu Berechnungen](../../../index.md)
