# optorder

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`optorder` – Optimierung der Ausdrücke.

## Detaillierte Beschreibung

Optimiert nur die symbolische Reihenfolge des Ausdrucks. Optional steuert ein zweiter ganzzahliger Modus, ob bzw. wie lange die Funktion im Ausdruck erhalten bleibt.

### Anwendung und Besonderheiten

Optimiert den Ausdruck im Modus für symbolische Reihenfolge. Ein optionaler ganzzahliger Modus bestimmt die Erhaltung des Funktionsaufrufs. Der Code behandelt die Modi 0, 1, 2, 11, 12 und 13; 0 liefert den Ausdruck ohne Wrapper, 2 erhält den Wrapper dauerhaft. Bei Modus 1 kann der Switch im mitgelieferten Code ohne break in Modus 2 weiterlaufen. Deshalb sollte die ursprünglich beschriebene Entfernung bei numerischem Ergebnis nicht als garantiert angesehen werden.

## Syntax

```text
optorder(ausdruck)
optorder(ausdruck, modus)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Umzuordnender Ausdruck. | Ausdruck | nein |
| modus | Erhaltung des Funktionsaufrufs; siehe Besonderheiten. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `optorder(y+x)`  
**Ergebnis:** x+y

| Ausdruck | Ergebnis |
| --- | --- |
| optorder(y+x) | x+y |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `OptOrder`.

[Zurück zu Berechnungen](../../../index.md)
