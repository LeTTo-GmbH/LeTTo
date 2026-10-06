# Prüfung des Dokumentationspakets

Geprüfter Stand: 06.10.2026.

| Prüfung | Ergebnis |
| --- | --- |
| Funktionsseiten | 396, einschließlich aller 394 Einträge der ausführlichen Parameterreferenz sowie float und mathe |
| Operatorseiten | 37, getrennt nach Infix, Prefix und Suffix |
| Konstantenseiten | 15 |
| Klammerseiten | 3 |
| Einzelbeschreibungen insgesamt | 451 |
| Themenübersichten | 28 |
| Alphabetische Funktionsübersicht | vorhanden |
| Angepasste Hauptseite | vorhanden; lange Parameterreferenz entfernt |
| Vollständigkeit der neun Inhaltsabschnitte | alle 451 Elementseiten besitzen alle Abschnitte |
| Relative interne Markdown-Verweise | 3040 geprüfte Verweise, kein fehlendes Ziel |
| Rückverweise | auf jeder Elementseite vorhanden und auflösbar |
| Funktionslinks in der Hauptübersicht | alle 396 Ziele vorhanden und verlinkt |
| Alte Platzhalterlinks in Funktionstabellen | keine |
| Demo-IDs der Vorlage | alle 285 eindeutigen IDs erhalten |
| Bildverweise der Vorlage | alle 10 unterschiedlichen Bildnamen erhalten |
| Dateinamen auf Dateisystemen ohne Beachtung der Groß-/Kleinschreibung | keine Kollisionen |
| Belegte Einführungsrevisionen | bei 63 Funktionen übernommen |
| Nicht belegte Revisionen / Codeänderungsdaten | ausdrücklich als nicht ermittelbar gekennzeichnet |

Die Linkprüfung betrifft die gelieferten Markdown-Dateien innerhalb von `wiki/Berechnungen`. Die referenzierten Nachbarkapitel, Demoanwendung und Bilder müssen im bestehenden Repository vorhanden sein. Ihre Inhalte sind nicht mitgeliefert und wurden nicht online überprüft.

Die Beispiele und Beschreibungen wurden anhand der gelieferten Dokumentation und ausgewählter Java-Implementierungen geprüft bzw. präzisiert. Dies ist kein vollständiger Laufzeittest der Parserfunktionen. Die Funktionsregistrierung, Hilfsklassen und Projektabhängigkeiten fehlen im isolierten Quellcodepaket; ein GitHub-Pages-Build mit dem tatsächlichen Repository wurde nicht ausgeführt.
