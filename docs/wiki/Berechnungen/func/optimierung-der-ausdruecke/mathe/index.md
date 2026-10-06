# mathe

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mathe` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Wertet Ganzzahlen und Konstanten numerisch nur soweit aus, wie es der symbolische Mathematikmodus zulässt; ein symbolisches Ergebnis bleibt in `mathe(...)` erhalten.

### Anwendung und Besonderheiten

Erzwingt den symbolischen Mathematikmodus für den übergebenen Ausdruck. Ganzzahlen und Konstanten werden in diesem Modus zusammengefasst; verbleibende symbolische Teile bleiben als Ausdruck erhalten.

## Syntax

```text
mathe(ausdruck)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Im Mathematikmodus auszuwertender Ausdruck. | Zahl / Ausdruck | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| mathe(2+3+x) | mathe(5+x) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `MatheOpt`.

[Zurück zu Berechnungen](../../../index.md)
