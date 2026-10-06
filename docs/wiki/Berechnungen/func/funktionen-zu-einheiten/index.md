# Funktionen zu Einheiten

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [dB](db-gross-1/index.md) | Wandelt einen Zahlenwert in eine nicht skalierende Dezibel-Einheit um. Einheitenlos wird in dB20 gewandelt, mit den Einheiten V,mV,uV,W,mW,uW wird in die zugehörige dB-Einheit gewandelt. DEMO-Beispiel |
| [dB10](db10-gross-1/index.md) | wandelt eine Zahl in einen Dezibel Wert dB10 mit 10dB pro Dekade DEMO-Beispiel |
| [dBm](dbm-gross-1/index.md) | Wandelt eine Leistung in dBm um. Bezugsleistung ist 1 mW: `10*log10(P/1mW)`. Bei komplexen Leistungen wird der Betrag verwendet; vorhandene dBW/dBm/dBu-Werte werden entsprechend umgerechnet. |
| [dBmV](dbmv-gross-1-3/index.md) | Wandelt eine Spannung in dBmV um. Bezugsspannung ist 1 mV: `20*log10(U/1mV)`. Bei komplexen Spannungen wird der Betrag verwendet. |
| [dBu](dbu-gross-1/index.md) | Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. **Hinweis:** Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V. |
| [dBuV](dbuv-gross-1-3/index.md) | Wandelt eine Spannung in dBuV um. Bezugsspannung ist 1 µV: `20*log10(U/1uV)`. Bei komplexen Spannungen wird der Betrag verwendet. |
| [dBV](dbv-gross-1-2/index.md) | Wandelt eine Spannung in dBV um. Bezugsspannung ist 1 V: `20*log10(U/1V)`. Bei komplexen Spannungen wird der Betrag verwendet; vorhandene dBV/dBmV/dBuV-Werte werden entsprechend umgerechnet. |
| [dBW](dbw-gross-1-2/index.md) | wandelt eine Leistung in einen Dezibel Wert dBW mit 10dB pro Dekade DEMO-Beispiel |
| [double](double/index.md) | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren DEMO-Beispiel |
| [eh](eh/index.md) | Liefert zu einem numerischen Wert die zugehörige Einheit als Wert 1 zurück; bei einem einheitenlosen Wert wird `1` geliefert. |
| [float](float/index.md) | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren (wie double) |
| [fromdB](fromdb-gross-5/index.md) | Wandelt eine nicht skalierende Dezibel-Einheit in einen normalen Zahlenwert um DEMO-Beispiel |
| [fromdB10](fromdb10-gross-5/index.md) | wandelt einen Dezibel Wert mit 10dB pro Dekade in den Ausgangswert DEMO-Beispiel |
| [fromdBm](fromdbm-gross-5/index.md) | Wandelt einen dBm-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBm interpretiert und als Leistung in mW zurückgegeben. |
| [fromdBmV](fromdbmv-gross-5-7/index.md) | Wandelt einen dBmV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBmV interpretiert und als Spannung in mV zurückgegeben. |
| [fromdBu](fromdbu-gross-5/index.md) | Wandelt einen LeTTo-dBu-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBu interpretiert und als Leistung in µW zurückgegeben. |
| [fromdBuV](fromdbuv-gross-5-7/index.md) | Wandelt einen dBuV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBuV interpretiert und als Spannung in µV zurückgegeben. |
| [fromdBV](fromdbv-gross-5-6/index.md) | Wandelt einen dBV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBV interpretiert und als Spannung in V zurückgegeben. |
| [fromdBW](fromdbw-gross-5-6/index.md) | wandelt einen Dezibel Wert mit 10dB pro Dekade in eine Leistung DEMO-Beispiel |
| [numeric](numeric/index.md) | verwirft die Einheit, wenn eine vorhanden ist und liefert nur den Zahlenwert (bezogen auf die Einheit!). Bei einer SI-Einheit wird der Zahlenwert bezogen auf die Basiseinheit geliefert, bei dimensonslosen Größen wird der Zahlenwert bezogen auf die verwendete dimensionslose Einheit gewählt.  numeric(x)*unit(x) liefert wieder x DEMO-Beispiel |
| [originnumeric](originnumeric/index.md) | liefert immer den Zahlenwert einer einheitenbehafteten Größe bezogen auf die vorhandene Einheit. Gibt es keine Originaleinheit da der Wert berechnet wurde wird der Zahlenwert bezogen auf die SI-Grundeinheit genommen.  originnumeric(x)*originunit(x) liefert wieder x DEMO-Beispiel |
| [originunit](originunit/index.md) | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 zurück.  originnumeric(x)*originunit(x) liefert wieder x DEMO-Beispiel |
| [removeunit](removeunit/index.md) | entfernt bei einem Ausdruck alle Einheiten und ersetzt dabei alle einheitenbehafteten Größen durch den Zahlenwert bezogen auf die BasisEinheit des SI-Systems DEMO-Beispiel |
| [splitoptunit](splitoptunit/index.md) | Zerlegt einen numerischen Wert in Zahlenwert und die optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1 |
| [splitunit](splitunit/index.md) | Zerlegt einen numerischen Wert in Zahlenwert und die originale/optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1 |
| [todB](todb-gross-3/index.md) | versieht einen Zahlenwert mit der skalierenden Dezibel-Einheit dB welche mit 20*log10 berechnet wird DEMO-Beispiel |
| [unit](unit/index.md) | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 ohne Einheitenvielfache zurück.  numeric(x)*unit(x) liefert wieder x DEMO-Beispiel |
| [unitopt](unitopt/index.md) | liefert bei einem einheitenbehafteten Wert die optimale SI-Einheit mit optimierten Einheitenvielfachen |
