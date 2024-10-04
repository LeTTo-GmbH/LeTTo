=Funktionsweise=
* Die Funktion csin erzeugt aus einer komplexen Zahl eine Zeitfunktion als Sinusfunktion!
* Die Funktion ist vor allem für die Verwendung im [[Graph]]-Plugin entwickelt worden

=Ein Parameter=
&lt;pre&gt;
csin(P1):cabs(P1)*sin(2*%pi*f*t+carg(P1))
&lt;/pre&gt;

=Zwei Parameter=
&lt;pre&gt;
csin(P1,P2) : cabs(P1)*sin(2*%pi*P2*t+carg(P1))
&lt;/pre&gt;

=Drei Parameter=
&lt;pre&gt;
csin(P1,P2,P3): cabs(P1)*sin(2*%pi*P2*P3+carg(P1)) 
&lt;/pre&gt;

