# Toleranz
Die Toleranz definiert, wie genau ein Schüler seine Antwort angeben muss:
* Die Toleranz ist im Normalfall eine **relative Angabe** und wird in **Prozent** angegeben
* Wird bei der Toleranz kein Prozent angegeben, so muss der Wert zwischen 0 und 1 liegen und entspricht dann dem Prozentwert durch 100
* Wird bei der Toleranz vor oder nach dem Wert ohne Prozentzeichen ein **a** angegeben, so wird dieser Wert als **absolute Toleranz** der Größe in SI-Einheiten interpretiert. ( z.B.: 0.1a bei einem eletrischen Strom in Ampere entspricht einer absoluten Toleranz von 0.1A ) Absolute Toleranzen sind vor allem bei Ergebnissen welche Null sind notwendig, da die Berechnung statt 0 meist eine sehr kleine Zahl berechnet, welche dann mit einer relativen Toleranz auch extrem genau eingegeben werden muss und 0 dadurch nicht im Toleranzbereich liegen kann!
* Behandlung von komplexen Zahlen bei relativer Toleranzangabe: Aus dem Betrag der komplexen Lösung wird mittels dem angegeben Prozentwert der Radius eines Toleranzkreises definiert. Der Mittelpunkt dieses Kreises wird von der korrekten Lösung bestimmt. Liegt die Schülereingabe innerhalb dieses Kreises wird diese als korrekt gewertet.
* Behandlung von komplexen Zahlen bei absoluter Toleranzangabe: Die absolute Toleranzangabe definiert den Radius eines Toleranzkreises. Der Mittelpunkt dieses Kreises wird von der korrekten Lösung bestimmt. Liegt die Schülereingabe innerhalb dieses Kreises wird diese als korrekt gewertet - siehe Bsp.: roter Zeiger wird nicht, blauer Zeiger wird als Lösung zugelassen.
  <br>![200px-ClipCapIt-200528-210911.PNG](../200px-ClipCapIt-200528-210911.PNG)
* Wird im Tolerenzfeld eine Einheit verwendet wird automatisch eine absolute Toleranz eingestellt.
* Wird im Toleranzfeld ein Einheitenvielfaches (m,u,n,p,k,M,...) verwendet so wird eine absolute Toleranz eingestellt.

## Beispiele 

| Toleranzfeld | Beschreibung                                                    | 
|--------------|-----------------------------------------------------------------|
| 3%           | relativ mit 3 Prozent                                           |
| 0.02         | relativ mit 2 Prozent                                           |
| a0.1         | absolut 0.1                                                     |
| 0.01a        | absolut 0.01                                                    |
| 1m           | absolut 0.001                                                   |
| 1mV          | absolut 0.001                                                   |
| a0           | absolut exakt - kann zu Problemen durch Rundungsfehler führen!! |

