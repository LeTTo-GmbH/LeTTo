# Dezibel
####  skalierende Einheit dB 
In LeTTo gibt es eine skalierende Dezibel-Einheit dB welche einen einheitenlosen Wert logarithmisch skaliert ausgibt. Der Rechenwert ist dabei aber immer der Ursprüngliche Wert.

Bsp:

* 40dB steht für den Zahlenwert 100
* Dargestellt wird: d=40dB
* gerechnet wird mit: r=100
* Umechnung
  * d=20dB*log(r)
  * r=10^(d/20dB)

####  dargestellte Einheit ohne Skalierung: dB10, dB20, dBW, dBm, dBu, dBV, dBmV, dBuV, dBA 
Weitere dB-Einheiten sind rein dargestellte Einheiten welche zwar bei einem einheitenlosen Zahlenwert dabei stehen können, wo aber der dargestellte Zahlenwert immer dem Zahlenwert entspricht mit dem auch gerechnet wird.

Da bei diesen Einheiten keine automatische Umrechnung der Darstellung erfolgt gibt es für diese Einheiten Umrechnungsfunktionen welche von einem Zahlenwert in dB umrechnen (dB,dB10,dBW,dBm,dBu,dBV,dBmV,dBuV) oder einen dB-Wert in den ursprünglichen Zahlenwert umrechnen (fromdB, fromdB10, fromdBW, fromdBm, fromdBu, fromdBV, fromdBmV, fromdBuV). siehe [Berechnungen#funktionen-zu-einheiten-](../Berechnungen/index.md#funktionen-zu-einheiten-)

####  Rechnen mit dB 
Da dB grundsätzlich dimensionslos ist geht beim Rechnen mit dB-Werten die Einheit verloren. Hierbei ist darauf zu achten ob eine skalierende Einheit verwendet wird die immer mit dem Originalwert rechnet oder eine dargestellte Einheit bei der mit dem dB-Zahlenwert gerechnet wird.

Beispiele:

30dB20+1 -&gt; 31

fromdB(30) -&gt; 31.623

dB(31.623) -&gt; 30dB20

removeunit(30dB) -&gt; 31.623

removeunit(30dB20) -&gt; 30

30dB+1 -&gt; 32.623

todB(30dB+1) -&gt; 30.27 dB

todB(30dB+5dB) -&gt;30.475 dB

todB(fromdB(30dB20+5dB20)) -&gt; 35dB


25dB10 + 1 -&gt; 26

fromdB10(25) -&gt; 316.23

dB10(316.23) -&gt; 25dB10

