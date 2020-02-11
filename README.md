# Retro Radio

Install Raspbian and setup wifi and so on.

## Speed up Raspbian boot

### Update, install vim and configure Pi

```
sudo apt update
sudo apt upgrade
sudo apt install vim
sudo raspi-config
```

### Boot config

Adjust the `/boot/config.txt` with the following (edit or add):

```
# Disable the rainbow splash
disable_splash=1

# Set bootloader delay to 0 seconds. Default is 1.
boot_delay=0
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
sudo systemctl disable apt-daily.timer
sudo systemctl disable apt-daily-upgrade.timer
sudo systemctl disable wifi-country.service
sudo systemctl disable hciuart.service
sudo systemctl disable raspi-config.service
sudo systemctl disable avahi-daemon.service
sudo systemctl disable triggerhappy.service
sudo systemctl disable rpi-eeprom-update.service
```

## Prepare deployment

Install the GPIO zero library and vlc:

```sh
sudo apt install python3-gpiozero vlc python3-vlc
```

## Connect Adafruit Speaker Bonnet

Follow [the guide](https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi?view=all) to assamble, connect and setup the Adafruit Speaker Bonnet ([PDF](docs/adafruit-speaker-bonnet.pdf)).

See the [pinouts](https://pinout.xyz/pinout/speaker_bonnet#) to connect:

![](docs/adafruit-speaker-bonnet.png)

## Connect buttons

Use two buttons for next and previous station and connect those to pins 5 and 6 and any free ground.

## OnOff Shim

Connect the [OnOff Shim](https://shop.pimoroni.com/products/onoff-shim) to the Pi and install the software with this command:

```sh
curl https://get.pimoroni.com/onoffshim | bash
```

Edit `/etc/cleanshutd.conf` to this content:

```
daemon_active=1
trigger_pin=23
#led_pin=17
poweroff_pin=4
hold_time=1
shutdown_delay=0
polling_rate=1
```

See the [pinouts](https://pinout.xyz/pinout/onoff_shim#) to connect. Note that we switched the trigger pin to 23 as the 17 is used by the Inky pHAT.

![](docs/onoff-shim.png)

## Inky pHAT

Connect the [Inky pHAT](https://shop.pimoroni.com/products/inky-phat?variant=12549254217811) to the Pi and install the software with this command:

```sh
curl https://get.pimoroni.com/inky | bash
```

See the [pinouts](https://pinout.xyz/pinout/inky_phat#) to connect:

![](docs/inky-phat.png)
