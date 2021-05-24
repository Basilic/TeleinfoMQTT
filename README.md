# TeleinfoMQTT
## Overview

Ce dépôt est un backup de ma config pour intégrer la téléinformation dans HA.

* Il contient les fichiers suivant:

	* Teleinfo.py: Ce script qui permet de lire le port serie sur lequel il est configuré et d'envoyer l'intégralité des données dans un fil MQTT.
	* teleinfo.service: Exemple de fichier a placé dans /etc/systemd/system pour démarrer le service au boot
	* 90-teleinfo.rules: permet de crée un lien symbolique au périphérique pour évité les mélanges, a placer dans /etc/udev/rules.d


## Installation:

### Dépendance:

* Python serial
* Python paho-mqtt

```
sudo apt-get install python-pyserial python-paho-mqtt
```

Si le broker est sur la meme machine et qu'il n'est pas encore installé:

```sudo apt-get install mosquitto```

### Mise en place
Déplacer le fichier Teleinfo.py dans /home/pi:

```
mv Teleinfo.py /home/pi
```

Déplacer le fichier 90-teleinfl.rules dans /etc/udev/rules.d et actualiser l'udev avec la commande:

```
sudo mv 90-teleinfo.rules /etc/udev/ruled.d/90-teleinfo.rules
sudo udevadm control --reload-rules && udevadm trigger
```

Déplacer le fichier teleinfo.service dans /etc/systemd/system et l'activé le service au boot avec la commande:

```
sudo mv teleinfo.service /etc/systemd/system
sudo systemctl enable teleinfo.service
```


