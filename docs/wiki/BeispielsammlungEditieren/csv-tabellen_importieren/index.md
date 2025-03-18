# CSV-Tabellen importieren (Kennlinien importieren)

Kurzanleitung zum Importieren von Kennlinien siehe [Video](https://www.youtube.com/watch?v=ngNw3Uu8Zyk): https://www.youtube.com/watch?v=ngNw3Uu8Zyk

## Maxima-Feld
Im Maxima-Feld des Frageeditors können externe CSV-Dateien (wie bspw. Kennlinien) als Tabellen in LeTTo importiert werden. 
<br>![Maxima-Feld des Frageeditors](../img_9.png "Maximafeld")

## Importvorgang
* Nach dem Klick auf den (CSV-Importieren)-Button  ![img_2.png](img_2.png)  - siehe oben, rechter Bildschirmrand im Maximafenster-  erscheint der Dialog für den Kennlinienimport:
  <br>![img.png](img.png)

### Aufbau einer importierbaren CSV-Datei **mit** Einheitenzeile
<pre>
Spalte1;U;I;B
°C;mV;kA;T
-2;13;-0.2;0.4
0;24;0,4;0.9
</pre>
### Aufbau einer importierbaren CSV-Datei **ohne** Einheitenzeile
<pre>
Zeit;Spannung;Strom
0ms;1V;2.4A
1ms;1.3V;2.6A
</pre>
### Beispiel CSV-Datei einer Magnetisierungskennlinie
[Magnetisierungslinie](/assets/download/Magnetisierungslinie.csv)

### Import einer neuen Kennlinie aus einer CSV-Datei nur in eine Frage
Die importierte Kennlinie steht nach dem erfolgreichem Import in LeTTo bei dieser Importmethode nur innerhalb einer Frage zur Verfügung.
* Button "Kennlinie hochladen"
* hochzuladende CSV-Datei auswählen
* Nun erscheint eine Vorschau des Imports in der die Importparameter verändert werden. Nach erfolgreichem Import werden die Daten auch als Grafik-Plot dargestellt.
  <br><img alt="img_3.png" src="img_3.png" width="600px"/>
  <br><img alt="img_4.png" src="img_4.png" width="250px"/>
* Button **"Kennlinie NUR in Frage übernehmen"** drücken
* Es muss nun eine Variable definiert werden über die die Kennlinie im Maxima-Feld ansprechbar sein soll:
  <br><img alt="img_5.png" src="img_5.png" width="300px"/>
* Nun erscheint die importierte Tabelle im Tabellen-Dialog: 
  <br><img alt="img_6.png" src="img_6.png" width="600px"/>
* Ab sofort kann die Kennlinie im Maxima-Feld verwendet werden
  <br><img alt="img_7.png" src="img_7.png" width="600px"/>
* Berechnungsfunktionen siehe [Berechnungen](../../Berechnungen/index.md#funktionen-für-importierte-tabellen)

### Import einer neuen Kennlinie und speichern als globale Tabelle
* Wie zuvor die Kennlinie hochladen
* Im Vorschaudialog **"Kennlinie GLOBAL speichern"** auswählen
* Nun muss eine globale Kategorie gewählt werden der die importierte Kennlinie themenmäßig zugeordnet werden kann
  <br><img alt="img_8.png" src="img_8.png" width="300px"/>
* Nun erscheint die Frage in der Liste der gewählten Kategorie
  <br><img alt="img_9.png" src="img_9.png" width="600px"/>
* Soll die Tabelle auch in der Frage verfügbar sein - siehe nächster Punkt (Import einer bestehenden globalen Tabelle in eine Frage)

### Import einer bestehenden globalen Tabelle in eine Frage
* Auswahl der Kategorie in der die globale Tabelle zu finden ist
* Auswahl der korrekten Tabelle (Kennlinie)
  <br><img alt="img_10.png" src="img_10.png" width="600px"/>
* Kennlinie **"Zur Frage"** hinzufügen
* Es muss nun die **Variable** definiert werden über die die Kennlinie im Maxima-Feld ansprechbar ist:
  <br><img alt="img_5.png" src="img_5.png" width="300px"/>
* Nun erscheint die importierte Tabelle im Tabellen-Dialog:
  <br><img alt="img_6.png" src="img_6.png" width="600px"/>
* Ab sofort kann die Kennlinie im Maxima-Feld verwendet werden
  <br><img alt="img_7.png" src="img_7.png" width="600px"/>
* Berechnungsfunktionen siehe [Berechnungen](../../Berechnungen/index.md#funktionen-für-importierte-tabellen)

