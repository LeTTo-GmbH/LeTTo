# Reguläre Ausdrücke
Regluäre Ausdrücke definieren Suchmuster für Zeichenketten und werden in LeTTo an folgenden Positionen verwenden:
* In der [Zieleinheit](../ZielEinheit/index.md) einer Teilfrage um Muster für die Schülereingabe zu definieren
* In einer Teilfrage mit dem Fragetyp regexp
* Im Parser (Maxima-Feld bzw. Berechnungsfelder - siehe [Berechnungen](../Berechnungen/index.md#stringfunktionen)) in den Funktionen 
  * replaceallstring()
  * replacefirststring()
  * matchstring()

## Reguläre Ausdrücke in Berechnungsfeldern und regexp-Teilfragen
* Hier werden die Reglären Ausdrücke mit Java-Syntax verwendet

#### Java Regular Expressions – Zeichen und Operatoren

| Regex-Zeichen / Operator      | Beschreibung                                                   | Beispiele                                                                  |
|-------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------|
| .                             | Beliebiges Zeichen, außer Zeilenumbruch, abhängig von Flags    | a.c findet abc, a-c, a c                                                   |
| &#92;                         | Escape-Zeichen für Sonderzeichen oder vordefinierte Klassen    | &#92;. findet einen Punkt; &#92;&#92; findet einen Backslash               |
| ^                             | Anfang einer Zeile oder des gesamten Inputs                    | ^abc findet abc nur am Anfang                                              |
| $                             | Ende einer Zeile oder des gesamten Inputs                      | abc$ findet abc nur am Ende                                                |
| *                             | 0 oder mehr Wiederholungen, greedy                             | ab* findet a, ab, abb                                                      |
| +                             | 1 oder mehr Wiederholungen, greedy                             | ab+ findet ab, abb, aber nicht a                                           |
| ?                             | 0 oder 1 Wiederholung, greedy                                  | colou?r findet color und colour                                            |
| {n}                           | Genau n Wiederholungen                                         | &#92;d{4} findet 2026                                                      |
| {n,}                          | Mindestens n Wiederholungen                                    | &#92;d{2,} findet 12, 123, 1234                                            |
| {n,m}                         | Zwischen n und m Wiederholungen                                | &#92;d{2,4} findet 12, 123, 1234                                           |
| *?                            | 0 oder mehr Wiederholungen, reluctant / lazy                   | <.*?> findet möglichst kurze HTML-artige Tags                              |
| +?                            | 1 oder mehr Wiederholungen, reluctant / lazy                   | ".+?" findet den kürzesten Text in Anführungszeichen                       |
| ??                            | 0 oder 1 Wiederholung, reluctant / lazy                        | a?? nimmt möglichst wenig                                                  |
| {n}?                          | Genau n Wiederholungen, reluctant-Variante formal möglich      | &#92;d{3}? findet 3 Ziffern                                                |
| {n,}?                         | Mindestens n Wiederholungen, reluctant / lazy                  | &#92;d{2,}? findet möglichst kurz ab 2 Ziffern                             |
| {n,m}?                        | Zwischen n und m Wiederholungen, reluctant / lazy              | &#92;d{2,4}? findet möglichst kurz                                         |
| *+                            | 0 oder mehr Wiederholungen, possessive                         | a*+a findet in aaa nichts, weil nicht zurückgegangen wird                  |
| ++                            | 1 oder mehr Wiederholungen, possessive                         | a++a findet in aaa nichts                                                  |
| ?+                            | 0 oder 1 Wiederholung, possessive                              | a?+a kann weniger Backtracking erlauben                                    |
| {n}+                          | Genau n Wiederholungen, possessive                             | &#92;d{3}+ findet 3 Ziffern ohne Backtracking                              |
| {n,}+                         | Mindestens n Wiederholungen, possessive                        | &#92;d{2,}+                                                                |
| {n,m}+                        | Zwischen n und m Wiederholungen, possessive                    | &#92;d{2,4}+                                                               |
| &#91;...&#93;                 | Zeichenklasse: eines der angegebenen Zeichen                   | &#91;abc&#93; findet a, b oder c                                           |
| &#91;^...&#93;                | Negierte Zeichenklasse                                         | &#91;^abc&#93; findet jedes Zeichen außer a, b, c                          |
| &#91;a-z&#93;                 | Zeichenbereich                                                 | &#91;a-z&#93; findet Kleinbuchstaben von a bis z                           |
| &#91;a-zA-Z&#93;              | Mehrere Bereiche in einer Zeichenklasse                        | &#91;a-zA-Z&#93; findet ASCII-Buchstaben                                   |
| &#91;a-d&#91;m-p&#93;&#93;    | Union von Zeichenklassen                                       | &#91;a-d&#91;m-p&#93;&#93; findet a bis d oder m bis p                     |
| &#91;a-z&&&#91;def&#93;&#93;  | Schnittmenge von Zeichenklassen                                | &#91;a-z&&&#91;def&#93;&#93; findet d, e, f                                |
| &#91;a-z&&&#91;^bc&#93;&#93;  | Subtraktion aus Zeichenklasse                                  | &#91;a-z&&&#91;^bc&#93;&#93; findet a, d bis z                             |
| &#91;a-z&&&#91;^m-p&#93;&#93; | Bereich aus Zeichenklasse ausschließen                         | &#91;a-z&&&#91;^m-p&#93;&#93; findet a bis l und q bis z                   |
| &#92;d                        | Ziffer                                                         | &#92;d+ findet 123                                                         |
| &#92;D                        | Keine Ziffer                                                   | &#92;D+ findet abc                                                         |
| &#92;s                        | Whitespace-Zeichen                                             | &#92;s+ findet Leerzeichen, Tab, Zeilenumbruch                             |
| &#92;S                        | Kein Whitespace-Zeichen                                        | &#92;S+ findet ein Wort ohne Leerzeichen                                   |
| &#92;w                        | Wortzeichen                                                    | &#92;w+ findet abc_123                                                     |
| &#92;W                        | Kein Wortzeichen                                               | &#92;W+ findet !?                                                          |
| &#92;h                        | Horizontaler Whitespace                                        | &#92;h+ findet Leerzeichen oder Tabulatoren                                |
| &#92;H                        | Kein horizontaler Whitespace                                   | &#92;H+                                                                    |
| &#92;v                        | Vertikaler Whitespace                                          | &#92;v+ findet vertikale Whitespace-Zeichen                                |
| &#92;V                        | Kein vertikaler Whitespace                                     | &#92;V+                                                                    |
| &#92;R                        | Beliebiger Unicode-Zeilenumbruch                               | a&#92;Rb findet a gefolgt von Zeilenumbruch und b                          |
| &#92;n                        | Line Feed                                                      | a&#92;nb findet a, Zeilenumbruch, b                                        |
| &#92;r                        | Carriage Return                                                | &#92;r&#92;n findet Windows-Zeilenende                                     |
| &#92;t                        | Tabulator                                                      | &#92;t+ findet Tabs                                                        |
| &#92;f                        | Form Feed                                                      | &#92;f                                                                     |
| &#92;a                        | Alarm / Bell                                                   | &#92;a                                                                     |
| &#92;e                        | Escape-Zeichen                                                 | &#92;e                                                                     |
| &#92;cx                       | Control-Zeichen                                                | &#92;cM entspricht Carriage Return                                         |
| &#92;0n                       | Zeichen mit oktalem Wert                                       | &#92;012 steht für Line Feed                                               |
| &#92;0nn                      | Zeichen mit zweistelligem oktalem Wert                         | &#92;040 steht für Leerzeichen                                             |
| &#92;0mnn                     | Zeichen mit dreistelligem oktalem Wert                         | &#92;011 steht für Tab                                                     |
| &#92;xhh                      | Zeichen mit hexadezimalem Wert                                 | &#92;x41 findet A                                                          |
| &#92;uhhhh                    | Unicode-Zeichen mit 4 Hex-Ziffern                              | &#92;u0041 findet A                                                        |
| &#92;x{h...h}                 | Unicode-Codepoint                                              | &#92;x{1F600} findet 😀                                                    |
| &#92;p{Lower}                 | POSIX/ASCII-Klasse für Kleinbuchstaben                         | &#92;p{Lower}+                                                             |
| &#92;p{Upper}                 | POSIX/ASCII-Klasse für Großbuchstaben                          | &#92;p{Upper}+                                                             |
| &#92;p{ASCII}                 | ASCII-Zeichen                                                  | &#92;p{ASCII}+                                                             |
| &#92;p{Alpha}                 | Alphabetische ASCII-Zeichen                                    | &#92;p{Alpha}+                                                             |
| &#92;p{Digit}                 | ASCII-Ziffern                                                  | &#92;p{Digit}+                                                             |
| &#92;p{Alnum}                 | ASCII-Buchstaben oder Ziffern                                  | &#92;p{Alnum}+                                                             |
| &#92;p{Punct}                 | ASCII-Interpunktionszeichen                                    | &#92;p{Punct}+                                                             |
| &#92;p{Graph}                 | Sichtbare ASCII-Zeichen                                        | &#92;p{Graph}+                                                             |
| &#92;p{Print}                 | Druckbare ASCII-Zeichen                                        | &#92;p{Print}+                                                             |
| &#92;p{Blank}                 | Leerzeichen oder Tab                                           | &#92;p{Blank}+                                                             |
| &#92;p{Cntrl}                 | Steuerzeichen                                                  | &#92;p{Cntrl}                                                              |
| &#92;p{XDigit}                | Hexadezimale Ziffer                                            | &#92;p{XDigit}+ findet 09AFaf                                              |
| &#92;p{Space}                 | Whitespace                                                     | &#92;p{Space}+                                                             |
| &#92;p{IsLatin}               | Unicode-Skript Latin                                           | &#92;p{IsLatin}+ findet lateinische Buchstaben                             |
| &#92;p{InGreek}               | Unicode-Block Greek                                            | &#92;p{InGreek}+ findet griechische Zeichen                                |
| &#92;p{Lu}                    | Unicode-Kategorie Großbuchstabe                                | &#92;p{Lu}+ findet ABC                                                     |
| &#92;p{Ll}                    | Unicode-Kategorie Kleinbuchstabe                               | &#92;p{Ll}+ findet abc                                                     |
| &#92;p{L}                     | Unicode-Buchstabe                                              | &#92;p{L}+ findet Buchstaben vieler Sprachen                               |
| &#92;p{N}                     | Unicode-Zahl                                                   | &#92;p{N}+                                                                 |
| &#92;p{Sc}                    | Währungssymbol                                                 | &#92;p{Sc} findet €, $                                                     |
| &#92;P{...}                   | Negierte Unicode-Klasse                                        | &#92;P{L}+ findet Nicht-Buchstaben                                         |
| &#92;b                        | Wortgrenze                                                     | &#92;bJava&#92;b findet Java als eigenes Wort                              |
| &#92;B                        | Keine Wortgrenze                                               | &#92;Bend findet end nicht am Wortanfang                                   |
| &#92;A                        | Anfang des gesamten Inputs                                     | &#92;Aabc findet abc nur ganz am Anfang                                    |
| &#92;G                        | Ende des vorherigen Matches                                    | &#92;G,?&#92;w+ kann fortlaufend Token lesen                               |
| &#92;Z                        | Ende des Inputs, erlaubt finalen Zeilenabschluss               | abc&#92;Z                                                                  |
| &#92;z                        | Absolutes Ende des Inputs                                      | abc&#92;z                                                                  |
| &#124;                        | Alternative / Oder                                             | cat&#124;dog findet cat oder dog                                           |
| (...)                         | Capturing Group                                                | (ab)+ findet ab, abab                                                      |
| (?:...)                       | Non-Capturing Group                                            | (?:ab)+ gruppiert ohne Capture                                             |
| (?<name>...)                  | Benannte Capturing Group                                       | (?<year>&#92;d{4})                                                         |
| &#92;1, &#92;2, ...           | Rückreferenz auf Capturing Group                               | (.)&#92;1 findet doppelte Zeichen wie aa                                   |
| &#92;k<name>                  | Rückreferenz auf benannte Gruppe                               | (?<x>.)&#92;k<x> findet doppelte Zeichen                                   |
| (?=...)                       | Positive Lookahead                                             | &#92;d+(?=€) findet Zahl vor €                                             |
| (?!...)                       | Negative Lookahead                                             | &#92;d+(?!€) findet Zahl, wenn danach kein € kommt                         |
| (?<=...)                      | Positive Lookbehind                                            | (?<=ID-)&#92;d+ findet Zahl nach ID-                                       |
| (?<!...)                      | Negative Lookbehind                                            | (?<!ID-)&#92;d+ findet Zahl, die nicht direkt nach ID- steht               |
| (?>...)                       | Atomic Group                                                   | (?>a+)a findet in aaa nichts                                               |
| (?idmsuxU-idmsuxU)            | Flags innerhalb des Regex setzen oder entfernen                | (?i)abc findet abc, ABC, Abc                                               |
| (?idmsuxU-idmsuxU:...)        | Flags nur für eine Gruppe setzen                               | (?i:abc)def macht nur abc case-insensitive                                 |
| (?i)                          | Case-insensitive Matching aktivieren                           | (?i)java findet Java, JAVA                                                 |
| (?d)                          | Unix-Lines-Modus                                               | (?d)^abc$ beeinflusst Zeilenende-Verhalten                                 |
| (?m)                          | Multiline-Modus                                                | (?m)^abc findet abc am Anfang jeder Zeile                                  |
| (?s)                          | Dotall-Modus: . findet auch Zeilenumbrüche                     | (?s)<body>.*</body>                                                        |
| (?u)                          | Unicode-aware Case Folding                                     | (?iu)straße                                                                |
| (?x)                          | Kommentare und Whitespace im Regex erlauben                    | (?x) &#92;d{4} - &#92;d{2} - &#92;d{2}                                     |
| (?U)                          | Unicode Character Classes aktivieren                           | (?U)&#92;w+ berücksichtigt Unicode stärker                                 |
| &#92;Q...&#92;E               | Literal-Quoting: Inhalt wird wörtlich behandelt                | &#92;Q.*?&#92;E findet exakt .*?                                           |
| &#92;c                        | Escape eines einzelnen Sonderzeichens, wenn sinnvoll           | &#92;+ findet +, &#92;* findet *                                           |
| &#92;.                        | Literal-Punkt                                                  | file&#92;.txt findet file.txt                                              |
| &#92;*                        | Literal-Stern                                                  | 3&#92;*4 findet 3*4                                                        |
| &#92;+                        | Literal-Plus                                                   | C&#92;+&#92;+ findet C++                                                   |
| &#92;?                        | Literal-Fragezeichen                                           | ja&#92;? findet ja?                                                        |
| &#92;( und &#92;)             | Literale Klammern                                              | &#92;(test&#92;) findet (test)                                             |
| &#92;&#91; und &#92;&#93;     | Literale eckige Klammern                                       | &#92;&#91;abc&#92;&#93; findet &#91;abc&#93;                               |
| &#92;{ und &#92;}             | Literale geschweifte Klammern                                  | &#92;{id&#92;} findet {id}                                                 |
| &#92;^                        | Literal-Caret                                                  | &#92;^abc findet ^abc                                                      |
| &#92;$                        | Literal-Dollarzeichen                                          | &#92;$&#92;d+ findet $100                                                  |
| &#92;-                        | Literal-Bindestrich in Zeichenklasse, wenn nötig               | &#91;a&#92;-z&#93; findet a, - oder z                                      |
| &&                            | Schnittmenge innerhalb einer Zeichenklasse                     | &#91;a-z&&&#91;aeiou&#93;&#93; findet Vokale                               |
| . in &#91;...&#93;            | Punkt ist innerhalb einer Zeichenklasse meist literal          | &#91;.&#93; findet .                                                       |
| * in &#91;...&#93;            | Stern ist innerhalb einer Zeichenklasse literal                | &#91;*&#93; findet *                                                       |
| + in &#91;...&#93;            | Plus ist innerhalb einer Zeichenklasse literal                 | &#91;+&#93; findet +                                                       |
| ? in &#91;...&#93;            | Fragezeichen ist innerhalb einer Zeichenklasse literal         | &#91;?&#93; findet ?                                                       |
| ^ in &#91;...&#93;            | Am Anfang negiert es, sonst literal                            | &#91;^0-9&#93; negiert; &#91;a^b&#93; findet a, ^, b                       |
| - in &#91;...&#93;            | Definiert Bereich, außer escaped oder am Rand                  | &#91;a-z&#93; Bereich; &#91;-az&#93; literal -                             |
| &#93; in &#91;...&#93;        | Muss escaped werden, wenn es literal gemeint ist               | &#91;&#92;&#93;&#93; findet &#93;                                          |
| &#92;1 bis &#92;9             | Numerische Backreferences                                      | (&#92;d&#92;d)-&#92;1 findet 12-12                                         |
| $1, $2, ...                   | Gruppenreferenzen im Replacement-String, nicht im Regex selbst | replaceAll("(&#92;&#92;d+)", "&#91;$1&#93;") macht aus 123 → &#91;123&#93; |
| ${name}                       | Benannte Gruppenreferenz im Replacement-String                 | replaceAll("(?<x>&#92;&#92;d+)", "${x}")                                   |

## Reguläre Ausdrücke bei der [Zieleinheit](../ZielEinheit/index.md) bei der Verwendung eines Suchmusters
* basieren auf Java Regular Expressions, werden aber durch einen Präprozesser aus dem Suchmuster erstellt
