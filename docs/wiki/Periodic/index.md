# Periodic
Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion 
##  periodic(Variable,Periodendauer,Funktion) 
####  Parameter 
* Variable (v): Die Funktion muss in dieser Variable veränderlich sein. 
* Periodendauer(p): die Variable wird von 0 bis Periodendauer durchlaufen. Die Einheit der Periodendauer wird auch als Einheit der Variable verwendet und muss in der Funktion ein korrektes Ergebnis liefern da es sonst zu einem Einheitenfehler führt. Die Funktion von 0 bis Periodendauer wird dann zyklisch fortgesetzt.  
* Die Funktion g(v) welche zyklisch wiederholt werden soll
* periodischer Teil der Funktion: f(v)=g(v) für v=0..p 
* perioisches Fortsetzen f(v+n*p)=g(v) für ganzzahlige n
####  Beispiel 
* Beispiel ch1(t):periodic(t,5ms,2'Vms-2'*t^2) <br> <br>![600px-ClipCapIt-190318-113524.PNG](600px-ClipCapIt-190318-113524.PNG)

##  periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion) 
Bei dieser Variante wird ein Bereich von 0 bis Funktionsperiodendauer der Ausgangsfunktion abgebildet auf einen Bereich von 0 bis Periodendauer der Zielfunktion.
####  Parameter 
* Variable (v): Die Funktion muss in dieser Variable veränderlich sein. 
* Periodendauer(p): die Variable der fertigen Funktion hat diese Periodendauer mit der angegebenen Einheit  
* Funktionsperiodendauer(fp): in der angegebenen Funktion wird der Bereich mit der Funktionsperiodendauer(fp) abgebildet auf die Periodendauer (p)
* Die Funktion g(v) welche zyklisch wiederholt werden soll
* periodischer Teil der Funktion: f(v)=g(v/p*fp) für v=0..p . Natürlich müssen die Einheiten von p und fp in die Funktion korrekt eingepasst sein, am Einfachsten ist fp einheitenlos.
* perioisches Fortsetzen f(v+n*p)=f(v) für ganzzahlige n
####  Beispiel 
* Beispiel 1: ch1(t):periodic(t,5ms,1,2V*t^2) <br> <br>![600px-ClipCapIt-190318-113644.PNG](600px-ClipCapIt-190318-113644.PNG)
* Beispiel 2: u(t) := periodic(t,10ms,pi,8V * sin(t)*sigma(t-%pi/4)) <br><br>![600px-Periodic-sin-phase.png](600px-Periodic-sin-phase.png)


##  siehe auch 
[Berechnungen](../Berechnungen/index.md)

