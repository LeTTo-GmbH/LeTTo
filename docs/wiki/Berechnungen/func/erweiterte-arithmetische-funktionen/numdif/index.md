# numdif

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`numdif` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

numerisches Differenzieren einer Funktion "funktion" nach einer Variablen "Variable" an der Stelle "position" mit einer Differenz der Variablen von "differenz" numdif(position,funktion,Variable,differenz)

### Anwendung und Besonderheiten

Berechnet eine Vorwärtsdifferenz: `(f(position + schrittweite) - f(position))/schrittweite`. Das Ergebnis ist eine Näherung, keine symbolisch exakte Ableitung. Die Schrittweite darf nicht 0 sein. Die unabhängige Variable ist der dritte Parameter; der Fehlertext im Code spricht an dieser Stelle irrtümlich vom zweiten Parameter.

## Syntax

```text
numdif(position, funktion, variable, schrittweite)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `position` | Stelle, an der differenziert wird. | Zahl / Ausdruck | nein |
| `funktion` | Zu differenzierender Ausdruck. | Ausdruck | nein |
| `variable` | Variable, nach der differenziert wird. | Variable | nein |
| `schrittweite` | Differenz für die numerische Ableitung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `numdif(0,sin(t),t,0.01)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| numdif(0,sin(t),t,0.01) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3276)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NumDif`.

[Zurück zu Berechnungen](../../../index.md)
