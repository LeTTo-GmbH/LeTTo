# Login

## Login am LeTTo-Server
* Standard-Einstieg für Schüler und Lehrer
* Server: https://serveradresse/letto[Schulkürzel]<br>
  zB: https://letto.htlstp.ac.at/lettohtlstp , https://s2.letto.at/lettomint2 , https://s1.letto.at/lettoexchange <br>
  ![img.png](img.png)

## Login in der LeTTo-App
* Neuerdings ist es möglich, sich auch über die LeTTo-App mit dem Benutzernamen und Passwort anzumelden.
* Die App wird in Zukunft auch für Android im Playstore verfügbar sein.
* Start der App am Browser: https://serveradresse/app<br>
  zB: https://letto.htlstp.ac.at/app , https://s2.letto.at/app , https://s1.letto.at/app <br>
  ![img_1.png](img_1.png)  
* Die Schulauswahl steht nur zur Verfügung wenn der Server mehrere Schulen verwaltet.
* Die App kann auch als [Android-App-APK](https://download.letto.at/download/app/stable) installiert werden. 

## Login mit dem Login-Service
* Der Login direkt am Login-Service ist nur für spezielle Anwendungen gedacht
* bei Servern mit AD oder LDAP Anbindung kann man sich hier nur anmelden wenn man sich mit dem gleichen Passwort auch schon am LeTTo-Server angemeldet hat.
* Diese Login-Seite sollte nur in Ausnahmefällen verwendet werden.
* Server: https://serveradresse/login<br>
  zB: https://letto.htlstp.ac.at/login , https://s2.letto.at/login , https://s1.letto.at/login <br>
  ![img_2.png](img_2.png) 

## Login im Setup-Service
* Der Login im Setup-Service ist nur für Administratoren gedacht
* Hier können sich nur Administratoren anmelden um den Server zu konfigurieren
* Server: https://serveradresse/config<br>
  zB: https://letto.htlstp.ac.at/config , https://s2.letto.at/config , https://s1.letto.at/config <br>
  ![img_3.png](img_3.png)

## Login in OpenProject [https://project.letto.at](https://project.letto.at)
* Die Logins am OpenProject-Server sind unabhängig von den LeTTo-Logins
* Jeder Benutzer muss sich separat am OpenProject-Server anmelden. 
* Bitte immer mit der Schul-Email-Adresse anmelden.
* Server: https://project.letto.at<br>
* Lehrer werden für die Benutzung freigeschaltet wenn sie nach der Registrierung eine Email an <mailto:werner.damboeck@letto.at> senden.
  - Bitte um Angabe der Schule und der Email-Adresse. 
  - Bitte um Geduld, die Freischaltung erfolgt manuell.
  - Bitte im Verständis dass wir keine Benutzer freischalten können die keine Schul-Email-Adresse verwenden, oder wo wir die Schulzugehörigkeit nicht nachvollziehen können.
* Der Project-Server dient zur Meldung von Fehlern, zur Dokumentation und für die Verwaltung von Aufgaben.
* Weiters befindet sich darauf ein Forum für Fragen und Antworten rund um LeTTo.
* Schüler sollten sich nicht am Project-Server anmelden.