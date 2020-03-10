from radio import Radio
from bluetooth import Bluetooth
from time import sleep

try:
  from gpiozero import Button
  runningOnRaspi = True
except:
  runningOnRaspi = False

radio = Radio()
bluetooth = Bluetooth()

def switchToBluetooth():
  if mode == "bluetooth":
    return
  global mode
  mode = "bluetooth"

  print("Load Bluetooth")

  radio.stop()
  bluetooth.start()

  nextButton.when_pressed = None
  prevButton.when_pressed = None

def switchToRadio():
  if mode == "radio":
    return
  global mode
  mode = "radio"

  print("Load Radio")

  bluetooth.stop()
  radio.start()

  nextButton.when_pressed = radio.nextStation
  prevButton.when_pressed = radio.prevStation

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
  sleep(10)