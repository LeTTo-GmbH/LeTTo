# periodic

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`periodic` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion periodic(Variable,Periodendauer,Funktion) periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion)

## Syntax

```text
periodic(variable, periodeExtern, periodeIntern, funktion)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `periodeExtern` | Parameter der Funktion. | Variable | nein |
| `periodeIntern` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

## Beispiele

**Beispiel:** `ch1(t):periodic(t,5ms,2'Vms-2'*t^2) ch1(t):periodic(t,5ms,1,2V*t^2)`  
**Ergebnis:** !100px-ClipCapIt-190318-113524.PNG !100px-ClipCapIt-190318-113644.PNG

| Ausdruck | Ergebnis |
| --- | --- |
| ch1(t):periodic(t,5ms,2'Vms-2'*t^2) <br> ch1(t):periodic(t,5ms,1,2V*t^2) | <br>![100px-ClipCapIt-190318-113524.PNG](../../../100px-ClipCapIt-190318-113524.PNG) <br> <br>![100px-ClipCapIt-190318-113644.PNG](../../../100px-ClipCapIt-190318-113644.PNG) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3274)

## Bildschirmhardcopys

![100px-ClipCapIt-190318-113524.PNG](../../../100px-ClipCapIt-190318-113524.PNG)

![100px-ClipCapIt-190318-113644.PNG](../../../100px-ClipCapIt-190318-113644.PNG)

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Periodic`.

[Zurück zu Berechnungen](../../../index.md)
