---
name: plugin-doku
description: Erzeugt oder aktualisiert die Doku des Java-Referenz-Plugins (plugin-demo-java) unter docs/wiki/Plugins/referenz-plugin-java aus dem Sourcecode. Verwenden, wenn die Plugin-Doku neu generiert, aktualisiert oder mit dem Plugin-Code abgeglichen werden soll.
---

# Doku des Referenz-Plugins generieren

Erzeuge bzw. aktualisiere die Dokumentation des Java-Referenz-Plugins für die GitHub-Pages-Doku von LeTTo.

## Quelle und Ziel

- **Quelle:** `../plugin-demo-java` (Repo https://github.com/LeTTo-GmbH/plugin-demo-java), relativ zum LeTTo-Repo-Root.
  Falls das Verzeichnis nicht erreichbar ist: abbrechen und den Benutzer bitten, Claude im LeTTo-Repo mit
  `--add-dir ../plugin-demo-java` zu starten bzw. beide Repos nebeneinander auszuchecken.
- **Ziel:** `docs/wiki/Plugins/referenz-plugin-java/` – Dateien außerhalb dieses Ordners nur wie unter „Verlinkung" beschrieben ändern.

Relevante Quellen im Plugin-Repo:

| Quelle | Inhalt für die Doku |
|---|---|
| `README.md`, `HELP.md` | Anleitung „Neues Plugin erstellen", Build, Debugging |
| `src/main/java/at/letto/plugins/controller/*` | REST-Endpunkte (Pfad, Methode, Request-/Response-DTO, JavaDoc, Swagger-Annotationen) |
| `src/main/java/at/letto/plugins/dto/*`, `enums/*` | DTOs und Enums der Schnittstelle |
| `src/main/java/at/letto/plugins/plugin/BasePlugin.java`, `PluginService.java` | Plugin-API: welche Methoden ein Plugin überschreibt |
| `src/main/java/at/letto/plugins/plugin/uhr/PluginUhr.java`, `src/main/resources/plugins/uhr/*` | Beispiel-Plugin (Uhr) |
| `src/main/java/at/letto/plugins/config/*` | Konfiguration, Endpoint-Pfad, Registrierung am LeTTo-Server |
| `build/`, `Dockerfile`, `yml/`, `proxy/` | Build, Docker-Deployment, Proxy |
| `src/main/resources/help/index.html` | Hilfeseite des Services |

## Seitenstruktur

Jede Seite ist ein eigener Ordner mit `index.md` (Konvention der LeTTo-Doku):

```
docs/wiki/Plugins/referenz-plugin-java/
  index.md                  Überblick, Zweck, Links zu GitHub/Swagger/JavaDoc, Inhaltsverzeichnis
  architektur/index.md      Aufbau des Services, Paketstruktur, Ablauf LeTTo-Server <-> Plugin (gern als Mermaid-Diagramm)
  eigenes-plugin/index.md   Schritt-für-Schritt: neues Plugin aus dem Demoprojekt erstellen (setpluginname, BasePlugin, StartupConfiguration, Ressourcen)
  plugin-api/index.md       BasePlugin: überschreibbare Methoden mit Zweck, Parametern, Rückgabe; am Uhr-Plugin erklärt
  rest-schnittstelle/index.md  alle Endpunkte als Tabellen je Controller: Methode, Pfad, Request-DTO, Response-DTO, Beschreibung
  dtos/index.md             alle DTOs und Enums: Felder, Typen, Bedeutung (aus JavaDoc/Swagger-@Schema)
  build-deployment/index.md Build (build.bat/build.sh), Docker, Proxy-Konfiguration, Registrierung am Server, Debugging
```

Nicht vorhandene Inhalte nicht erfinden: Wenn im Code etwas nicht dokumentiert oder unklar ist, kurz so kennzeichnen
(„im Code nicht dokumentiert") statt zu raten.

## Format-Konventionen

- Sprache: Deutsch, Stil wie die bestehenden Seiten in `docs/wiki/` (knappe Aufzählungen, Tabellen).
- **Kein YAML-Front-Matter.** Jede Seite beginnt mit einer `# Überschrift` (daraus erzeugt GitHub Pages den Titel).
- Direkt unter der Überschrift steht als HTML-Kommentar der Quellstand:
  `<!-- generiert aus plugin-demo-java @ <commit-hash> (revision <inhalt von revision.txt>) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->`
- Links relativ mit `../xyz/index.md`, wie in den bestehenden Seiten.
- Jede Unterseite hat am Ende einen Link zurück zur Übersicht `../index.md`.
- Code-Beispiele als ```java bzw. ```bash-Blöcke, kurz halten und nur Ausschnitte zitieren, die den Sachverhalt zeigen.
- Bilder in den jeweiligen Seitenordner legen und relativ einbinden.

## Ablauf

1. **Quellstand ermitteln:** `git -C ../plugin-demo-java rev-parse --short HEAD` und `revision.txt` lesen.
   Auf uncommittete Änderungen im Plugin-Repo hinweisen (`git -C ../plugin-demo-java status -s`).
2. **Neu oder inkrementell?**
   - Existiert der Zielordner noch nicht: alle Seiten neu erzeugen.
   - Sonst den Hash aus dem Kommentar in `index.md` lesen und mit
     `git -C ../plugin-demo-java diff --stat <alter-hash>..HEAD` die Änderungen ermitteln.
     Nur die betroffenen Seiten aktualisieren und überall den Kommentar auf den neuen Hash setzen.
     Wenn der Benutzer „komplett neu" verlangt, alles neu erzeugen.
3. **Quellen lesen** (siehe Tabelle) und die Seiten schreiben.
4. **Verlinkung** (nur diese Änderungen außerhalb des Zielordners):
   - `docs/wiki/Plugins/index.md`, Abschnitt „Plugin-Entwicklung": Link auf `../Plugins/referenz-plugin-java/index.md`
     als empfohlenen Einstieg ergänzen. Veraltete Verweise (z. B. auf `letto-pluginuhr`) nicht löschen, sondern den Benutzer fragen.
   - `docs/wiki/index.md`: Eintrag „Referenz-Plugin (Java)" alphabetisch passend einfügen, falls noch nicht vorhanden.
5. **Prüfen:**
   - Alle relativen Links im Zielordner zeigen auf existierende Dateien.
   - Jeder Endpunkt aus den Controllern und jedes DTO aus `dto/` kommt in der Doku vor (Abgleich per Grep).
   - Falls Ruby/Jekyll lokal verfügbar ist, optional `bundle exec jekyll build` in `docs/` ausführen.
6. **Zusammenfassung** für den Benutzer: Quellstand, neue/geänderte Seiten, offene Punkte (undokumentierte Stellen).
   Nicht committen, außer der Benutzer verlangt es.
