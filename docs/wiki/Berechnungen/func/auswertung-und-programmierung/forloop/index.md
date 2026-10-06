# forloop

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`forloop` – Auswertung und Programmierung.

## Detaillierte Beschreibung

Führt eine Zählschleife aus forloop(Variable,Startwert,Wiederholbedingung,Inkrement,Ausdruck,Aggregatsfunktion). Ohne Aggregatsfunktion wird ein Feld mit den Ergebnissen der Schleifeniterationen geliefert.

### Anwendung und Besonderheiten

Es werden fünf oder sechs Parameter erwartet. Die sechste Angabe ist eine Aggregatsfunktion als String; ohne sie wird ein Vektor der Einzelergebnisse zurückgegeben. Die Wiederholbedingung muss boolesch auswertbar sein. Die Implementierung bricht bei mehr als 1.000.000 Iterationen mit einem Fehler ab. Das Inkrement ist ein Ausdruck wie `i++` oder `i:i+2`.

Die Implementierung erwartet 5 bis 6 Argumente.

## Syntax

```text
forloop(variable, startwert, bedingung, inkrement, ausdruck)
forloop(variable, startwert, bedingung, inkrement, ausdruck, aggregation)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Schleifenvariable. | Variable | nein |
| `startwert` | Startwert der Schleifenvariable. | Zahl / Ausdruck | nein |
| `bedingung` | Bedingung für die Fortsetzung der Schleife. | Ausdruck | nein |
| `inkrement` | Ausdruck, der die Schleifenvariable verändert. | Ausdruck | nein |
| `ausdruck` | Pro Schleifendurchlauf auszuwertender Ausdruck. | Ausdruck | nein |
| `aggregation` | Verknüpft die Einzelergebnisse, z. B. `"+"`; fehlt dieser Parameter, entsteht ein Vektor. | String | ja, sechster Parameter |

## Beispiele

**Beispiel:** `forloop(i,1,i<7,i++,i,"+") forloop(i,1,i<7,i:i+2,i)`  
**Ergebnis:** 21 [1,3,5]

| Ausdruck | Ergebnis |
| --- | --- |
| forloop(i,1,i&lt;7,i++,i,"+")<br>forloop(i,1,i&lt;7,i:i+2,i) | 21<br>&#91;1,3,5&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3486)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6077

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Loop`.

[Zurück zu Berechnungen](../../../index.md)
