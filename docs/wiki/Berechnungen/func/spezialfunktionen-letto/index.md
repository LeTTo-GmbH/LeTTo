# Spezialfunktionen LeTTo

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [declare](declare/index.md) | Deklariert Variablentypen für die Maxima-Kompatibilität. Die Funktion ist im internen Parser derzeit noch nicht funktional umgesetzt und liefert dort `false`. |
| [delay](delay/index.md) | **Test-/Diagnosefunktion:** verzögert die Auswertung um die angegebene Anzahl Sekunden und prüft dabei regelmäßig auf einen Timeout/Abbruch. |
| [infiniteloop](infiniteloop/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich eine Endlosschleife und dient zum Testen der Timeout-Behandlung. Nicht für reguläre Aufgaben verwenden. |
| [parser](parser/index.md) | Markierungsfunktion für Ausdrücke, die von Maxima unverändert an den internen Parser weitergereicht werden sollen. Im internen Parser selbst wird lediglich der einzelne Parameter ausgewertet. |
| [points](points/index.md) | Berechnet die erreichbare Gesamtpunkteanzahl einer Frage DEMO-Beispiel |
| [runtimeexception](runtimeexception/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich eine RuntimeException. Ein optionaler Parameter wird als Fehlermeldung verwendet. |
| [selective_kill](selective-kill/index.md) | Löscht alle Variablen aus dem Variablenspeicher außer den angegebenen Variablen bzw. Variablenvektoren und liefert die Anzahl der gelöschten Variablen. |
| [stackoverflow](stackoverflow/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich einen StackOverflow. Nicht für reguläre Aufgaben verwenden. |
