# Installieren von JDK-21
Ab rev6600 (August 2024) vom Setup-Service welches direkt am Host installiert ist muss mindestens JDK-21 
am Host installiert sein. Dies betrifft nicht die Services welche in Docker-Containern laufen da dort
das JDK vom Container bereitgestellt wird.

## in Ubuntu 20.04
als root:
<pre>add-apt-repository ppa:openjdk-r/ppa
apt-get -y update
apt-get -y install openjdk-21-jdk openjdk-21-jre openjdk-21-jre-headless openjdk-21-source
</pre>

## in Ubuntu 22.04 und 24.04
als root:
<pre>apt-get -y install openjdk-21-jre openjdk-21-jdk openjdk-21-jre-headless openjdk-21-source</pre>

## in Debian 11(bullseye) oder Debian 12(bookworm)
als root:
<pre>apt update
apt install wget apt-transport-https
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/trusted.gpg.d/adoptium.asc
echo "deb https://packages.adoptium.net/artifactory/deb bullseye main" | tee /etc/apt/sources.list.d/adoptium.list
apt update
apt install temurin-21-jdk
java -version</pre>

