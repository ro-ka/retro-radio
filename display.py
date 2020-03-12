import os
from threading import Thread
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

PATH = os.path.dirname(__file__)

inky_display = InkyPHAT("black")
inky_display.set_border(inky_display.WHITE)

fontFile = "fonts/PermanentMarker-Regular.ttf"
font = ImageFont.truetype(os.path.join(PATH, fontFile), 22)

def showRadioStationWorker(stationName):
  img = Image.open(os.path.join(PATH, "assets/display-radio.png"))
  # img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

  pal_img = Image.new("P", (1, 1))
  pal_img.putpalette((255, 255, 255) + (0, 0, 0) * 254)

  img = img.convert("RGB").quantize(palette=pal_img)
  draw = ImageDraw.Draw(img)

  fontW, fontH = font.getsize(stationName)
  fontX = (inky_display.WIDTH / 2) - (fontW / 2)
  fontY = (inky_display.HEIGHT / 2) - (fontH / 2)

  draw.rectangle(((fontX, fontY), (fontX + fontW + 10, fontY + fontH + 10)), fill=inky_display.BLACK)
  draw.rectangle(((fontX - 5, fontY - 5), (fontX + fontW + 5, fontY + fontH + 5)), fill=inky_display.BLACK)
  draw.rectangle(((fontX - 4, fontY - 4), (fontX + fontW + 4, fontY + fontH + 4)), fill=inky_display.WHITE)
  draw.text((fontX, fontY), stationName, inky_display.BLACK, font)
  inky_display.set_image(img)
  inky_display.show()

def showRadioStation(stationName):
  # Async display update
  thread = Thread(target=showRadioStationWorker, args=(stationName,))
  thread.start()

def showBluetoothWorker():
  img = Image.open(os.path.join(PATH, "assets/display-bluetooth.png"))

  pal_img = Image.new("P", (1, 1))
  pal_img.putpalette((255, 255, 255) + (0, 0, 0) * 254)

  img = img.convert("RGB").quantize(palette=pal_img)

  inky_display.set_image(img)
  inky_display.show()

def showBluetooth():
  # Async display update
  thread = Thread(target=showBluetoothWorker, args=())
  thread.start()