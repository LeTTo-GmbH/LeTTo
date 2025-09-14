# FAQ Frequently Asked Questions - Häufig gestellte Fragen

## Loginprobleme

#### Ich habe mein ***Passwort vergessen***, was kann ich tun?
  - Als Schüler wende dich an einen Lehrer deiner Schule - er kann dir das [Passwort für LeTTo zurücksetzen](../Schülerpasswortsetzen/index.md).
  - Als Lehrer wende dich an den LeTTo-Administrator deiner Schule - er kann dir das Passwort für LeTTo zurücksetzen.

#### Login am LeTTo-Server funktioniert nicht da der ***Fingerprint*** leer ist
  - Ursache: Der Browser kann der Fingerprint nicht erstellen da ein Adblocker oder ein Script-Blocker (NoScript, uBlock Origin, ...) die notwendigen Scripte blockiert.
  - Lösung: Adblocker oder Script-Blocker für die Letto-Seite deaktivieren und Seite neu laden.

#### Login an einem LeTTo-Server welcher das Passwort an einer ***Active-Directory*** oder ***LDAP-Domain*** checkt funktioniert nicht obwohl die Benutzerdaten und das Passwort sicher stimmen.
  - mögliche Ursachen: 
    - Der LeTTo-Server kann die Domain nicht erreichen (Netzwerkproblem, Firewall, DNS-Problem, ...)
      - Lösung: Den LeTTo-Administrator der Schule informieren damit er das Problem beheben kann.
    - Das Passwort enthält Sonderzeichen welche in der Kommunikation mit der Domain nicht korrekt übermittelt werden.
      - Lösung: Das Passwort auf der Domain ändern und dabei keine Umlaute und Sonderzeichen mit Ausnahme von Minus,Unterstrich und Rufzeichen verwenden.
  - alternative Lösung: Der Lehrer/Administrator kann das Passwort auch direkt im LeTTo-Server zurücksetzen - dann wird das Passwort nur lokal am LeTTo-Server geändert und nicht an der Domain.

  
