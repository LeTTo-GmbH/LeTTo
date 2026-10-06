# getvars

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`getvars` – Polynome.

## Detaillierte Beschreibung

Liefert alle im Ausdruck vorkommenden Variablennamen als Vektor von Strings.

## Syntax

```text
getvars(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `getvars(x^2+a*y)`  
**Ergebnis:** ["a","x","y"]

| Ausdruck | Ergebnis |
| --- | --- |
| getvars(x^2+a*y) | &#91;"a","x","y"&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `GetVars`.

[Zurück zu Berechnungen](../../../index.md)
