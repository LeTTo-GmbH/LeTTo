# Build und Deployment des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

## Build

* Windows: `build\build.bat`
* Linux: `build/build.sh`

Beide Scripts suchen das Projektverzeichnis (Datei `plugin-demo-java.info`), lesen den Endpoint-Pfad (`urlpath`) aus
`build/vars.bat` und führen folgende Schritte aus:

1. `revision.txt` nach `src/main/resources/revision.txt` kopieren
2. `mvn clean`
3. `mvn javadoc:javadoc` und die JavaDoc nach `src/main/resources/static/<endpoint>/open/javadoc` kopieren
4. `mvn package` (ohne Tests) → `target/plugin-demo-java-0.1.jar`
5. laufenden Container mit `docker compose -f docker-service-<endpoint>.yml down` stoppen
6. Docker-Image `lettohub/letto-service-<endpoint>:stable` neu bauen
7. `yml/docker-service-plugin.yml` als `docker-service-<endpoint>.yml` ins Compose-Verzeichnis kopieren und mit `docker compose up -d` starten

| | build.bat | build.sh |
|---|---|---|
| Java | `JAVA_HOME` fest auf `C:\Program Files\Java\jdk-25` | aus der Umgebung |
| Maven | `mvn` | `mvn`, sonst `./mvnw` |
| Compose-Verzeichnis | `\opt\letto\docker\compose\letto` | `$LETTO_COMPOSE_DIR`, Standard `/opt/letto/docker/compose/letto` |

## Docker

`Dockerfile`:

* Basis `eclipse-temurin:25-jdk-jammy`, Zeitzone Europe/Vienna, Locales `en_US.UTF-8` und `de_DE.UTF-8` (für `LC_ALL` aus der Compose-Datei)
* Jar als `plugin.jar`, Scripts nach `/scripts`
* Ports 8080 (HTTP) und 5080 (Remote-Debugging)
* Healthcheck alle 30 s mit `scripts/healthcheck.sh`: ruft `http://localhost:8080/ping` auf und erwartet `pong`. Nach
  `UNHEALTHY_RETRIES` (Standard 100) Fehlschlägen werden die Prozesse im Container beendet.
* Start mit `scripts/start.sh`; ist die Umgebungsvariable `debug=true`, wird Java mit JDWP auf Port 5080 gestartet.
  Log in `/log/start.log`.

### Compose-Datei `yml/docker-service-plugin.yml`

* Netzwerk `nw-letto` (extern), Container und Hostname `letto-<endpoint>`
* Volumes: Log (`/log`), Bilder (`/opt/letto/images`), Plugin-Bilder (`/opt/letto/plugins`)
* Debug-Port: `${DEBUG_PORT_<ENDPOINT>:-5206}` → 5080
* Speicherlimit `${<ENDPOINT>_MEMORY_LIMIT:-1G}`, Java-Optionen `${JAVA_OPTS_<ENDPOINT>:--Xms50m -Xmx500m}`

Wichtige Umgebungsvariablen:

| Variable | Bedeutung |
|---|---|
| `letto_setup_uri` | URI des Setup-Services (Standard `http://letto-setup.nw-letto:8096`) |
| `letto_user_user_password` | Passwort für die Anmeldung am Setup-Service (`SERVICE_USER_PASSWORD`) |
| `servername` | Servername (`SERVER_NAME`) |
| `letto.plugin.uri.intern` | interne URI des Plugins (Standard `http://letto-<endpoint>.nw-letto:8080`) |
| `letto.plugin.uri.extern` | externe Basis-URI (Standard `https://${SERVER_NAME}`) |
| `network.letto.address`, `docker.container.name` | Adresse und Containername, werden an das Setup gemeldet |
| `letto_pathImages`, `letto_webPathImages` | Verzeichnis und Web-Pfad der Bilder |
| `letto_pathPlugins`, `letto_webPathPlugins` | Verzeichnis und Web-Pfad der Plugin-Bilder |
| `debug` | `true` startet mit Remote-Debugging (`DEBUG_PLUGINS` bzw. `DEBUG`) |

Weitere Variablen (`jwt_secret`, `server_secret`, `spring.mail.*` u.a.) sind in der Compose-Datei gesetzt, werden im Demo-Code aber nicht ausgewertet.

## Docker Hub

* Das Image wird als [lettohub/letto-service-plugindemo](https://hub.docker.com/r/lettohub/letto-service-plugindemo) veröffentlicht, Tag `stable` = Stand von `master`.
* `build.bat` bzw. `build.sh` bauen das Image nur lokal; der Push auf Docker Hub erfolgt getrennt mit `docker push lettohub/letto-service-plugindemo:stable`.
* Die Beschreibung auf Docker Hub steht in `DOCKERHUB.md` im Repo. `build/dockerhub-description.ps1` lädt sie über die Docker-Hub-API hoch
  (PowerShell, benötigt einen Docker-Hub-Zugang mit Schreibrecht auf `lettohub`):

```bash
powershell -ExecutionPolicy Bypass -File build\dockerhub-description.ps1
```

* Zugangsdaten verwendet das Script in dieser Reihenfolge:
  1. Parameter `-User` und `-Token` bzw. Umgebungsvariable `DOCKERHUB_TOKEN` (Personal Access Token mit „Read & Write"),
  2. die Anmeldung von Docker Desktop aus dem Credential-Store (`credsStore` in `~/.docker/config.json`),
  3. interaktive Abfrage von Benutzer und Token.
* Weitere Parameter: `-Repo` (Standard `lettohub/letto-service-plugindemo`), `-Short` (Kurzbeschreibung), `-File` (Standard `DOCKERHUB.md`).

## Proxy

Die nginx-Konfiguration `proxy/<endpoint>.conf` wird von `setpluginname.bat` erzeugt:

```text
location /plugindemo/ {
     resolver 127.0.0.11 valid=5s ipv6=off;
     set $plugindemopath     letto-plugindemo.nw-letto:8080;
     proxy_set_header   Host $host;
     proxy_set_header   X-Real-IP $remote_addr;
     proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header   X-Forwarded-Proto $scheme;
     proxy_pass         http://$plugindemopath;
     proxy_read_timeout 90;
}
```

Einspielen am LeTTo-Server:

```bash
cp proxy/*.conf /opt/letto/docker/proxy/
docker restart letto-proxy
```

## Registrierung am LeTTo-Server

* Nach dem vollständigen Start (`ApplicationReadyEvent`) ruft `PluginRegistrationOnReady` die Methode
  `PluginConfiguration.registerPluginInSetup()` auf.
* Diese sendet ein [`ConfigServiceDto`](../dtos/ConfigServiceDto/index.md) per `POST` an `<letto.setup.uri>/config/auth/user/registerplugin`
  (Basic Auth mit `letto.user.user.name` / `letto.user.user.password`).
* Gemeldet werden u.a.:
  * `uriIntern` = `letto.plugin.uri.intern` + `/open` (Basis des [`ApiController`](../rest-schnittstelle/ApiController/index.md))
  * `uriExtern` = `letto.plugin.uri.extern` + `/<endpoint>/auth/user`
  * `nwLettoAddress`, `dockerName`, `plugin=true`, `extern=true`, `stateless=true`, `scalable=false`
* Das Ergebnis ([`RegisterServiceResultDto`](../dtos/RegisterServiceResultDto/index.md)) wird geloggt: neu registriert oder aktualisiert, Anzahl der Instanzen.
  Ist das Setup nicht erreichbar, wird nur ein Fehler geloggt – eine erneute Registrierung erfolgt erst beim nächsten Start.
* Die Swagger-Doku der Endpunkte des Setup-Services liegt unter `https://<servername>/config/swagger-ui/index.html`.

## Debugging und Testen

* Am Entwicklungsrechner muss eine LeTTo-Installation vorhanden sein.
* `build.bat` bzw. `build.sh` startet den Container automatisch; danach kann sofort mit dem Plugintester und im Debugger getestet werden.
* Remote-Debugging: `DEBUG_PLUGINS=true` (bzw. `DEBUG=true`) in der LeTTo-Umgebung setzen und den Debugger mit Port
  `DEBUG_PORT_<ENDPOINT>` (Standard 5206) verbinden.
* Proxy-Konfiguration einspielen (siehe oben), damit die externen Endpunkte und die Hilfeseite erreichbar sind.
* Plugintester: `https://<servername>/plugintester`, installierbar über das Setup-Service (`https://<servername>/config`).
* Erreichbarkeit prüfen: `https://<servername>/<endpoint>/open/ping` liefert `pong`.

[Referenz-Plugin (Java)](../index.md)
