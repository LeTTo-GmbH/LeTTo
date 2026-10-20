# Plot-Plugin Auflösung
Die Auflösung des [Plot](../Plot/index.md)-Plugins kann über den w-Parameter und size gesetzt werden.

* Entweder im PIG-Tag in der Angabe:
<pre>
[PIG plugin1 "w30h"/](PIG plugin1 "w30h"/)
</pre>

* oder in der Plugin-Definition:
<pre>
f(x):=x^2-3;w30h
</pre>

###  mögliche w-Parameter 


| Parameter                 | Beschreibung                                                | Beispiel    |
|---------------------------|-------------------------------------------------------------|-------------|
| w{zahl}                   | Bildbreite in Prozent                                       | w30         |
| w{zahl}h                  | Hohe Auflösung mit Bildbreite in Prozent                    | w30h        |
| w{zahl}l                  | kleinere Auflösung mit Bildbreite in Prozent                | w50l        |
| w{zahl}s                  | geringe Auflösung mit Bildbreite in Prozent                 | w40s        |
| w{zahl}H                  | Auflösung 1000x1000 mit Bildbreite in Prozent               | w70H        |
| w{zahl}L                  | Auflösung 500x500 mit Bildbreite in Prozent                 | w30L        |
| w{zahl}S                  | Auflösung 300x300 mit Bildbreite in Prozent                 | w40S        |
| w{zahl}-{pixel}           | Auflösung pixel mal pixel mit einer Bildbreite in Prozent   | w30-500     |
| w{zahl}-{pixelx}x{pixely} | Auflösung pixelx mal pixely mit einer Bildbreite in Prozent | w30-800x500 |


###  mögliche size-Parameter 

Wenn der size-Parameter gesetzt ist kann der **w-Parameter nur für die Bildbreite in Prozent** verwendet werden, die Auflösung kann aber damit nicht verändert werden.

