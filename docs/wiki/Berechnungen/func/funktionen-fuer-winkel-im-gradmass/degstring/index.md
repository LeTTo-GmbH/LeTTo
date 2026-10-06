# degstring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`degstring` – Funktionen für Winkel im Gradmaß.

## Detaillierte Beschreibung

erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen Winkel im Bogenmaß einen String der Winkeldarstellung

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
degstring(winkel)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `degstring(0.5)`  
**Ergebnis:** "2°15&#39;22&#39;&#39;"

| Ausdruck | Ergebnis |
| --- | --- |
| degstring(0.5) | &quot;2°15&#39;22&#39;&#39;&quot; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3196)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `DegString`.

[Zurück zu Berechnungen](../../../index.md)
