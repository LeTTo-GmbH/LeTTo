# deg

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`deg` – Funktionen für Winkel im Gradmaß.

## Detaillierte Beschreibung

erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen WinkelString einen Winkel im Bogenmaß

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
deg(string)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

## Beispiele

**Beispiel:** `deg([2,15,22]) deg("2°15&#39;22&#39;&#39;")`  
**Ergebnis:** 2.25611111111°

| Ausdruck | Ergebnis |
| --- | --- |
| deg(&#91;2,15,22&#93;) <br> deg(&quot;2°15&#39;22&#39;&#39;&quot;) | 2.25611111111° |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3195)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Deg`.

[Zurück zu Berechnungen](../../../index.md)
