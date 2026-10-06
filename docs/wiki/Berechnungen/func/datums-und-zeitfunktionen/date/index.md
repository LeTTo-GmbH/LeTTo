# date

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`date` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

date(y,m,d,h,min,sec) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00

date(y,m,d) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00

### Anwendung und Besonderheiten

Das Datum wird als Ganzzahl in Sekunden ab 01.01.0000 gespeichert, nicht als Unix-Zeitstempel. Fehlende Komponenten haben die Vorgaben Jahr 0, Monat 1, Tag 1 und Uhrzeit 00:00:00. Ein einzelnes Stringargument wird über `Datum.toDateInteger` eingelesen; ein einzelner Vektor enthält bis zu sechs einheitenlose numerische Komponenten. Ein einzelner Zahlenparameter wird im mitgelieferten Code nicht als Jahr ausgewertet.

## Syntax

```text
date()
date(jahr, monat)
date(jahr, monat, tag)
date(jahr, monat, tag, stunde)
date(jahr, monat, tag, stunde, minute)
date(jahr, monat, tag, stunde, minute, sekunde)
date(komponentenvektor)
date(datumsstring)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| jahr | Jahr; Vorgabe 0. | einheitenlose Zahl | ja |
| monat | Monat; Vorgabe 1. | einheitenlose Zahl | ja |
| tag | Tag; Vorgabe 1. | einheitenlose Zahl | ja |
| stunde | Stunde; Vorgabe 0. | einheitenlose Zahl | ja |
| minute | Minute; Vorgabe 0. | einheitenlose Zahl | ja |
| sekunde | Sekunde; Vorgabe 0. | einheitenlose Zahl | ja |
| komponentenvektor / datumsstring | Alternativer einzelner Parameter anstelle der Komponentenliste. | Vektor / String | alternative Aufrufvariante |

## Beispiele

```text
date(2026,10,6)
```

Anwendungsbeispiel; das Ergebnis folgt aus den oben beschriebenen Parametern.

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3634)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6530

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `FuncDate`.

[Zurück zu Berechnungen](../../../index.md)
