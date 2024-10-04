Die Auflösung des [[Plot]]-Plugins kann über den w-Parameter und size gesetzt werden.

* Entweder im PIG-Tag in der Angabe:
&lt;pre&gt;
[PIG plugin1 "w30h"/]
&lt;/pre&gt;

* oder in der Plugin-Definition:
&lt;pre&gt;
f(x):=x^2-3;w30h
&lt;/pre&gt;

== mögliche w-Parameter ==

{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung || Beispiel
|-
| w{zahl} || Bildbreite in Prozent || w30
|-
| w{zahl}h || Hohe Auflösung mit Bildbreite in Prozent || w30h
|-
| w{zahl}l || kleinere Auflösung mit Bildbreite in Prozent || w50l
|-
| w{zahl}s || geringe Auflösung mit Bildbreite in Prozent || w40s
|-
| w{zahl}H || Auflösung 1000x1000 mit Bildbreite in Prozent || w70H
|-
| w{zahl}L || Auflösung 500x500 mit Bildbreite in Prozent || w30L
|-
| w{zahl}S || Auflösung 300x300 mit Bildbreite in Prozent || w40S
|-
| w{zahl}-{pixel} || Auflösung pixel mal pixel mit einer Bildbreite in Prozent || w30-500
|-
| w{zahl}-{pixelx}x{pixely} || Auflösung pixelx mal pixely mit einer Bildbreite in Prozent || w30-800x500
|-
|}

== mögliche size-Parameter ==

Wenn der size-Parameter gesetzt ist kann der '''w-Parameter nur für die Bildbreite in Prozent''' verwendet werden, die Auflösung kann aber damit nicht verändert werden.

{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung || Beispiel
|-
| size={pixel} || Auflösung pixel mal pixel || size=800
|-
| size={pixelx}x{pixely} || Auflösung pixelx mal pixely || size=800x600
|-
|}

