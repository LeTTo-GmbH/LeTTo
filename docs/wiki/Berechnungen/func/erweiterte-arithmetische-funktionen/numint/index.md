# numint

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`numint` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

numerische Integration numint(untereGrenze,obereGrenze,funktion,Variable) numint(untereGrenze,obereGrenze,funktion,Variable,punkteAnzahl)

### Anwendung und Besonderheiten

Berechnet eine numerische Näherung des bestimmten Integrals mit einer Trapezsumme. Ohne fünften Parameter werden 1.000 Teilintervalle verwendet. Die Grenzen müssen kompatible Einheiten besitzen; ein Nullwert wird bei der Einheitenprüfung gesondert behandelt. Der vierte Parameter muss eine Variable sein. Weitere Argumente werden im mitgelieferten Code eingelesen, beeinflussen die Berechnung aber nicht.

## Syntax

```text
numint(untergrenze, obergrenze, funktion, variable)
numint(untergrenze, obergrenze, funktion, variable, anzahl)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| untergrenze | Beginn des Integrationsintervalls. | Zahl, ggf. mit Einheit | nein |
| obergrenze | Ende des Integrationsintervalls. | Zahl, gleiche Einheit wie Untergrenze | nein |
| funktion | Zu integrierender Ausdruck. | Ausdruck | nein |
| variable | Integrationsvariable. | Variable | nein |
| anzahl | Anzahl Teilintervalle; Standard 1000. Der Code übernimmt Werte größer 9 und kleiner 1000000000. | Ganzzahl / numerischer Wert | ja |

## Beispiele

**Beispiel:** `numint(0,2pi,sin(t),t)`  
**Ergebnis:** 0

| Ausdruck | Ergebnis |
| --- | --- |
| numint(0,2pi,sin(t),t) | 0 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3275)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NumInt`.

[Zurück zu Berechnungen](../../../index.md)
