# setmakelist

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setmakelist` – Mengen-Funktionen.

## Detaillierte Beschreibung

setmakelist(f,x,start,stop) setzt in den Ausdruck f für x die Werte von start bis stop mit einer Schrittweite von 1 ein.

### Anwendung und Besonderheiten

Wertet den ersten Ausdruck für die Werte einer Variable aus und sammelt die Ergebnisse in einem Vektor. Die Werte stammen entweder aus einem Vektor oder aus Startwert, Endwert und optionaler Schrittweite. Ohne explizite Schrittweite wird 1 in der passenden Einheit verwendet. Der Endwert wird eingeschlossen, sofern er mit der Schrittweite erreicht wird. Bei Schrittweite 0 werden im Code nur Start- und Endwert als Stützwerte übernommen.

## Syntax

```text
setmakelist(ausdruck, variable, werte)
setmakelist(ausdruck, variable, start, ende)
setmakelist(ausdruck, variable, start, ende, schrittweite)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Für jeden Variablenwert auszuwertender Ausdruck. | Ausdruck | nein |
| variable | Laufvariable. | Variable | nein |
| werte / start | Vektor von Laufwerten oder Startwert eines Bereichs. | Vektor / Zahl | nein |
| ende | Endwert beim Bereichsaufruf. | Zahl | nur Bereichsaufruf |
| schrittweite | Abstand der Laufwerte; Standard 1 in passender Einheit. | Zahl | ja |

## Beispiele

**Beispiel:** `setmakelist(x^2,x,1,4)`  
**Ergebnis:** [ 1,4,9,16 ]

| Ausdruck | Ergebnis |
| --- | --- |
| setmakelist(x^2,x,1,4) | &#91; 1,4,9,16 &#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3381)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetMakeList`.

[Zurück zu Berechnungen](../../../index.md)
