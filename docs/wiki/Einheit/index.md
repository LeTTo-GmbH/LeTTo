# Einheit
####  Allgemeines zu Einheiten 
*Als Einheit kann jede SI-Grundeinheit und alle davon abgeleiteten Einheiten verwendet werden. 

*Eine Einheit kann bei einem [Datensatz](../Datensätze/index.md), im [Maxima-Feld#maxima-feld-](../BeispielsammlungEditieren#maxima-feld-/index.md#maxima-feld-), bei der [Zieleinheit](../ZielEinheit/index.md) einer Frage, bei der Lösung, bei der Schülerantwort etc. verwendet werden.

*Fast jede Einheit kann mit einem Einheitenvielfachen versehen werden zB: mA uV kW

*Eine Einheit, welche kein Rechenzeichen beinhaltet kann immer direkt an den Zahlenwert angehängt werden  zB: 5A, 30mAs, 4m3

*Eine **Einheit**, welche ein **Rechenzeichen beinhaltet** sollte immer in **einfache Hochkommata** gesetzt werden (Ausnahme ist hier die Schülereingabe von genau einem Zahlenwert, hier können die Hochkommata weggelassen werden) zB: 5'V/m' 29'km/h'

####  siehe auch 
* [Berechnungen](../Berechnungen/index.md)
* [Maxima#maxima-feld-](../BeispielsammlungEditieren#maxima-feld-/index.md#maxima-feld-)
* [Datensätze](../Datensätze/index.md)
* [ZielEinheit](../ZielEinheit/index.md)
* [Editor für den Angabetext#datensätze-und-variable-](../EditorfürdenAngabetext/index.md#datensätze-und-variable-)
* [Eingabe von Resultaten](../EingabevonResultateninLeTTo/index.md)

####  Basiseinheiten 

| Einheit | Name    | Dimension                                                          | Dimensionssymbol |
|---------|---------|--------------------------------------------------------------------|------------------|
| m       | Meter   | Länge                                                              | l                |
| g       | Gramm   | Masse                                                              | m                |
| s       | Sekunde | Zeit                                                               | t                |
| A       | Ampere  | Stromstärke                                                        | I                |
| K       | Kelvin  | Temperatur                                                         | T                |
| mol     | Mol     | Stoffmenge                                                         | N                |
| cd      | Candela | Lichtstärke                                                        | J                |
| Euro    | Euro    | Währung (keine richtige Einheit aber als Basiseinheit realisiert)  | W                |
| Dollar  | Dollar  | Währung2 (keine richtige Einheit aber als Basiseinheit realisiert) | X                |


####  Einheiten 

#####  Grundeinheiten: 

| Einheit | Name                | Basiseinheit | Größe                         | Dimensionssymbol |
|---------|---------------------|--------------|-------------------------------|------------------|
| N       | Newton              | kgm/s2       | Kraft                         | F                |
| W       | Watt                | kgm2/s3      | Leistung                      | Q                |
| V       | Volt                | kgm2/As3     | elektrische Spannung          | U                |
| VAr     | Volt-Ampere-Reaktiv | kgm2/s3      | Bildleistung                  | Q                |
| var     | Volt-Ampere-Reaktiv | kgm2/s3      | Bildleistung                  | Q                |
| VA      | Volt-Ampere         | kgm2/s3      | Scheinleistung                | S                |
| Ohm     | Ohm                 | kgm2/A2s3    | elektrischer Widerstand       | R                |
| C       | Coulomb             | As           | elektrische Ladung            | Q                |
| S       | Siemens             | A2s2/kgm2    | elektrischer Leitwert         | G                |
| Pa      | Pascal              | kg/ms2       | Druck                         | p                |
| H       | Henry               | kgm2/A2s2    | Induktivität                  | L                |
| F       | Farad               | A2s4/kgm2    | Kapazität                     | C                |
| T       | Tesla               | kg/As2       | magnetische Induktion         | B                |
| Hz      | Herz                | 1/s          | Frequenz                      | f                |
| Bd      | Baud                | 1/s          | Baudrate bei Datenübertragung | BR               |
| J       | Joule               | kgm2/s2      | Arbeit                        | W                |
| Wb      | Weber               | kgm2/As2     | magnetischer Fluss            | Phi              |
| lm      | Lumen               | cd           | Lichtstrom cd/sr              | I                |
| lx      | lux                 | lm/m2        | Beleuchtungsstärke            | L                |
| Bq      | Becquerel           | 1/s          | Radioaktivität                | Ra               |
| Gy      | Gray                | J/kg         | Energiedosis                  | Ed               |
| Sv      | Sievert             | J/kg         | Äquivalenzdosis               | Da               |
| kat     | Katal               | mol/s        | Katalystische Aktivität       | Kat              |


#####  nicht SI-Einheiten: 

| Einheit  | Name                   | Basiseinheit | Größe(Symbol)     | Faktor      |
|----------|------------------------|--------------|-------------------|-------------|
| min      | Minute                 | s            | Zeit              | 60          |
| h        | Stunde                 | s            | Zeit              | 3600        |
| day      | Tag                    | s            | Zeit              | 3600*24     |
| month    | Monat                  | s            | Zeit              | 3600*24*30  |
| year     | Jahr                   | s            | Zeit              | 3600*24*365 |
| Upm      | Umdrehungen pro Minute | 1/s          | Drehzahl(n)       | 1/60        |
| inch     | Zoll                   | m            | Länge             | 0.0254      |
| th       | tausendstel Zoll       | m            | Länge             | 0.0000254   |
| mil      | tausendstel Zoll       | m            | Länge             | 0.0000254   |
| Mx       | Maxwell                | kgm2/As2     | magnetischer Fluß | 1e-8        |
| °C       | Grad Celsius           | K            | Temperatur        | *1+273.15   |
| t        | Tonne                  | kg           | Masse             | 1000        |
| bar      | Bar                    | kg/ms2       | Druck             | 1e5         |
| l        | Liter                  | m3           | Volumen           | 1e-3        |
| €        | Euro                   | Euro         | Währung           | 1           |
| $        | Dollar                 | Dollar       | Währung2          | 1           |
| Eurocent | Eurocent               | Euro         | Währung           | 0.01        |


#####  Winkel: Hier sind keine Einheitenvielfachen erlaubt! 

| Einheit | Name         | Basiseinheit | Faktor zu Basiseinheit |
|---------|--------------|--------------|------------------------|
|         | Radiant      | 1            | 1                      |
| °       | Grad         | 1            | %pi/180                |
| ´       | Bogenminute  | 1            | %pi/180/60             |
| ´´      | Bogensekunde | 1            | %pi/180/3600           |
| pi      | Radiant      | 1            | %pi                    |
| sr      | Steradiant   | 1            | 1                      |


#####  Sondereinheiten für Einheitenlose Größen: Hier sind keine Einheitenvielfachen erlaubt! 

| Einheit  | Name              | Beschreibung/Faktor zu 1                        |
|----------|-------------------|-------------------------------------------------|
| dB       | Dezibel           | Einheit für Einheitenlose logarithmische Größen |
| %        | Prozent           | 0.01                                            |
| promille | Promille          | 0.001                                           |
| ppm      | parts per million | 1e-6                                            |
| °        | Grad              | pi/180                                          |


#####  Sondereinheiten Digitaltechnik: 

| Einheit | Beschreibung                                                                                       | Zahlenwert                 |
|---------|----------------------------------------------------------------------------------------------------|----------------------------|
| Bit     | Bit der Digitaltechnik als 0/1-Information - wird intern als Zahlenwert 1 einheitenlos gespeichert | 1                          |
| Byte    | 8 Bit als 1 Byte - wird intern als Zahlenwert 8 einheitenlos gespeichert                           | 8                          |       
| kBit    | 1024 Bit                                                                                           | 1024                       |
| kByte   | 1024 Byte                                                                                          | 1024*8                     |
| MBit    | 1024 kBit                                                                                          | 1024*1024                  |
| MByte   | 1024 kByte                                                                                         | 1024*1024*8                |
| GBit    | 1024 MBit                                                                                          | 1024*1024*1024             |
| GByte   | 1024 MByte                                                                                         | 1024*1024*1024*8           | 
| TBit    | 1024 GBit                                                                                          | 1024*1024*1024*1024        |
| TByte   | 1024 GByte                                                                                         | 1024*1024*1024*1024*8      |
| PBit    | 1024 TBit                                                                                          | 1024*1024*1024*1024*1024   |
| PByte   | 1024 TByte                                                                                         | 1024*1024*1024*1024*1024*8 |

####  Dimensionen, die kein eigenes Einheitenzeichen haben, aber trotzdem definiert sind 

| Größe                      | Dimensionssymbol | Einheit   |
|----------------------------|------------------|-----------|
| magnetische Feldstärke     | H                | A/m       |
| elektrische Feldstärke     | E                | V/m       |
| elektrische Flußdichte     | D                | As/m2     |
| spezifischer Widerstand    | rho              | Ohm*mm2/m |
| spezifischer Leitwert      | gamma            | Sm/mm2    |
| magnetische Permeabilität  | mu               | Vs/Am     |
| elektrische Permittivität  | epsilon          | As/Vm     |
| Widerstandsbelag           | Rs               | Ohm/m     |
| Induktivitätsbelag         | Ls               | H/m       |
| Kapazitätsbelag            | Cs               | F/m       |
| Leitwertsbelag             | Gs               | S/m       |
| Fläche                     | A                | m2        |
| Volumen                    | V                | m3        |
| Drehmoment                 | M                | Nm        |
| Geschwindigkeit            | v                | m/s       |
| Beschleunigung             | a                | m/s2      |
| Winkelgeschwindigkeit      | omega            | rad/s     |
| Winkelbeschleunigung       | alpha            | rad/s2    |
| Impuls                     | p                | Ns        |
| Dichte                     | rho              | kg/m3     |
| Wichte                     | Y                | N/m3      |
| Elastizitätsmodul          | E                | N/m2      |
| dynamische Viskosität      | rho              | Ns/m2     |
| kinematische Viskosität    | v                | m2/s      |
| Trägheitsmoment            | J                | kgm2      |
| Widerstandsmoment          | W                | m3        |
| mechanische Spannung       | sigma            | N/m2      |
| spezifische Wärmekapazität | c                | kJ/kgK    |
| Wärmekapazität             | C                | J/K       |
| thermischer Widerstand     | Rth              | K/W       |


####  Einheitenvielfache 

| Zeichen | Name  | Faktor |
|---------|-------|--------|
| y       | Yocto | 1e-24  |
| z       | Zepto | 1e-21  |
| a       | Atto  | 1e-18  |
| f       | Femto | 1e-15  |
| p       | Piko  | 1e-12  |
| n       | Nano  | 1e-9   |
| u       | Mikro | 1e-6   |
| m       | Milli | 1-3    |
| c       | Zenti | 0.01   |
| d       | Dezi  | 0.1    |
| da      | Deka  | 10     |
| h       | Hekto | 100    |
| k       | Kilo  | 1e3    |
| M       | Mega  | 1e6    |
| G       | Giga  | 1e9    |
| T       | Tera  | 1e12   |
| P       | Peta  | 1e15   |
| E       | Exa   | 1e18   |
| Z       | Zetta | 1e21   |
| Y       | Yotta | 1e24   |


Kategorie:Berechnung

