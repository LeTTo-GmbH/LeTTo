= Digigraph =
Mit dem Digigraph-[[Plugins|Plugin]] können Zeitverläufe von Digitalsignalen in einem, einem Oszilloskop nachgebildeten, Graphen dargestellt werden.

Folgende Signalarten sind darstellbar:
* allgemeine Signalverläufe
* UART
* RS232
* SPI
* I²C

= Signaldefinition =
== allgemeine Signalverläufe ==
Übertragung von Bits erfolgt LSB-First
=== Syntax ===
&lt;pre&gt;
bit,Name:Bitdauer:daten
&lt;/pre&gt;
* Name : Signalname
* Bitdauer : Dauer von einem Bit
* daten: Die Daten können als Zeichen, String, Ganzzahl, Hexadezimalzahl oder Binärzahl angegeben werden. Zeichen und Strings werden im 8-Bit-ASCii-Code codiert.
===Beispiele===
&lt;pre&gt;
bit,x:1us:0b1001001;bit,y:2us,8:0b0100100011
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-222145.PNG|400px]]

== UART ==
=== Syntax ===
&lt;pre&gt;
uart,Name:Baudrate,Bit,Parität,Stopbits:daten,daten,daten
&lt;/pre&gt;
* Name: Signalname
* Baudrate: Die Baudrate in baud ohne Angabe der Einheit.
* Bit: Bitanzahl für die Datenübertragung.
* Parität: Angabe der Paritätsbits (e,o,n).
* Stopbits: 1 oder 2 Stopbits.
* daten: Die Daten können als Zeichen, String, Ganzzahl, Hexadezimalzahl oder Binärzahl angegeben werden. Zeichen und Strings werden im 8-Bit-ASCii-Code codiert.
===Beispiele===
&lt;pre&gt;
uart,G:9600,8,n,1:0b1010101;uart,P:7200,8,n,1:0x7e
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-195203.PNG|400px]]
&lt;pre&gt;
uart,G:9600,8,o,1:0b1011101,0b01010001
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-195317.PNG|400px]]

== RS232 ==
=== Syntax ===
&lt;pre&gt;
rs232,Name:Baudrate,Bit,Parität,Stopbits:daten,daten,daten
&lt;/pre&gt;
* Name: Signalname
* Baudrate: Die Baudrate in baud ohne Angabe der Einheit.
* Bit: Bitanzahl für die Datenübertragung.
* Parität: Angabe der Paritätsbits (e,o,n).
* Stopbits: 1 oder 2 Stopbits.
* daten: Die Daten können als Zeichen, String, Ganzzahl, Hexadezimalzahl oder Binärzahl angegeben werden. Zeichen und Strings werden im 8-Bit-ASCii-Code codiert.
===Beispiele===
&lt;pre&gt;
rs232,G:9600,8,n,1:0b1010101;rs232,P:7200,8,n,1:0x7e
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-195813.PNG|400px]]

==SPI==
=== Syntax ===
&lt;pre&gt;
spi,Name:Clockfrequenz,Mode:daten,daten,daten
&lt;/pre&gt;
* Name: Signalname, kann auch weggelassen werden
* Mode: Definition wie in [https://de.wikipedia.org/wiki/Serial_Peripheral_Interface Wikipedia] beschrieben zusammen gesetzt aus CPHA (Clock-Phase) und CPOL (Clock-Polarity)
* Clockfrequenz: Die Grundfrequenz der SCL-Leitung
* daten: Die Daten können als Zeichen, String, Ganzzahl, Hexadezimalzahl oder Binärzahl angegeben werden. Zeichen und Strings werden im 8-Bit-ASCii-Code codiert.
===Beispiele===
&lt;pre&gt;
spi:40000Hz,1:'Ac':0xf0,0x81
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-213219.PNG|400px]]
&lt;pre&gt;
spi:40000Hz,mode:0x81:0x42
&lt;/pre&gt;
{| class="wikitable" style="text-align: left; width: 100%;" 
| Mode || 0 || 1 || 2 || 3
|-
| CPOL || 0 || 0 || 1 || 1
|-
| CPHA || 0 || 1 || 0 || 1
|-
| Graph || :[[Datei:ClipCapIt-190218-213357.PNG|200px]] || :[[Datei:ClipCapIt-190218-213422.PNG|200px]] || :[[Datei:ClipCapIt-190218-213434.PNG|200px]] || :[[Datei:ClipCapIt-190218-213503.PNG|200px]]
|-
|}

==I²C-Bus==
=== Syntax ===
&lt;pre&gt;
i2c,Name:Clockfrequenz:daten,daten,daten
&lt;/pre&gt;
* Name: Signalname, kann auch weggelassen werden
* Clockfrequenz: Die Grundfrequenz der SCL-Leitung
* daten: Die Daten können als Zeichen, String, Ganzzahl, Hexadezimalzahl oder Binärzahl angegeben werden. Zeichen und Strings werden im 8-Bit-ASCii-Code codiert.
===Beispiele===
&lt;pre&gt;
i2c:10000Hz:0x101,0x080,0x100,0x200
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-194357.PNG|400px]]
&lt;pre&gt;
i2c,x:40000Hz:0x181
&lt;/pre&gt;
:[[Datei:ClipCapIt-190218-194606.PNG|400px]]

= PIG Parameter = 
Beim PIG-Tag können Parameter zur [[Konfiguration des Oszilloskopes]] angegeben werden.

Beispiele:
&lt;pre&gt;
ch1:div=5V,null=3,color=#008800 ; time:div=3us,trigger=0
&lt;/pre&gt;


===Zeichenelemente des Plot-Plugins===
Durch Strichpunkt getrennt können auch die [[Plot#vordefinierte_graphische_Funktionen|Zeichenelemente]] des Plot-Plugins eingefügt werden.

Das Koordinatensystem des Bildschirmfensters hat den Nullpunkt links unten.

Die positive horizontale Achse reicht von 0 bis 100 von links nach rechtes.

Die postitive vertikale Achse reicht unten nach oben und beginnt unten bei 0. Der maximale Wert ist abhängig vom Seitenverhältnis des Fensters.


[[Category:Plugins]]

