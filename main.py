from radio import Radio
from bluetooth import Bluetooth
# from subprocess import call
from time import sleep
import Adafruit_MCP3008

try:
  from gpiozero import Button
  runningOnRaspi = True
except:
  runningOnRaspi = False

VOLUME_CHANNEL = 0
mcp = Adafruit_MCP3008.MCP3008(clk=13, cs=26, miso=25, mosi=9)

mode = None
radio = Radio()
bluetooth = Bluetooth()

def switchToBluetooth():
  global mode
  if mode == "bluetooth":
    return
  mode = "bluetooth"

  print("Load Bluetooth")

  nextButton.when_pressed = None
  prevButton.when_pressed = None

  radio.stop()
  bluetooth.start()

def switchToRadio():
  global mode
  if mode == "radio":
    return
  mode = "radio"

  print("Load Radio")

  bluetooth.stop()
  radio.start()

  nextButton.when_pressed = radio.nextStation
  prevButton.when_pressed = radio.prevStation

def getVolumeFromValue(value):
  MAX = 1023
  correctedValue = MAX - value
  volumeValue = int(round(correctedValue / float(MAX) * 100))
  volumeValue = max(volumeValue, 0)
  volumeValue = min(volumeValue, 100)
  return volumeValue

if runningOnRaspi:
  bluetoothButton = Button(16)
  radioButton = Button(20)

  global nextButton
  nextButton = Button(5)
  global prevButton
  prevButton = Button(6)

  if bluetoothButton.is_pressed:
    switchToBluetooth()

  if radioButton.is_pressed:
    switchToRadio()

  bluetoothButton.when_pressed = switchToBluetooth
  radioButton.when_pressed = switchToRadio

while True:
  value = mcp.read_adc(VOLUME_CHANNEL)
  volume = getVolumeFromValue(value)
  radio.setVolume(volume)
  # call(["amixer", "sset", "Master", str(volume)+"%"])

  sleep(0.2)