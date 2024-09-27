# Ubuntu-Server mit Netplan
Die Konfiguration erfolgt über eine Datei im Verzeichnis
  >/etc/netplan/

Der Name der Datei ist von der Schnittstelle abhängig z.B:
  >/etc/netplan/00-installer-config.yaml
   
## Beispiel für manuelle Konfiguration
<pre class="config"># Bemerkung - Netzwerk eines Rechners in einer Hyper-V
network:
  ethernets:
    eth0:
      addresses:
      - 172.28.17.11/20
      nameservers:
        addresses:
        - 8.8.8.8
        search:
        - letto.at
      routes:
      - to: default
        via: 172.28.16.1
  version: 2
</pre>