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

| Regex-Zeichen / Operator | Beschreibung | Beispiele |
|---|---|---|
| `.` | Beliebiges Zeichen, außer Zeilenumbruch, abhängig von Flags | `a.c` findet `abc`, `a-c`, `a c` |
| `\` | Escape-Zeichen für Sonderzeichen oder vordefinierte Klassen | `\.` findet einen Punkt; `\\` findet einen Backslash |
| `^` | Anfang einer Zeile oder des gesamten Inputs | `^abc` findet `abc` nur am Anfang |
| `$` | Ende einer Zeile oder des gesamten Inputs | `abc$` findet `abc` nur am Ende |
| `*` | 0 oder mehr Wiederholungen, greedy | `ab*` findet `a`, `ab`, `abb` |
| `+` | 1 oder mehr Wiederholungen, greedy | `ab+` findet `ab`, `abb`, aber nicht `a` |
| `?` | 0 oder 1 Wiederholung, greedy | `colou?r` findet `color` und `colour` |
| `{n}` | Genau `n` Wiederholungen | `\d{4}` findet `2026` |
| `{n,}` | Mindestens `n` Wiederholungen | `\d{2,}` findet `12`, `123`, `1234` |
| `{n,m}` | Zwischen `n` und `m` Wiederholungen | `\d{2,4}` findet `12`, `123`, `1234` |
| `*?` | 0 oder mehr Wiederholungen, reluctant / lazy | `<.*?>` findet möglichst kurze HTML-artige Tags |
| `+?` | 1 oder mehr Wiederholungen, reluctant / lazy | `".+?"` findet den kürzesten Text in Anführungszeichen |
| `??` | 0 oder 1 Wiederholung, reluctant / lazy | `a??` nimmt möglichst wenig |
| `{n}?` | Genau `n` Wiederholungen, reluctant-Variante formal möglich | `\d{3}?` findet 3 Ziffern |
| `{n,}?` | Mindestens `n` Wiederholungen, reluctant / lazy | `\d{2,}?` findet möglichst kurz ab 2 Ziffern |
| `{n,m}?` | Zwischen `n` und `m` Wiederholungen, reluctant / lazy | `\d{2,4}?` findet möglichst kurz |
| `*+` | 0 oder mehr Wiederholungen, possessive | `a*+a` findet in `aaa` nichts, weil nicht zurückgegangen wird |
| `++` | 1 oder mehr Wiederholungen, possessive | `a++a` findet in `aaa` nichts |
| `?+` | 0 oder 1 Wiederholung, possessive | `a?+a` kann weniger Backtracking erlauben |
| `{n}+` | Genau `n` Wiederholungen, possessive | `\d{3}+` findet 3 Ziffern ohne Backtracking |
| `{n,}+` | Mindestens `n` Wiederholungen, possessive | `\d{2,}+` |
| `{n,m}+` | Zwischen `n` und `m` Wiederholungen, possessive | `\d{2,4}+` |
| `[...]` | Zeichenklasse: eines der angegebenen Zeichen | `[abc]` findet `a`, `b` oder `c` |
| `[^...]` | Negierte Zeichenklasse | `[^abc]` findet jedes Zeichen außer `a`, `b`, `c` |
| `[a-z]` | Zeichenbereich | `[a-z]` findet Kleinbuchstaben von `a` bis `z` |
| `[a-zA-Z]` | Mehrere Bereiche in einer Zeichenklasse | `[a-zA-Z]` findet ASCII-Buchstaben |
| `[a-d[m-p]]` | Union von Zeichenklassen | `[a-d[m-p]]` findet `a` bis `d` oder `m` bis `p` |
| `[a-z&&[def]]` | Schnittmenge von Zeichenklassen | `[a-z&&[def]]` findet `d`, `e`, `f` |
| `[a-z&&[^bc]]` | Subtraktion aus Zeichenklasse | `[a-z&&[^bc]]` findet `a`, `d` bis `z` |
| `[a-z&&[^m-p]]` | Bereich aus Zeichenklasse ausschließen | `[a-z&&[^m-p]]` findet `a` bis `l` und `q` bis `z` |
| `\d` | Ziffer | `\d+` findet `123` |
| `\D` | Keine Ziffer | `\D+` findet `abc` |
| `\s` | Whitespace-Zeichen | `\s+` findet Leerzeichen, Tab, Zeilenumbruch |
| `\S` | Kein Whitespace-Zeichen | `\S+` findet ein Wort ohne Leerzeichen |
| `\w` | Wortzeichen | `\w+` findet `abc_123` |
| `\W` | Kein Wortzeichen | `\W+` findet `!? ` |
| `\h` | Horizontaler Whitespace | `\h+` findet Leerzeichen oder Tabulatoren |
| `\H` | Kein horizontaler Whitespace | `\H+` |
| `\v` | Vertikaler Whitespace | `\v+` findet vertikale Whitespace-Zeichen |
| `\V` | Kein vertikaler Whitespace | `\V+` |
| `\R` | Beliebiger Unicode-Zeilenumbruch | `a\Rb` findet `a` gefolgt von Zeilenumbruch und `b` |
| `\n` | Line Feed | `a\nb` findet `a`, Zeilenumbruch, `b` |
| `\r` | Carriage Return | `\r\n` findet Windows-Zeilenende |
| `\t` | Tabulator | `\t+` findet Tabs |
| `\f` | Form Feed | `\f` |
| `\a` | Alarm / Bell | `\a` |
| `\e` | Escape-Zeichen | `\e` |
| `\cx` | Control-Zeichen | `\cM` entspricht Carriage Return |
| `\0n` | Zeichen mit oktalem Wert | `\012` steht für Line Feed |
| `\0nn` | Zeichen mit zweistelligem oktalem Wert | `\040` steht für Leerzeichen |
| `\0mnn` | Zeichen mit dreistelligem oktalem Wert | `\011` steht für Tab |
| `\xhh` | Zeichen mit hexadezimalem Wert | `\x41` findet `A` |
| `\uhhhh` | Unicode-Zeichen mit 4 Hex-Ziffern | `\u0041` findet `A` |
| `\x{h...h}` | Unicode-Codepoint | `\x{1F600}` findet 😀 |
| `\p{Lower}` | POSIX/ASCII-Klasse für Kleinbuchstaben | `\p{Lower}+` |
| `\p{Upper}` | POSIX/ASCII-Klasse für Großbuchstaben | `\p{Upper}+` |
| `\p{ASCII}` | ASCII-Zeichen | `\p{ASCII}+` |
| `\p{Alpha}` | Alphabetische ASCII-Zeichen | `\p{Alpha}+` |
| `\p{Digit}` | ASCII-Ziffern | `\p{Digit}+` |
| `\p{Alnum}` | ASCII-Buchstaben oder Ziffern | `\p{Alnum}+` |
| `\p{Punct}` | ASCII-Interpunktionszeichen | `\p{Punct}+` |
| `\p{Graph}` | Sichtbare ASCII-Zeichen | `\p{Graph}+` |
| `\p{Print}` | Druckbare ASCII-Zeichen | `\p{Print}+` |
| `\p{Blank}` | Leerzeichen oder Tab | `\p{Blank}+` |
| `\p{Cntrl}` | Steuerzeichen | `\p{Cntrl}` |
| `\p{XDigit}` | Hexadezimale Ziffer | `\p{XDigit}+` findet `09AFaf` |
| `\p{Space}` | Whitespace | `\p{Space}+` |
| `\p{IsLatin}` | Unicode-Skript Latin | `\p{IsLatin}+` findet lateinische Buchstaben |
| `\p{InGreek}` | Unicode-Block Greek | `\p{InGreek}+` findet griechische Zeichen |
| `\p{Lu}` | Unicode-Kategorie Großbuchstabe | `\p{Lu}+` findet `ABC` |
| `\p{Ll}` | Unicode-Kategorie Kleinbuchstabe | `\p{Ll}+` findet `abc` |
| `\p{L}` | Unicode-Buchstabe | `\p{L}+` findet Buchstaben vieler Sprachen |
| `\p{N}` | Unicode-Zahl | `\p{N}+` |
| `\p{Sc}` | Währungssymbol | `\p{Sc}` findet `€`, `$` |
| `\P{...}` | Negierte Unicode-Klasse | `\P{L}+` findet Nicht-Buchstaben |
| `\b` | Wortgrenze | `\bJava\b` findet `Java` als eigenes Wort |
| `\B` | Keine Wortgrenze | `\Bend` findet `end` nicht am Wortanfang |
| `\A` | Anfang des gesamten Inputs | `\Aabc` findet `abc` nur ganz am Anfang |
| `\G` | Ende des vorherigen Matches | `\G,?\w+` kann fortlaufend Token lesen |
| `\Z` | Ende des Inputs, erlaubt finalen Zeilenabschluss | `abc\Z` |
| `\z` | Absolutes Ende des Inputs | `abc\z` |
| `|` | Alternative / Oder | `cat|dog` findet `cat` oder `dog` |
| `(...)` | Capturing Group | `(ab)+` findet `ab`, `abab` |
| `(?:...)` | Non-Capturing Group | `(?:ab)+` gruppiert ohne Capture |
| `(?<name>...)` | Benannte Capturing Group | `(?<year>\d{4})` |
| `\1`, `\2`, ... | Rückreferenz auf Capturing Group | `(.)\1` findet doppelte Zeichen wie `aa` |
| `\k<name>` | Rückreferenz auf benannte Gruppe | `(?<x>.)\k<x>` findet doppelte Zeichen |
| `(?=...)` | Positive Lookahead | `\d+(?=€)` findet Zahl vor `€` |
| `(?!...)` | Negative Lookahead | `\d+(?!€)` findet Zahl, wenn danach kein `€` kommt |
| `(?<=...)` | Positive Lookbehind | `(?<=ID-)\d+` findet Zahl nach `ID-` |
| `(?<!...)` | Negative Lookbehind | `(?<!ID-)\d+` findet Zahl, die nicht direkt nach `ID-` steht |
| `(?>...)` | Atomic Group | `(?>a+)a` findet in `aaa` nichts |
| `(?idmsuxU-idmsuxU)` | Flags innerhalb des Regex setzen oder entfernen | `(?i)abc` findet `abc`, `ABC`, `Abc` |
| `(?idmsuxU-idmsuxU:...)` | Flags nur für eine Gruppe setzen | `(?i:abc)def` macht nur `abc` case-insensitive |
| `(?i)` | Case-insensitive Matching aktivieren | `(?i)java` findet `Java`, `JAVA` |
| `(?d)` | Unix-Lines-Modus | `(?d)^abc$` beeinflusst Zeilenende-Verhalten |
| `(?m)` | Multiline-Modus | `(?m)^abc` findet `abc` am Anfang jeder Zeile |
| `(?s)` | Dotall-Modus: `.` findet auch Zeilenumbrüche | `(?s)<body>.*</body>` |
| `(?u)` | Unicode-aware Case Folding | `(?iu)straße` |
| `(?x)` | Kommentare und Whitespace im Regex erlauben | `(?x) \d{4} - \d{2} - \d{2}` |
| `(?U)` | Unicode Character Classes aktivieren | `(?U)\w+` berücksichtigt Unicode stärker |
| `\Q...\E` | Literal-Quoting: Inhalt wird wörtlich behandelt | `\Q.*?\E` findet exakt `.*?` |
| `\c` | Escape eines einzelnen Sonderzeichens, wenn sinnvoll | `\+` findet `+`, `\*` findet `*` |
| `\.` | Literal-Punkt | `file\.txt` findet `file.txt` |
| `\*` | Literal-Stern | `3\*4` findet `3*4` |
| `\+` | Literal-Plus | `C\+\+` findet `C++` |
| `\?` | Literal-Fragezeichen | `ja\?` findet `ja?` |
| `\(` und `\)` | Literale Klammern | `\(test\)` findet `(test)` |
| `\[` und `\]` | Literale eckige Klammern | `\[abc\]` findet `[abc]` |
| `\{` und `\}` | Literale geschweifte Klammern | `\{id\}` findet `{id}` |
| `\^` | Literal-Caret | `\^abc` findet `^abc` |
| `\$` | Literal-Dollarzeichen | `\$\d+` findet `$100` |
| `\-` | Literal-Bindestrich in Zeichenklasse, wenn nötig | `[a\-z]` findet `a`, `-` oder `z` |
| `&&` | Schnittmenge innerhalb einer Zeichenklasse | `[a-z&&[aeiou]]` findet Vokale |
| `.` in `[...]` | Punkt ist innerhalb einer Zeichenklasse meist literal | `[.]` findet `.` |
| `*` in `[...]` | Stern ist innerhalb einer Zeichenklasse literal | `[*]` findet `*` |
| `+` in `[...]` | Plus ist innerhalb einer Zeichenklasse literal | `[+]` findet `+` |
| `?` in `[...]` | Fragezeichen ist innerhalb einer Zeichenklasse literal | `[?]` findet `?` |
| `^` in `[...]` | Am Anfang negiert es, sonst literal | `[^0-9]` negiert; `[a^b]` findet `a`, `^`, `b` |
| `-` in `[...]` | Definiert Bereich, außer escaped oder am Rand | `[a-z]` Bereich; `[-az]` literal `-` |
| `]` in `[...]` | Muss escaped werden, wenn es literal gemeint ist | `[\]]` findet `]` |
| `\1` bis `\9` | Numerische Backreferences | `(\d\d)-\1` findet `12-12` |
| `$1`, `$2`, ... | Gruppenreferenzen im Replacement-String, nicht im Regex selbst | `replaceAll("(\\d+)", "[$1]")` macht aus `123` → `[123]` |
| `${name}` | Benannte Gruppenreferenz im Replacement-String | `replaceAll("(?<x>\\d+)", "${x}")` |

## Reguläre Ausdrücke bei der [Zieleinheit](../ZielEinheit/index.md) bei der Verwendung eines Suchmusters
* basieren auf Java Regular Expressions, werden aber durch einen Präprozesser aus dem Suchmuster erstellt
