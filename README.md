# LeTTo

Offenes Repository mit [Wiki](https://doc.letto.at/), [Discussions](https://github.com/LeTTo-GmbH/LeTTo/discussions) und wichtigen Infos zur Lernplattform [LeTTo](https://www.letto.at)

## Bilder in der IntelliJ bearbeiten
* Bildbearbeitungsprogramm installieren
  * Windows einfach: [Paint.NET](https://www.getpaint.net/download.html) [Github](https://github.com/paintdotnet/release/releases/download/v5.1.9/paint.net.5.1.9.winmsi.x64.zip) [Github-Seite](https://github.com/paintdotnet/release/releases)
  * Windows: [IrfanView](https://www.irfanview.com/)
  * Linux: [Gimp](https://www.gimp.org/)

* In IntelliJ unter File -> Settings -> Tools -> External Tools
  * Add new tool
  * Name: Paint.NET
  * Description: Bildbearbeitung mit Paint.NET
  * Program: C:\Program Files\paint.net\PaintDotNet.exe
  * Arguments: $FilePath$
  * Working directory: $ProjectFileDir$
  * OK
* Rechtsklick auf ein Bild in IntelliJ -> External Tools -> Paint.NET
* Bild automatisch in der IntelliJ per Doubleclick in Paint.NET öffnen
  * Im Windows Explorer *.png per Rechtsklick -> Open with -> Choose another app -> Paint.NET
  * Haken bei "Always use this app to open .png files" setzen
  * Dazu muss das Dateiformat in IntelliJ als "Files opened in associated applications" definiert werden
  * IntelliJ: Einstellungen / Preferences (Strg+Alt+S) → Editor → File Types.
      * Wähle in der Liste Files opened in associated applications (oder „Files opened in associated application“).
      * Füge ein Pattern *.png (oder *.PNG) hinzu.
