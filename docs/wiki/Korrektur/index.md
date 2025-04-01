# Korrektur von Schülereingaben bei [Mehrfachberechnungsfragen](../BeispielsammlungEditieren/index.md#mehrfachberechnungsfrage) 

Die automatische Korrektur von LeTTo stellt einen wesentlichen Bestandteil von LeTTo dar. 
Sie kann sehr weitreichend parametriert werden. 

## [Zieleinheit](../ZielEinheit/index.md)
* In der [Zieleinheit](../ZielEinheit/index.md) kann das Korrekturverhalten von symbolischen Eingaben und Zahlenwerten wesentlich beeinflusst werden.
* Sie ist im Einheitenfeld der Teilfrage direkt als Text oder mit einem Doppelklick auf das Einheitenfeld per Dialog konfigurierbar.

## Korrektur von Zahlenwerten im Einheit
* Das Ergebnis wird nur als Korrekt gewertet wenn Zahlenwert und Einheit stimmen
* Bei einer falschen Einheit wird der Zahlenwert mit der eingegebenen Einheit auf eine SI-Basiseinheit umgerechnet und mit 
  dem Zahlenwert der korrekten Lösung mit SI-Basiseinheit verglichen<br>
  z.B. korrekt Lösung: 2mV, Eingabe: 20cm^2, verglichen wird 0.002 mit 20*10^-4, ergibt korrekter Zahlenwert mit Einheitenfehler

## Korrektur von symbolischen Ausdrücken
* Ist die korrekte Lösung symbolisch oder die ZielEinheit auf symbol... gesetzt wird symbolisch korrigiert.
* Die Korrektur erfolgt stufenweise
  * zuerst wird der String der Schülereingabe mit dem String der korrekten Lösung verglichen 
  * dann wird durch Umformen verglichen wobei nur die Operationen beim Umformen verwendet werden welche in der Zieleinheit definiert sind.
  * Wenn keine Optimierungsstufe angegeben oder symbolfull gewählt wurde erfolg ein numerischer Vergleich
    * falls es sich um ein Polynom handelt werden dann die Pole und Nullstellen verglichen
    * schlussendlich werden zufällige Zahlenwerte für die Variablen in dem symbolischen Ausdruck eingesetzt und die berechnete Lösung verglichen
      * Da die eingesetzten zufälligen Zahlenwerte keine Einheit haben erfolgt dieser Vergleich immer ohne Einheiten-Überprüfung
      * zufällige Zahlenwerte führen bei manchen Funktionen wie etwa Potenzen zu stark abweichenden Berechnungswerten 
        welche zu einer nicht nachvollziehbaren Zufälligkeit führen
      * Um die Einheiten korrekt prüfen zu können und die Zufälligkeit der Überprüfung zu vermeiden können Testvektoren 
        für die Variablen definiert werden mit denen die Schülereingabe gegen die korrekte Lösung geprüft wird (siehe nächster Punkt).

## Korrektur von symbolischen Ausdrücken mit Testvektoren
* wie im vorigen Punkt erwähnt kann es beim numerischen Vergleich durch Einsetzen von Zahlenwerten 
  zu **numerischen Zufälligkeiten** und nicht Erkennung von **Einheitenfehlern** kommen. Abhilfe schafft die
  Definition von Testvektoren für die verwendeten Variablen eines Ausdrucks.
* Sind keine Testvektoren definiert wird der Ausdruck mit zufälligen Zahlenwerten geprüft.
* Ein Testvektor wird im Maxima-Feld mit "test_" gefolgt vom Variablennamen als Vektor mit den einzusetzenden Werten definiert.<br>
  zB.: 
  <pre>test_x:[3,5,7]m
  </pre>
* Manchmal ist es notwendig bei mehreren Teilfragen verschiedene Testvektoren für die einzelnen Teilfragen zu definieren.
  In diesem Fall wird der Testvektor mit dem Namen der Teilfrage und dem Variablennamen definiert.<br>
  zB.: 
  <pre>test_Q0_x:[3,5,7]m
  test_Q1_x:[4,6,8]m
  </pre>
  Ist test_Q0_x und test_Q1_x definiert wird der Testvektor test_Q0_x für die Teilfrage Q0 und der Testvektor test_Q1_x für die Teilfrage Q1 verwendet.<br>
  Ist nur test_x definiert wird dieser Testvektor für alle Teilfragen verwendet.<br>
  Ist test_Q0_x und test_x definiert wird der Testvektor test_Q0_x für die Teilfrage Q0 und der Testvektor test_x für alle anderene Teilfragen verwendet.<br>
* Gibt es mehrere Variablen werden die Tests jeweils mit den Testvektor-Elementen mit gleichem Modulo-Indizes durchgeführt.<br>
  zB.: 
  <pre>test_x:[2,4,5]
  test_y:[1,7]
  </pre>
  Es wird die Prüfung mit den Paaren (x=2,y=1),(x=4,y=7) und (y=5,y=1) durchgeführt.
* Die Genauigkeit der Prüfung (Toleranz) bezieht sich beim Test mit Testvektoren immer auf das Ergebnis des Ausdruckes mit eingesetzten Zahlenwerten.
* Damit das Ergebnis korrekt ist müssen **ALLE Werte** der Testvektoren als **korrekt** bewertet werden.

#### obere Schranke für die Korrektur mit Testvektoren
* Damit die Korrektur mit Testvektoren bei sehr großen Zahlenwerten nicht zu Problemen führt werden Testwerte welche mit der Lehrerlösung 
  betragsmäßig größer als eine definierte obere Schranke sind nicht verwendet.
* Die obere Schranke ist standardmäßig 1e50 und kann mit den Testvektoren test_SQ und test_Q0,test_Q1,... definiert werden.

