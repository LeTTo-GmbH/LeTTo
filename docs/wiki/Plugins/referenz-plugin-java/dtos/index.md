# DTOs und Enums des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* Pakete: `at.letto.plugins.dto` und `at.letto.plugins.enums`.
* Die DTOs werden als JSON übertragen; Feldnamen im JSON entsprechen den Java-Feldnamen.
* Getter/Setter und Konstruktoren erzeugt Lombok.

## Request-DTOs

Fast alle Requests an den [ApiController](../rest-schnittstelle/index.md) enthalten die drei Felder:

| Feld | Typ | Bedeutung |
|---|---|---|
| `typ` | String | Typ des Plugins |
| `name` | String | Name des Plugins in der Frage |
| `config` | String | Konfigurationsstring des Plugins |

In den folgenden Tabellen sind nur die zusätzlichen Felder angeführt.

### PluginRequestDto

Auswahl eines Plugins anhand von Typ, Name und Konfiguration. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `params` | String | Parameter für die Antworterzeugung |
| `q` | PluginQuestionDto | Frage, in der das Plugin eingebettet ist |
| `pluginMaximaCalcMode` | PluginMaximaCalcModeDto | Art der Berechnung |

### LoadPluginRequestDto

Laden eines Plugin-DTOs. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `params` | String | Parameter für die Antworterzeugung |
| `q` | PluginQuestionDto | Frage, in der das Plugin eingebettet ist |
| `nr` | int | laufende Nummer für alle PIG-Tags und Question-Plugins |
| `configurationID` | String | Konfigurations-ID, wenn das PluginDto über Ajax bei der Konfiguration angefordert wird |

### PluginAngabeRequestDto

Verarbeitung eines Angabetextes. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `text` | String | Angabetext der Frage oder Text in PI-Tags |
| `q` | PluginQuestionDto | Frage, in der das Plugin eingebettet ist |

### PluginParserRequestDto

Auswertung einer Plugin-Parserfunktion. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `vars` | VarHashDto | alle Variablen der Frage |
| `cp` | CalcParamsDto | Berechnungsparameter |
| `p` | CalcErgebnisDto[] | Werte, die von der Frage an das Plugin übergeben werden |

### PluginEinheitRequestDto

Bestimmung der Ergebniseinheit. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `p` | String[] | Einheiten der Parameter als Recheneinheiten |

### PluginScoreRequestDto

Bewertung einer Plugin-Antwort. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `pluginDto` | PluginDto | PluginDto, das für die JavaScript-aktive Eingabe aufbereitet wurde |
| `antwort` | String | Antwort des Schülers |
| `toleranz` | ToleranzDto | Toleranz für die Lösung |
| `varsQuestion` | VarHashDto | VarHash aller Variablen der Frage |
| `answerDto` | PluginAnswerDto | korrekte Antwort und Informationen für den Scorer (JavaDoc im DTO: „Antwort des Schülers" – laut Controller ist es die Musterlösung) |
| `grade` | double | maximale Punktanzahl für die richtige Antwort |

### PluginRenderResultRequestDto

Darstellung einer bewerteten Antwort. Felder wie `PluginScoreRequestDto` und zusätzlich:

| Feld | Typ | Bedeutung |
|---|---|---|
| `tex` | boolean | `true` für LaTeX-Code, `false` für HTML-Code |

### PluginRenderLatexRequestDto

LaTeX-Ausgabe eines Plugins. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `pluginDto` | PluginDto | PluginDto, das am Webserver an das JavaScript gesandt wird |
| `answer` | String | Inhalt des Antwortfeldes des Schülers |
| `mode` | String | Druckmodus (mögliche Werte im Code nicht dokumentiert) |

### PluginUpdateJavascriptRequestDto

Aktualisierung einer Plugin-Definition anhand der JavaScript-Eingabe. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `pluginDef` | String | aktuelle Plugin-Definition |
| `jsResult` | String | Rückgabe von JavaScript |

### PluginConfigurationInfoRequestDto

Öffnen einer Plugin-Konfiguration. Felder `typ`, `name`, `config` sowie:

| Feld | Typ | Bedeutung |
|---|---|---|
| `configurationID` | String | eindeutige ID für die Verbindung zwischen Edit-Service, Browser und Plugin-Konfiguration |
| `timeout` | long | maximale Gültigkeit der Sitzung in Sekunden ohne Anfragen |

### PluginSetConfigurationDataRequestDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `typ` | String | Typ des Plugins |
| `configurationID` | String | ID der zuvor mit `configurationinfo` angelegten Sitzung |
| `configuration` | String | aktueller Konfigurationsstring |
| `questionDto` | PluginQuestionDto | Frage mit VarHashes |

### PluginConfigurationRequestDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `typ` | String | Typ des Plugins |
| `configurationID` | String | ID der Konfigurationssitzung |

## Frage und Variablen

### PluginQuestionDto

Daten, die von einer Frage an ein Plugin übergeben werden.

| Feld | Typ | Bedeutung |
|---|---|---|
| `id` | long | ID der Frage |
| `name` | String | Name der Frage |
| `maximaDefs` | String | Standarddefinitionen, die vor Maxima ausgeführt werden |
| `moodlemac` | String | Inhalt der Moodle.mac |
| `points` | double | erreichbare Punkte |
| `subQuestions` | List&lt;PluginSubQuestionDto&gt; | Teilfragen |
| `maxima` | String | Haupt-Maxima-Feld |
| `images` | List&lt;String&gt; | Dateinamen aller Bilder (md5-Prüfsumme.extension) |
| `imagesContent` | List&lt;String&gt; | Bilder als `base64:…`, externe URL (`http://`, `https://`) oder `text:…`; bevorzugt die externe URL |
| `dsNr` | int | Nummer des aktuellen Datensatzes |
| `vars` | VarHashDto | Werte aller Datensatz-Variablen |
| `cvars` | VarHashDto | Konstante und Datensatz-Variablen |
| `varsMaxima` | VarHashDto | Ergebnisse aller Maxima-Berechnungen ohne eingesetzte Datensätze |
| `mvars` | VarHashDto | Konstante, Datensatz-Variablen und Maxima-Ergebnisse mit eingesetzten Werten |

### PluginSubQuestionDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `name` | String | Name der Teilfrage |
| `points` | double | erreichbare Punkte der Teilfrage |

### VarHashDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `vars` | LinkedHashMap&lt;String, VarDto&gt; | Variablen nach Namen in Einfügereihenfolge |

### VarDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `calcErgebnisDto` | CalcErgebnisDto | Wert der Variablen |
| `ze` | String | Zieleinheit (ungeparst) |
| `cp` | CalcParamsDto | Berechnungsparameter |

### CalcErgebnisDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `string` | String | lesbarer, noch nicht geparster Ausdruck |
| `json` | String | JSON-String des CalcErgebnis-Ausdrucks |
| `type` | CALCERGEBNISTYPE | Typ, wenn nicht über JSON übertragen werden kann |

### CalcParamsDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `optmode` | String | Art der Optimierung |
| `toleranz` | ToleranzDto | Toleranz für Vergleiche |
| `rekursiv` | boolean | Auswertung rekursiv auf alle Parameter anwenden |
| `symbolicMode` | boolean | Ganzzahlen und Konstanten (e, pi) nur bei Verknüpfung mit Gleitkommazahlen als Zahlenwert einsetzen |
| `showpotenz` | SHOWPOTENZ | Darstellung von Potenzen |
| `calcmode` | CALCMODE | Art der Berechnung |
| `ausmultiplizieren` | boolean | Summen ausmultiplizieren |
| `herausheben` | boolean | aus Summen herausheben |
| `forceOpt` | boolean | `noopt` wird jedenfalls entfernt und optimiert |

### ToleranzDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `toleranz` | double | Toleranz absolut oder relativ (1 % = 0.01); Standard `1e-10` |
| `mode` | TOLERANZMODE | `RELATIV` (Standard) oder `ABSOLUT` |

### PluginMaximaCalcModeDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `maxima` | boolean | `true` Berechnung mit Maxima, `false` mit Parser (Standard `false`) |
| `preCalc` | boolean | Datensätze vor Maxima einsetzen (Standard `true`) |

## Plugin-Informationen

### PluginGeneralInfo

Allgemeine Informationen zu einem Plugin, unabhängig von einer Instanz.

| Feld | Typ | Bedeutung |
|---|---|---|
| `typ` | String | Typ des Plugins |
| `version` | String | Version |
| `wikiHelp` | String | Name der Wiki-Seite |
| `helpUrl` | String | Hilfe-URL |
| `help` | String | Hilfetext (HTML) |
| `defaultPluginConfig` | boolean | Standard-Plugin-Konfiguration verwenden |
| `math` | boolean | Plugin kann Ergebnisse und VarHash als JSON verarbeiten |
| `pluginType` | String | Klasse des Plugins |
| `initPluginJS` | String | JS-Methode zur Initialisierung der interaktiven Eingabe |
| `javaScript` | boolean | Plugin hat eine JavaScript-Schnittstelle |
| `javascriptLibraries` | List&lt;JavascriptLibrary&gt; | externe JS-Libraries (vollständige URL) |
| `javascriptLibrariesLocal` | List&lt;JavascriptLibrary&gt; | lokale JS-Libraries |
| `inputElement` | String | Eingabeelement (Name aus `InputElement`) |
| `cacheable` | boolean | Plugin ist stateless |
| `useVars` | boolean | benötigt VarHash der Datensätze |
| `useCVars` | boolean | benötigt VarHash der cvars |
| `useVarsMaxima` | boolean | benötigt VarHash der Maxima-Berechnungen ohne eingesetzte Datensätze (in `BasePlugin` heißt das Feld `useMaximaVars`) |
| `useMVars` | boolean | benötigt VarHash der Datensätze und Maxima-Ergebnisse mit eingesetzten Werten |
| `pluginServiceURL` | String | URL des Plugin-Services für die direkte Kommunikation |

### PluginGeneralInfoList

| Feld | Typ | Bedeutung |
|---|---|---|
| `pluginInfos` | List&lt;PluginGeneralInfo&gt; | Informationen aller Plugins |

### JavascriptLibrary

| Feld | Typ | Bedeutung |
|---|---|---|
| `library` | String | Ressourcenverzeichnis oder Serveradresse |
| `name` | String | Name / Bezeichner |
| `globalName` | String | relativer Pfad am JS-Server bei globalen Libraries |
| `local` | String | `LOCAL` (Ressource), `SERVER` (vollständige Adresse) oder `JAVASCRIPT` (Quelltext) |
| `js_code` | String | vollständiger JS-Code im Modus `JAVASCRIPT` |

## Darstellung

### PluginDto

Wird vom Plugin über LeTTo an das JavaScript des Plugins geschickt.

| Feld | Typ | Bedeutung |
|---|---|---|
| `imageUrl` | String | URL des Bildes, meist `data:image/png;base64,…` |
| `pig` | boolean | Plugin ist über einen PIG-Tag in der Frage eingebunden |
| `result` | boolean | Plugin ist in einer Subquestion definiert |
| `tagName` | String | eindeutiger Bezeichner, `<frageId>_<name>_<nr>` |
| `width`, `height` | int | Größe des Plugin-Bereichs in Pixel (Standard 500) |
| `params` | HashMap&lt;String,String&gt; | Parameter vom Plugin an JavaScript, von LeTTo nicht verwendet |
| `jsonData` | String | JSON vom Plugin an JavaScript, von LeTTo nicht verwendet |

### PluginRenderDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `source` | String | LaTeX- oder HTML-Quelltext |
| `images` | HashMap&lt;String,String&gt; | Bilder: Dateiname → Base64; werden im Verzeichnis `img/` relativ zum LaTeX-Quelltext abgelegt; erlaubt sind `.png`, `.jpg`, `.jpeg`, `.pdf` |

### ImageBase64Dto

| Feld | Typ | Bedeutung |
|---|---|---|
| `base64Image` | String | Base64-codiertes Bild |
| `imageInfoDto` | ImageInfoDto | Bildinformationen |
| `error` | String | Fehlermeldung, wenn das Bild nicht erzeugt werden kann |

### ImageUrlDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `imageUrl` | String | URL des Bildes |
| `imageInfoDto` | ImageInfoDto | Bildinformationen |
| `error` | String | Fehlermeldung |

### ImageInfoDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `version` | String | Plugin-Version |
| `pluginTyp` | String | Plugin-Typ |
| `filename` | String | Dateiname |
| `url` | String | öffentliche URL oder leer |
| `width`, `height` | int | Originalgröße in Pixel |
| `unit` | IMAGEUNIT | Einheit von `imageWidth` |
| `imageWidth` | int | Anzeigebreite (Standard 100) |
| `style` | String | CSS-Style |
| `alternate` | String | Alternativtext (Barrierefreiheit) |
| `title` | String | Titel |
| `lifetime` | long | Ablaufzeit in ms seit 1.1.1970 (Standard ein Jahr), ≤ 0 = unbegrenzt |

### PluginImageResultDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `ok` | boolean | nur bei `true` wurde das Bild korrekt gerendert |
| `messages` | List&lt;String&gt; | Fehlermeldungen beim Rendern |

## Bewertung

### PluginAnswerDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `ergebnis` | CalcErgebnisDto | korrektes Ergebnis |
| `answerText` | String | korrekte Antwort aus der Frage als String |
| `ze` | String | Zieleinheit für die Korrektur |

### PluginScoreInfoDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `schuelerErgebnis` | CalcErgebnisDto | Eingabe des Schülers |
| `zielEinheit` | String | Zieleinheit der Korrektur |
| `punkteIst` | double | erreichte Punkte |
| `punkteSoll` | double | erreichbare Punkte |
| `status` | Score | Bewertungsergebnis |
| `htmlScoreInfo` | String | HTML-Text mit Informationen zur Bewertung |
| `feedback` | String | Feedback |

## Datensätze

### PluginDatasetDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `name` | String | Variablenname |
| `bereich` | String | Datensatzdefinition mit Zahlenbereich |
| `einheit` | String | Zieleinheit |
| `useTemplate` | boolean | Standardwerte der übergeordneten Kategorie statt `bereich` verwenden |

### PluginDatasetListDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `datasets` | List&lt;PluginDatasetDto&gt; | Datensätze |

## Konfiguration

### PluginConfigurationInfoDto

Information vom Plugin an LeTTo, wie die Konfiguration erfolgt. Konstanten `CONFIGMODE_STRING` (0), `CONFIGMODE_JSF` (1),
`CONFIGMODE_JAVASCRIPT` (2), `CONFIGMODE_URL` (3) – siehe [Architektur](../architektur/index.md#konfigurationsdialog).

| Feld | Typ | Bedeutung |
|---|---|---|
| `configurationID` | String | Konfigurations-ID |
| `configurationMode` | int | Konfigurations-Modus |
| `useQuestion` | boolean | Frage wird benötigt |
| `useVars`, `useCVars`, `useMaximaVars`, `useMVars` | boolean | benötigte VarHashes |
| `addDataSet` | boolean | Button „AddDataset" im umgebenden Dialog |
| `calcMaxima` | boolean | Button „Maxima" im umgebenden Dialog |
| `externUrl` | boolean | Plugin ist über den Browser direkt erreichbar |
| `javaScriptMethode` | String | JS-Methode für die Konfiguration, erhält das `PluginConfigDto` |
| `configurationUrl` | String | URL des Dialogs im Modus `CONFIGMODE_URL` |

### PluginConfigDto

Wird vom Plugin über LeTTo an das JavaScript der Konfiguration geschickt.

| Feld | Typ | Bedeutung |
|---|---|---|
| `typ` | String | Typ des Plugins |
| `name` | String | Name des Plugins im Dialog |
| `config` | String | Konfigurationsstring |
| `tagName` | String | eindeutiger Bezeichner des Plugin-Tags |
| `width`, `height` | int | Größe des Plugin-Bereichs |
| `configurationID` | String | Konfigurations-ID |
| `errorMsg` | String | Fehlermeldung |
| `pluginDto` | PluginDto | PluginDto für die Initialisierung (Vorschau) |
| `pluginDtoUri` | String | URI für ein neues PluginDto (`reloadplugindto`) |
| `pluginDtoToken` | String | Token für `pluginDtoUri` (im Demo leer) |
| `params` | HashMap&lt;String,String&gt; | Parameter an JavaScript, von LeTTo nicht verwendet |
| `jsonData` | String | JSON an JavaScript, von LeTTo nicht verwendet |

### PluginConfigurationConnection

Interne Klasse (kein REST-DTO): Zustand einer Konfigurationssitzung im Plugin-Service.

| Feld | Typ | Bedeutung |
|---|---|---|
| `configurationID` | String | ID; wird zufällig erzeugt, wenn keine übergeben wurde |
| `typ`, `name`, `config` | String | Plugin-Daten |
| `pluginService` | PluginService | Plugin-Instanz der Sitzung |
| `pluginConfigurationInfoDto` | PluginConfigurationInfoDto | Konfigurationsinformation |
| `pluginConfigDto` | PluginConfigDto | aktuelles PluginConfigDto |
| `pluginQuestionDto` | PluginQuestionDto | Frage zum Plugin |
| `timeout` | long | Gültigkeitsdauer in Sekunden |
| `lastTime` | long | Zeitpunkt des letzten Zugriffs |

## Service und Registrierung

### ConfigServiceDto

Wird bei der Registrierung an das Setup-Service gesendet.

| Feld | Typ | Bedeutung |
|---|---|---|
| `name`, `version`, `author`, `license` | String | Name, Version, Autor, Lizenz des Services |
| `bs` | String | Betriebssystem |
| `ip` | String | IP des Services |
| `encoding` | String | Zeichen-Encoding |
| `programmingLanguage` | String | Programmiersprache (das Demo übergibt hier die Java-Version) |
| `nwLettoAddress` | String | Adresse im Docker-Netzwerk `nw-letto` |
| `dockerName` | String | eindeutiger Name des Docker-Containers |
| `uriIntern` | String | interne URI ohne Authentifizierung (`protokoll://adresse:port/basis`), daran werden die Plugin-Endpunkte angehängt |
| `extern` | boolean | Service ist vom Browser erreichbar |
| `uriExtern` | String | absolute externe Basis-URI |
| `plugin` | boolean | Service ist ein Plugin |
| `scalable` | boolean | Service kann mehrfach vorkommen |
| `stateless` | boolean | Service hat nur stateless Endpunkte |
| `username`, `password` | String | Zugangsdaten, wenn sich LeTTo am Plugin authentifizieren muss |
| `usePluginToken` | boolean | Token der Schule verwenden – noch nicht implementiert |
| `serviceStartTime` | long | Startzeitpunkt (DateInteger) |
| `lastRegistrationTime` | long | Zeitpunkt der letzten Registrierung |
| `params` | HashMap&lt;String,String&gt; | zusätzliche Parameter |

### RegisterServiceResultDto

| Feld | Typ | Bedeutung |
|---|---|---|
| `registrationOK` | boolean | Registrierung erfolgreich |
| `newRegistered` | boolean | neu registriert oder schon vorhanden |
| `registrationCounter` | int | Anzahl registrierter Instanzen dieses Plugin-Services |
| `msg` | String | Rückmeldung bei Fehlern |

### ServiceInfoDTO

| Feld | Typ | Bedeutung |
|---|---|---|
| `serviceName`, `version`, `author`, `license` | String | Service-Daten |
| `endpoints` | String | Information über die Endpunkte (im Demo leer) |
| `jarfilename` | String | gestartete Jar-Datei |
| `starttime` | String | Datum und Uhrzeit des Starts |
| `adminInfoDto` | AdminInfoDto | administrative Informationen |
| `jarLibs` | List&lt;String&gt; | verwendete Library-Jars |

### AdminInfoDto

Informationen über den Service für den Administrator.

| Feld | Typ | Bedeutung |
|---|---|---|
| `servicename`, `pid`, `homedir` | String | Name, Prozess-ID, Home-Verzeichnis |
| `startuptime`, `updtime` | long | Startzeit und Laufzeit in ms |
| `version`, `time` | String | Version, aktuelle Zeit am Service |
| `betriebssystem`, `ip`, `hostname`, `language` | String | Systemdaten |
| `encoding`, `fileEncoding`, `fileSeparator` | String | Encodings und Dateitrennzeichen |
| `javaSpecificVersion`, `javaVendor`, `javaVersion`, `javaVersionNumber` | String | Java-Laufzeit |
| `linuxDescription`, `linuxDistribution`, `linuxRelease` | String | Linux-Version |
| `serverUsername`, `serverVersion`, `systemHome` | String | Benutzer, Server-Version, System-Home |
| `isLinux`, `isUbuntu`, `isWindows` | boolean | Betriebssystem |
| `httpPort`, `ajpPort`, `httpsPort` | int | Ports |

## Enums

| Enum | Werte | Bedeutung |
|---|---|---|
| `CALCERGEBNISTYPE` | `CALCULATE`, `STRING`, `ERROR` | Typ eines `CalcErgebnisDto`: mathematischer Ausdruck, reiner String, Fehlermeldung |
| `CALCMODE` | `MAXIMA`, `LOESUNG`, `EQUALS`, `VIEW` | Berechnung im Maxima-Feld, der Lösung, Vergleich Schüler/Lehrer, im Angabetext |
| `IMAGEUNIT` | `none`, `px`, `pt`, `cm`, `percent`, `em` | Einheit für Bildgrößen |
| `InputElement` | `TextField`, `TextArea`, `Button`, `MULTICHOICE`, `XHTML`, `SourceCode`, `JAVASCRIPT` | Eingabeelement der Subquestion |
| `ORIENTATIONX` | `LEFT`, `CENTER`, `RIGHT` | horizontale Textausrichtung |
| `ORIENTATIONY` | `BOTTOM`, `CENTER`, `TOP` | vertikale Textausrichtung |
| `SHOWPOTENZ` | `AUTO`, `POW`, `SQRT` | Darstellung von Potenzen automatisch, als Potenz, als Wurzel |
| `TOLERANZMODE` | `RELATIV`, `ABSOLUT` | Art der Toleranz |

### Score

Ergebnis einer Beurteilung (neue Werte werden nur hinten angefügt):

| Wert | Bedeutung |
|---|---|
| `NotScored` | nicht bewertet, richtiges Ergebnis nicht bekannt (z.B. Freitext) |
| `OK` | richtig |
| `FALSCH` | falsch |
| `TEILWEISE_OK` | teilweise richtig |
| `EINHEITENFEHLER` | Einheitenfehler |
| `OK_Lehrer` | vom Lehrer als richtig beurteilt |
| `FALSCH_Lehrer` | vom Lehrer als falsch beurteilt |
| `TEILWEISE_OK_Lehrer` | vom Lehrer als teilweise richtig beurteilt |
| `EINHEITENFEHLER_Lehrer` | Einheitenfehler in der Beispielangabe |
| `ANGABEFEHLER_EH` | Ergebnis der Angabe wegen Rechenfehler nicht berechenbar |
| `PARSERFEHLER_SYSTEM` | Parser kann das richtige Ergebnis nicht berechnen |
| `NichtEntschieden` | noch nicht entschieden; sind alle Answers nicht entschieden, ist die Antwort falsch |
| `MEHRFACHANTWORT_OK` | Mehrfachbeantwortung, richtig |
| `MEHRFACHANTWORT_OK_LEHRER` | Mehrfachbeantwortung, richtig, vom Lehrer definiert |
| `MEHRFACHANTWORT_TW_RICHTIG` | Mehrfachbeantwortung, teilweise richtig |
| `MEHRFACHANTWORT_TW_RICHTIG_LEHRER` | Mehrfachbeantwortung, teilweise richtig, Lehrerbeurteilung |

[Referenz-Plugin (Java)](../index.md)
