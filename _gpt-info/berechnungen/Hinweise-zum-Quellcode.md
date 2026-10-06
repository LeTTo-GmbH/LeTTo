# Beim Dokumentieren festgestellte Abweichungen

Diese Hinweise beziehen sich auf die mitgelieferten Dateien; sie sind keine Aussagen über andere Versionen. Die Implementierung selbst wurde nicht verändert.

| Element | Feststellung und Behandlung in der Dokumentation |
| --- | --- |
| `bimp`, Infix `imp` | Klasse IMP verwendet für Ganzzahlen `a.not().or(b)`. Für 13 und 10 ergibt sich -5, nicht der ursprünglich angegebene Wert 8. Bei booleschen Werten steht `!(a || b)` im Code, also NOR statt der üblichen Implikation. Die Detailseiten beschreiben das tatsächliche Verhalten. Die konkrete Registrierung von `imp` ist nicht mitgeliefert; die Zuordnung folgt der ursprünglichen Übersicht. |
| `pulse` | Die Java-Implementierung schließt beide Randpunkte ein; die ursprüngliche Beschreibung verwendet strikte Ungleichungen. Die Intervalldefinition wurde korrigiert. |
| `round` | Klasse Round akzeptiert genau einen Parameter. Die Parameterreferenz nennt zusätzlich eine Variante mit Kommastellen; diese wurde aus der Syntax entfernt und durch einen Hinweis auf `cround` ersetzt. |
| `isNearInteger`, `ni` | Bei zwei Parametern wird im Code `params[0]` als Toleranz gelesen, obwohl der zweite Parameter dafür dokumentiert ist. Dieser Widerspruch ist auf den Seiten erläutert. |
| `bitstream` | Positive und negative Gruppengrößen gruppieren von unterschiedlichen Seiten. Gruppengröße 0 führt im vorhandenen Code zu einem leeren String. Beide Randfälle sind beschrieben. |
| `date`, `time` | Einzelne String- und Vektorargumente werden separat behandelt. Ein einzelnes Zahlenargument wird nicht als Jahr bzw. Stunde ausgewertet. Die Syntax und Parametertabellen wurden auf diesen Code abgestimmt. |
| `datestring`, `timestring`, `datetimestring` | Die Implementierung erwartet als erstes Argument einen Ganzzahlwert. Der Formatstring ist optional. Die ursprüngliche Parametertabelle wurde korrigiert. |
| `forloop` | Fünf oder sechs Parameter; die optionale Aggregation fehlte in der ausführlichen Parametertabelle. Sie ist ergänzt. |
| `viewpow`, `viewsqrt` | Der optionale Modus 0, 1 oder 2 war im erläuternden Text beschrieben, fehlte aber in der Parameterreferenz. Er ist auf den Seiten enthalten. |
| `pvfunc` | Die Parameter heißen fachlich Funktion, Variable, Start, Ende und Schrittweite. Die ursprünglichen Namen `varlist` und `isnumeric` waren irreführend. Der Endwert wird nicht eingeschlossen. |
| `polynom` | Die Hilfe nennt einen parameterlosen Aufruf; der Code greift stets auf das erste Argument zu. Dieser Aufruf wurde aus den empfohlenen Varianten entfernt. |
| `par` | Die Implementierung verarbeitet mehrere Werte, obwohl die Parameterreferenz nur einen oder zwei nennt. Die Syntax beschreibt die variable Parameteranzahl. |
| `setcut`, `setunion` | Die Kurzsyntax nennt nur den parameterlosen Sonderfall. Die eigentlichen Mengenargumente sind jetzt ebenfalls dokumentiert. |
| `numdif` | Verwendet eine Vorwärtsdifferenz. Der Fehlertext spricht vom zweiten Parameter als Variable, geprüft wird aber der dritte. Die Dokumentation benennt die richtige Position. |
| `numint` | Implementiert eine Trapezsumme mit standardmäßig 1000 Teilintervallen. Die optionale Anzahl wurde präzisiert. |
| `optorder` | Die Implementierung des Erhaltungsmodus hat Switch-Fallthrough. Die beabsichtigte Entfernung des Wrappers bei numerischem Ergebnis ist deshalb nicht für alle Modi gesichert. |
| Beispiele für `diff`, `bxor`, `originunit`, `e12up`, `e12down` | Offensichtliche Ergebnis- bzw. Funktionsnamensfehler wurden berichtigt. |
| `%k` | Der angegebene Wert mit Einheit J/K ist die Boltzmann-Konstante; die alte Bezeichnung „Stefan Bolzman“ wurde korrigiert. Der numerische Wert der Vorlage bleibt erhalten. |

Die bereitgestellten Quellen enthalten weitere interne Klassen ohne einen in der Übersicht belegten Funktionsnamen. Daraus wurden keine zusätzlichen öffentlichen Parserfunktionen erfunden. Für eine vollständige Schnittstellen- und Versionsprüfung wären die Funktionsregistrierung und die Git-Historie erforderlich.
