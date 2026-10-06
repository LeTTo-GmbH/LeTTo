# Optimierung der Ausdrücke

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [aopt](aopt/index.md) | Bei Maxima und Lösung geht die Funktion verloren, nur innerhalb von noopt bleibt sie erhalten. Bei der Anzeige führt sie zur Optimierung das Ausdruckes nach Einsetzen der Datensätze. |
| [lnoopt](lnoopt/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nicht mehr optimiert. |
| [lopt](lopt/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. DEMO-Beispiel |
| [loptnumeric](loptnumeric/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nur numerisch optimiert. |
| [mathe](mathe/index.md) | Wertet Ganzzahlen und Konstanten numerisch nur soweit aus, wie es der symbolische Mathematikmodus zulässt; ein symbolisches Ergebnis bleibt in `mathe(...)` erhalten. |
| [noopt](noopt/index.md) | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion an sich geht aber verloren. DEMO-Beispiel |
| [nopt](nopt/index.md) | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion bleibt erhalten und wird erst bei der Lösungsberechnung oder durch opt() entfernt. DEMO-Beispiel |
| [number](number/index.md) | Erzwingt die numerische Auswertung aller numerisch berechenbaren Teile. Bleibt bei einem weiterhin symbolischen Ergebnis als Funktion erhalten. |
| [opt](opt/index.md) | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden. Nur bei der Verwendung des internen Parser sinnvoll. DEMO-Beispiel |
| [optorder](optorder/index.md) | Optimiert nur die symbolische Reihenfolge des Ausdrucks. Optional steuert ein zweiter ganzzahliger Modus, ob bzw. wie lange die Funktion im Ausdruck erhalten bleibt. |
| [qopt](qopt/index.md) | Im Maximafeld wird alles innerhalb der Funktion nicht ausgewertet und die Funktion bleibt erhalten, bei der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert.  Anwendung findet die Funktion bei boolschen Fragen und Folgefehlerbehandlung. |
| [ratsimp](ratsimp/index.md) | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden (wie opt, wird jedoch auch von Maxima ausgewertet) DEMO-Beispiel |
