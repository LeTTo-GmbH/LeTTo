# plugin

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`plugin` – Auswertung und Programmierung.

## Detaillierte Beschreibung

Ruft die Berechnungsmethode des Plugins, welches als erster Stringparameter angegeben werden muss auf und übergibt die weiteren Parameter an die Berechnungsmethode des Plugins.

## Syntax

```text
plugin(pluginname, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `pluginname` | Parameter der Funktion. | String | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | ja, beliebig oft |

## Beispiele

**Beispiel:** `plugin("plugin1",3)`  
**Ergebnis:** führt die Berechnung des Plugins mit dem Namen "plugin1" mit dem Parameter 3 aus.

| Ausdruck | Ergebnis |
| --- | --- |
| plugin("plugin1",3) | führt die Berechnung des Plugins mit dem Namen "plugin1" mit dem Parameter 3 aus. |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3478)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Plugin`.

[Zurück zu Berechnungen](../../../index.md)
