# setsub

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setsub` – Mengen-Funktionen.

## Detaillierte Beschreibung

setsub(M,x,y) Liefert eine Teilmenge von M der Elemente vom index x bis zum Index y

## Syntax

```text
setsub(v1, von, bis)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Vektor / Ganzzahl | nein |

## Beispiele

**Beispiel:** `setsub([1,3,-2,4],1,2)`  
**Ergebnis:** [3,-2]

| Ausdruck | Ergebnis |
| --- | --- |
| setsub(&#91;1,3,-2,4&#93;,1,2) | &#91;3,-2&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3380)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetSub`.

[Zurück zu Berechnungen](../../../index.md)
