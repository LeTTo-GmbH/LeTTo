# Enums des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* Paket `at.letto.plugins.enums`; Enums werden in JSON als Name des Werts übertragen.

| Enum | Beschreibung | Werte |
|---|---|---|
| [CALCERGEBNISTYPE](CALCERGEBNISTYPE/index.md) | Mögliche Typen für [CalcErgebnisDto](../dtos/CalcErgebnisDto/index.md) bei reiner String-Übertragung | `CALCULATE`, `STRING`, `ERROR` |
| [CALCMODE](CALCMODE/index.md) | Art der Berechnung MAXIMA : Berechnung im Maxima-Feld einer Frage LOESUNG : Berechnung der Lösung aus dem Lösungsfeld EQUALS : Vergleich des Ergebnisses des Schülers mit dem Ergebnis des Lehrers VIEW : Berechnungen direkt mit Angabefeld mit {= | `MAXIMA`, `LOESUNG`, `EQUALS`, `VIEW` |
| [IMAGEUNIT](IMAGEUNIT/index.md) | Einheiten welche für die Größenangaben von Bildern verwendet werden können none : keine Angabe der Dateigröße px : Pixel pt : Punkte cm : Zentimeter percent : Prozent der Bildschirmbreite em : Vielfache der Standardschriftgröße | `none`, `px`, `pt`, `cm`, `percent`, `em` |
| [InputElement](InputElement/index.md) | Definiert das Eingabeelement für die Subquestion, deren Typ auf Plugin gesetzt ist | `TextField`, `TextArea`, `Button`, `MULTICHOICE`, `XHTML`, `SourceCode`, `JAVASCRIPT` |
| [ORIENTATIONX](ORIENTATIONX/index.md) | Horizontale Ausrichtung eines Textes an seinem Bezugspunkt | `LEFT`, `CENTER`, `RIGHT` |
| [ORIENTATIONY](ORIENTATIONY/index.md) | Vertikale Ausrichtung eines Textes an seinem Bezugspunkt | `BOTTOM`, `CENTER`, `TOP` |
| [SHOWPOTENZ](SHOWPOTENZ/index.md) | Gibt an, ob eine Potenz als Potenz oder als Wurzel dargestellt werden soll AUTO : Die Darstellung wird automatisch festgelegt POW : Potenzen werden als Potenz dargestellt SQRT : Wenn es sinnvoll ist, werden Potenzen als Wurzel dargestellt | `AUTO`, `POW`, `SQRT` |
| [Score](Score/index.md) | Ergebnis einer Fragen-Beurteilung NotScored : nicht bewertet, da das richtige Ergebnis nicht bekannt ist | `NotScored`, `OK`, `FALSCH`, `TEILWEISE_OK`, `EINHEITENFEHLER`, `OK_Lehrer`, `FALSCH_Lehrer`, `TEILWEISE_OK_Lehrer`, `EINHEITENFEHLER_Lehrer`, `ANGABEFEHLER_EH`, `PARSERFEHLER_SYSTEM`, `NichtEntschieden`, `MEHRFACHANTWORT_OK`, `MEHRFACHANTWORT_OK_LEHRER`, `MEHRFACHANTWORT_TW_RICHTIG`, `MEHRFACHANTWORT_TW_RICHTIG_LEHRER` |
| [TOLERANZMODE](TOLERANZMODE/index.md) | Art der Toleranzverarbeitung RELATIV : Die Toleranz wird relativ zum größeren Wert des Vergleiches bestimmt ABSOLUT : Die Toleranz wird absolut angegeben und ist von den Werten unabhängig | `RELATIV`, `ABSOLUT` |

[Referenz-Plugin (Java)](../index.md)
