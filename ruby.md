# Installiere Ruby 
* Download von https://rubyinstaller.org/ und Installation

# Installation von Ruby Plugin in der IntelliJ
* File-Settings-Plugins - Ruby Plugin
  * Plugin installieren und dann die IntelliJ restarten
* Konfiguration
  <pre>gem install bundler
  gem update
  </pre>
* wichtige Kommandos
  * zeige alle installierten gems<br><pre>gem list</pre>
  * zeige info zu einem gem<br><pre>gem info gam_name</pre>
  * zeige die Umgebung<br><pre>gem env</pre>

# Installation von Jekyll
* braucht man für die GitHub-Pages
* Installation 
  <pre>gem install bundler jekyll
  bundle install
  </pre>
* gehe ins Verzeichnis docs
  <pre>echo 'source "https://rubygems.org"' > Gemfile
  echo 'gem "jekyll"' >> Gemfile
  </pre>
* wandle mit Geany die Datei Gemfile in eine UTF-8 Datei! 
* Füge alle notwendigen Packete in das Gemfile ein
* weiter im gleichen Verzeichnis
  <pre>bundle install
  bundle exec jekyll build
  </pre>


bundle exec jekyll serve
bundle exec jekyll build