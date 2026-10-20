# Linienart
Die Linienart im [Plot](../Plot/index.md)-Plogin wird über den **style** Wert der als String definiert ist angegeben. 

##  Zeichen für die Definition der Linienart 


| Zeichen         | Beschreibung                                                                                                                | Beispiel                                                                                                       | Graph                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| . (Punkt)       | kurzer Strich bzw. Punkt                                                                                                    | line(-6,-3,6,9,style=".",size=8);line(-6,-6,6,6,style="2.",size=8);line(-6,-9,6,3,style="6.",size=8)           | <br>![100px-ClipCapIt-200520-085034.PNG](100px-ClipCapIt-200520-085034.PNG) |
| - (Minus)       | mittlerer Strich                                                                                                            | line(-6,-3,6,9,style="-",size=8);line(-6,-6,6,6,style="-",size=3);line(-6,-9,6,3,style="9-",size=3)            | <br>![100px-ClipCapIt-200520-085211.PNG](100px-ClipCapIt-200520-085211.PNG) |
| - (Unterstrich) | langer Strich                                                                                                               | line(-6,-3,6,9,style="_",size=8);line(-6,-6,6,6,style="_",size=3);line(-6,-9,6,3,style="9_",size=3)            | <br>![100px-ClipCapIt-200520-085402.PNG](100px-ClipCapIt-200520-085402.PNG) |
| (Leerzeichen)   | Zwischenraum                                                                                                                | line(-6,-3,6,9,style=". .",size=8);line(-6,-6,6,6,style=". ",size=8);line(-6,-9,6,3,style="- ",size=3)         | <br>![100px-ClipCapIt-200520-085610.PNG](100px-ClipCapIt-200520-085610.PNG) |
| r               | abgerundete Enden                                                                                                           | line(-6,-3,6,9,style=".r",size=8);line(-6,-6,6,6,style="-r",size=8);line(-6,-9,6,3,style="-r",size=3)          | <br>![100px-ClipCapIt-200520-085759.PNG](100px-ClipCapIt-200520-085759.PNG) |
| s               | rechteckige Enden                                                                                                           | line(-6,-3,6,9,style=".s",size=8);line(-6,-6,6,6,style="-s",size=8);line(-6,-9,6,3,style="-s",size=3)          | <br>![100px-ClipCapIt-200520-090048.PNG](100px-ClipCapIt-200520-090048.PNG) |
| R               | abgerundete äußere Ecken                                                                                                    | rect(-8,-8,8,8,style="R",size=18);rect(-6,-6,6,6,style="R",size=8)                                             | <br>![100px-ClipCapIt-200520-182106.PNG](100px-ClipCapIt-200520-182106.PNG) |
| B               | angefaste äußere Ecken                                                                                                      | rect(-8,-8,8,8,style="B",size=18);rect(-6,-6,6,6,style="B",size=8)                                             | <br>![100px-ClipCapIt-200520-182305.PNG](100px-ClipCapIt-200520-182305.PNG) |
| 0..9 (Ziffer)   | setzt den automatischen Leerraum zwischen zwei Linien (0:extrem kurz 9:lang). Der Wert kann auch mehrmals angegeben werden. | line(-6,-3,6,9,style="1-4-9-",size=5);line(-6,-6,6,6,style="1--9--",size=4);line(-6,-9,6,3,style="1-.",size=4) | <br>![100px-ClipCapIt-200520-183040.PNG](100px-ClipCapIt-200520-183040.PNG) |


##  Beispiele 

