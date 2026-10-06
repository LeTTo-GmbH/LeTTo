# Auswertung und Programmierung

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [dataset](dataset/index.md) | liefert alle Datensätze einer Datensatz-Definition in einem Vektor DEMO-Beispiel |
| [ev](ev/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden DEMO-Beispiel |
| [evruntime](evruntime/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Das **Einsetzen erfolgt erst bei der Ergebnisberechnung**! DEMO-Beispiel |
| [forloop](forloop/index.md) | Führt eine Zählschleife aus forloop(Variable,Startwert,Wiederholbedingung,Inkrement,Ausdruck,Aggregatsfunktion). Ohne Aggregatsfunktion wird ein Feld mit den Ergebnissen der Schleifeniterationen geliefert. DEMO-Beispiel |
| [if](if/index.md) | Bedingungsfunktion if(bedingung,wahrwert,falschwert) DEMO-Beispiel |
| [nv](nv/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Im Gegensatz zu ev werden bestehende Variable nur in den Gleichungen, aber nicht im Ausdruck selbst eingesetzt! DEMO-Beispiel |
| [plugin](plugin/index.md) | Ruft die Berechnungsmethode des Plugins, welches als erster Stringparameter angegeben werden muss auf und übergibt die weiteren Parameter an die Berechnungsmethode des Plugins. DEMO-Beispiel |
| [runtime](runtime/index.md) | Bei dieser Funktion wird **erst bei der Berechnung der Frageantwort, nach dem Einsetzen der Datensätze** das **komplette Maxima-Feld** mit dem internen **Parser** durchgerechnet und danach der Parameter-Ausdruck berechnet. Dadurch kann man bei komplizierten Berechnungen eine sehr aufwendige symbolische Berechnung verhindern! DEMO-Beispiel |
| [symbolic](symbolic/index.md) | Bei allen Variablen innerhalb von symbolic werden nur nicht-numerische Werte eingesetzt! Wird vor allem im Angabtext bei {= } verwendet DEMO-Beispiel |
| [wenn](wenn/index.md) | Bedingungsfunktion wenn(bedingung,wahrwert,falschwert). Im Prinzip identisch wie if, jedoch kann if mit Maxima nicht verwendet werden. DEMO-Beispiel |
