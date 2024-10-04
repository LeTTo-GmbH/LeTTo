= Installieren von JDK-21 =
Ab rev6600 (August 2024) vom Setup-Service welches direkt am Host installiert ist muss mindestens JDK-21 
am Host installiert sein. Dies betrifft nicht die Services welche in Docker-Containern laufen da dort
das JDK vom Container bereitgestellt wird.

siehe auch:
* [[Update_rev66xx]]
* [[Administration]]

== in Ubuntu 20.04 ==
als root:
&lt;pre&gt;add-apt-repository ppa:openjdk-r/ppa
apt-get -y update
apt-get -y install openjdk-21-jdk openjdk-21-jre openjdk-21-jre-headless openjdk-21-source
&lt;/pre&gt;

== in Ubuntu 22.04 und 24.04 ==
als root:
&lt;pre&gt;apt-get -y install openjdk-21-jre openjdk-21-jdk openjdk-21-jre-headless openjdk-21-source&lt;/pre&gt;

== in Debian 11(bullseye) oder Debian 12(bookworm) ==
als root:
&lt;pre&gt;apt update
apt install wget apt-transport-https
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/trusted.gpg.d/adoptium.asc
echo "deb https://packages.adoptium.net/artifactory/deb bullseye main" | tee /etc/apt/sources.list.d/adoptium.list
apt update
apt install temurin-21-jdk
java -version&lt;/pre&gt;

