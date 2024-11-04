# Eingabe von Resultaten in LeTTo
###  Allgemeine Hinweise 

* Das Dezimaltrennzeichen ist der Punkt (<code>.</code>), nicht der Beistrich 
* Zwischen Zahlenwert und Einheit kann ein Leerzeichen eingefügt werden (muss aber nicht)
* Nach einem Minuszeichen <code>-</code> bei der Eingabe einer negativen Größe darf nie ein Leerzeichen auftreten
* Nach einem <code>e</code> oder <code>E</code> bei der Eingabe einer Gleitkommazahl darf ebenfalls nie ein Leerzeichen auftreten

###  Reelle physikalische Größen 

Reelle Einheiten bestehen immer aus einem Zahlenwert und einer [Einheit](../Einheit/index.md). Nachfolgend werden exemplarisch die wichtigsten physikalischen Größen zusammengefasst. LeTTo-Eingaben sind in <code>Schreibmaschinenschrift</code> angegeben. Die Groß- und Kleinschreibung von Einheiten muss genau eingehalten werden. 

Als <b>einfache Regel</b> gilt, dass alle Einheiten unter einfache Hochkomma gesetzt werden. Das funktioniert immer. Das einfache Hochkomma ' findet man mit <code>SHIFT + #</code>. Für einfache Einheiten, die ohne die Operatoren <code>*</code>, <code>/</code> und <code>^</code> auskommen, dürfen die beiden Hochkomma auch weggelassen werden.


* <code>250V</code> für eine Spannung von 250 V
* <code>220kOhm</code> oder <code>220E3Ohm</code> oder <code>220e3Ohm</code> für einen Widerstand von 220&amp;nbsp;k&amp;Omega; = 220&amp;middot;10<sup>3</sup>&amp;nbsp;&amp;Omega;
* <code>4.7MOhm</code> oder <code>4.7E6Ohm</code> für einen Widerstand von 4,7&amp;nbsp;M&amp;Omega; = 4,7&amp;middot;10<sup>6</sup>&amp;nbsp;&amp;Omega;
* <code>2.5mA</code> oder <code>2.5E-3A</code> für einen Strom von 2,5&amp;nbsp;mA = 2,5&amp;middot;10<sup>-3</sup>&amp;nbsp;A
* <code>2.2uF</code> oder <code>2.2E-6F</code> für eine Kapazität von 2,2&amp;nbsp;&amp;mu;F = 2,2&amp;middot;10<sup>-6</sup>&amp;nbsp;F
* <code>4.7nF</code> oder <code>4.7E-9F</code> für eine Kapazität von 4,7&amp;nbsp;nF = 4,7&amp;middot;10<sup>-9</sup>&amp;nbsp;F
* <code>6.8pF</code> oder <code>6.8E-12F</code> für eine Kapazität von 6,8&amp;nbsp;pF = 6,8&amp;middot;10<sup>-12</sup>&amp;nbsp;F
* <code>50mH</code> oder <code>50E-3H</code> für eine Induktivität von 50&amp;nbsp;mH = 50&amp;middot;10<sup>-3</sup>&amp;nbsp;H
* <code>45Ah</code> für eine Ladung von 45&amp;nbsp;Ah
* <code>500var</code> für eine Blindleistung von 500&amp;nbsp;var
* <code>250MVA</code> für eine Scheinleistung von 250&amp;nbsp;MVA
* <code>4.8kW</code> für eine Leistung bzw. Wirkleistung von 4,8&amp;nbsp;kW
* <code>1kWh</code> eine Einergie von 1&amp;nbsp;kWh = 3,6&amp;middot;10<sup>6</sup>&amp;nbsp;J
* <code>8.1mm2</code> oder <code>8.1mm^2</code> für eine Fläche von 8.1&amp;nbsp;mm<sup>2</sup>
* <code>27cm3</code> oder <code>27cm^3</code> für ein Volumen von 27&amp;nbsp;cm<sup>3</sup>
* <code>3.9A/mm2</code> oder <code>3.9A/mm^2</code> für eine Stromdichte von 3,9&amp;nbsp;A/mm<sup>2</sup>
* <code>290kA/m</code> oder <code>290A/mm</code> für eine magnetische Feldstärke von 290&amp;nbsp;kA/m
* <code>0.97T</code> oder <code>0.97Vs/m2</code> oder <code>0.97Vs/m^2</code> für eine magnetische Flussdichte von 0,97&amp;nbsp;T = 0,97&amp;nbsp;Vs/m<sup>2</sup>
* <code>628.32uVs/Am</code> oder <code>628.32E-6H/m</code> für eine Permeabilität von 628,32&amp;nbsp;&amp;mu;Vs/Am = 628,32&amp;middot;10<sup>-6</sup>&amp;nbsp;H/m
* <code>80km/h</code> für eine Geschwindigkeit von 80&amp;nbsp;km/h
* <code>12.2°</code> für einen Winkel von 12,2<sup>&amp;omicron;</sup> (Grad)
* <code>3.14159</code> für eine Winkel von 3,14159 rad (Radiant). **Wichtig:** die Einheit rad ist keine gültige Einheit in LeTTo und darf daher nicht angegeben werden; Winkel in Radiant werden ohne Einheit eingegeben
* <code>3000Upm</code> oder <code>3000min-1</code> oder <code>3000'1/min'</code> für eine Drehzahl von 3000&amp;nbsp;Upm = 50&amp;nbsp;s<sup>-1</sup> 
* <code>190.2s-1 oder 190.2'1/s'</code> für eine Winkelgeschwindigkeit von 190,2&amp;nbsp;rad/s
* <code>-2.82Nm</code> für ein Drehmoment von -2,82&amp;nbsp;Nm
* <code>0.12kgm2</code> oder <code>0.12kg1m2</code> oder <code>0.12kg*m^2</code>für ein Massenträgheitsmoment von 0,12&amp;nbsp;kg&amp;middot;m<sup>2</sup>
* <code>2h-1</code> oder <code>2'1/h'</code> für den Kehrwert in Stunden von 2&amp;nbsp;h<sup>-1</sup>

###  Komplexe physikalische Größen 

* <code>20.2V arg-12.2°</code> oder <code>20.2 arg-12.2°V</code> für die komplexe Spannung von 20,2&amp;nbsp;V&amp;ang;-12.2<sup>&amp;omicron;</sup>
* <code>1.1Ohm arg-30.2°</code> oder <code>1.1 arg-30.2°Ohm</code> für die komplexe Impedanz von 1,1&amp;nbsp;Ohm&amp;ang;-30.2<sup>&amp;omicron;</sup>
* <code>12.2A-j*8.6A</code> oder <code>12.2A-8.6A*j</code> oder <code>12.2-j*8.6A</code> für den komplexen Strom von 12,2&amp;nbsp;A-j&amp;middot;8,6&amp;nbsp;A

###  Vektoren 

* <code>[2, -3, 0](2, -3, 0)N</code> oder <code>[2N, -3N, 0N](2N, -3N, 0N)</code> für den dreidimensionalen Vektor ![Kraftvektor.png](Kraftvektor.png)
* <code>[0, 0, 12](0, 0, 12)Nm</code> oder <code>[0Nm, 0Nm, 12Nm](0Nm, 0Nm, 12Nm)</code> für den dreidimensionalen Vektor ![Drehmomentvektor.png](Drehmomentvektor.png)
* <code>[2, 0, 0](2, 0, 0)mm/s2</code> oder <code>[2mm/s2, 0mm/s2, 0m/s^2](2mm/s2, 0mm/s2, 0m/s^2)</code> oder <code>[2E-3, 0, 0](2E-3, 0, 0)m/s-2</code> für den dreidimensionalen Vektor ![Beschleunigungsvektor.png](Beschleunigungsvektor.png)

###  Symbolische Resultate 

* Bei symbolischen Resultaten müssen die Einheiten – falls erforderlich – in einfache Hochkomma gesetzt werden, z. B. <code>s=x*2.5'm/s'+22'm'</code>
* <code>x^y</code> für ![xpowery.png](xpowery.png)
* <code>sqrt(2)</code> für ![sqrt2.png](sqrt2.png)
* <code>root(x^2,3)</code> oder <code>x^(2/3)</code> für ![root3x2.png](root3x2.png)
* <code>exp(-x)</code> für ![exp-x.png](exp-x.png)
* <code>cos(x)</code> für ![cosx.png](cosx.png)
* <code>atan(1)</code> für den Arkustangens von 1
* <code>%pi</code> für die Kreiszahl &amp;pi; = 3,14159...

###  Siehe auch 

* [Einheit](../Einheit/index.md)

