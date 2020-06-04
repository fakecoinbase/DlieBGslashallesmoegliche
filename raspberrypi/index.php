<html>
<head>
<title>Raspberry Pi Setup | DlieBG</title>
</head>
<body>

<p style="font-size:1.5em;">
Raspberry Pi Default-Setup by DlieBG
</p>

<p>
Bibliotheken updaten und Pakete upgraden (bei komplett neu aufgesetzten Systemen nicht nötig):<br>
<code>sudo apt-get update</code><br>
<code>sudo apt-get upgrade</code>
</p>

<p>
Apache2 und PHP:<br>
<code>sudo apt-get install apache2 libapache2-mod-php php</code>
</p>

<p>
Statische IPv6 Interface-ID:<br>
<code>sudo nano /etc/dhcpcd.conf</code>
<code style="margin-left:2em;">slaac hwaddr</code>
<code style="margin-left:2em;">#slaac private</code>
</p>

<p>
SSL:<br>
<code>sudo apt-get install python-certbot-apache</code><br>
<code>sudo certbot --apache</code><br>
<code>sudo nano /home/pi/renew-certs.sh</code><br>
<code style="margin-left:2em;">certbot renew -q</code><br>
<code>sudo chmod +x renew-certs.sh</code><br>
<code>sudo crontab -e</code><br>
<code style="margin-left:2em;">* 3 * * * /home/pi/renew-certs.sh</code>
</p>

<p>
Pi-hole:<br>
<code>sudo curl -sSL https://install.pi-hole.net | bash</code>
</p>

<p>
OpenVPN:<br>
<code>curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh</code><br>
<code>chmod +x openvpn-install.sh</code><br>
<code>./openvpn-install.sh</code>
</p>

<p>
NAS:<br>
<code>sudo nano mount.sh</code><br>
<code style="margin-left: 2em;">sudo mount -t cifs -o user=Public,password='',rw,file_mode=0777,dir_mode=0777 //192.168.0.132/Public /home/pi/NAS/Public</code><br>
<code style="margin-left: 2em;">sudo mount -t cifs -o user=Benedikt,password='passwort',rw,file_mode=0777,dir_mode=0777 //192.168.132/Benedikt /home/pi/NAS/Benedikt</code>
</p>

</body>
</html>
