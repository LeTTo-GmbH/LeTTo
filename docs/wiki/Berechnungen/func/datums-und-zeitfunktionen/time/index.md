# time

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`time` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

time(h,min,sec) erzeugt eine Uhrzeit als Ganzzahl in Sekunden seit Mitternacht

### Anwendung und Besonderheiten

Bei mehreren Zahlenargumenten werden Stunde, Minute und Sekunde verwendet; fehlende Komponenten sind 0. Ein Vektor enthält bis zu drei Komponenten. Ein einzelnes Zahlenargument wird in dieser Implementierung nicht als Stundenwert ausgewertet. Die Umwandlung eines Strings verwendet `Datum.toDateInteger`; der genaue zulässige Stringsyntax ist in den mitgelieferten Dateien nicht enthalten. Der Aufruf `time(12,30,0)` liefert einen numerischen Uhrzeitwert.

## Syntax

```text
time()
time(stunde, minute)
time(stunde, minute, sekunde)
time(komponentenvektor)
time(zeitstring)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| stunde | Stundenkomponente; Standard 0. | einheitenlose Zahl | ja |
| minute | Minutenkomponente; Standard 0. | einheitenlose Zahl | ja |
| sekunde | Sekundenkomponente; Standard 0. | einheitenlose Zahl | ja |
| komponentenvektor / zeitstring | Einzelner alternativer Parameter anstelle der Komponentenliste. | Vektor / String | alternative Aufrufvariante |

## Beispiele

```text
time(12,30,0)
```

Anwendungsbeispiel; das Ergebnis folgt aus den oben beschriebenen Parametern.

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3635)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6762

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `FuncTime`.

[Zurück zu Berechnungen](../../../index.md)
