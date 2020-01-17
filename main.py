import player
from stations import Stations
from time import sleep

try:
  from gpiozero import Button
  runningOnRaspi = True
except:
  runningOnRaspi = False

stations = Stations(player)

if runningOnRaspi:
  nextButton = Button(5)
  prevButton = Button(6)

  nextButton.when_pressed = stations.next
  prevButton.when_pressed = stations.prev

while True:
  sleep(10)