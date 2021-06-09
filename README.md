# pi-purify

This project adds wifi connectivity to the Winix C535 air purifier.  I only have one relay, so it just does speed control.

## Hardware
- Raspberry Pi Zero W (powered internally by 5v header pins)
- Relay
- Winix Air Purifier

## Software
This repo contains:
1. A Flask application which listens for requests
2. A systemd script to launch the application at boot

## Setup

```bash
apt update
apt install python3-flask

cp pi-purify.py /usr/local/bin/
cp pi-purify.service /etc/systemd/system
systemctl enable pi-purify
systemctl start pi-purify
```
