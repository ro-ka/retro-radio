# Retro Radio

Install Raspbian and setup wifi and so on.

## Speed up Raspbian boot

### Boot config

Adjust the `/boot/config.txt` with the following (edit or add):

```
# Disable the rainbow splash
disable_splash=1

# Set bootloader delay to 0 seconds. Default is 1.
boot_delay=0

# Overclock, voids warranty.
force_turbo=1
```

Make the kernel output less verbose by appending the following after `rootwait` in `/boot/cmdline.txt`:

```
loglevel=3 quiet logo.nologo
```

### Static IP

Define a static IP for your Pi in your router. Fritzbox makes this quite easy. Then tell the Pi to use that IP always. Edit `/etc/dhcpcd.conf` with these lines:

```
interface wlan0
static ip_address=192.168.178.178/24
static routers=192.168.178.1
static domain_name_servers=192.168.178.1 8.8.8.8

noarp
ipv4only
noipv6
```

### Disable services

Disable services that take up start time but are not needed. Check with `systemd-analyze` how long it takes to boot and identify with `systemd-analyze blame` which services take a lot of time.

```sh
sudo systemctl disable ntp.service
sudo systemctl disable dphys-swapfile.service
sudo systemctl disable keyboard-setup.service
sudo systemctl disable apt-daily.service
sudo systemctl disable apt-daily-upgrade.service
sudo systemctl disable wifi-country.service
sudo systemctl disable hciuart.service
sudo systemctl disable raspi-config.service
sudo systemctl disable avahi-daemon.service
sudo systemctl disable triggerhappy.service
```

## Prepare deployment

Install the GPIO zero library, vlc and pip, the python package manager:

```sh
sudo apt install python3-gpiozero vlc pip3
```

Install python-vlc via pip:

```sh
pip3 install python-vlc
```

## Connect Adafruit Speaker Bonnet

Follow [the guide](https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi?view=all) to assamble, connect and setup the Adafruit Speaker Bonnet ([PDF](docs/adafruit-speaker-bonnet.pdf)).

## Connect buttons

Use two buttons for next and previous station and connect those to pins 5 and 6.