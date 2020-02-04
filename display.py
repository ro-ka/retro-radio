from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("black")
inky_display.set_border(inky_display.WHITE)
font = ImageFont.truetype(FredokaOne, 22)

def showStationName(stationName):
  img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
  draw = ImageDraw.Draw(img)

  w, h = font.getsize(stationName)
  x = (inky_display.WIDTH / 2) - (w / 2)
  y = (inky_display.HEIGHT / 2) - (h / 2)

  draw.text((x, y), stationName, inky_display.BLACK, font)
  inky_display.set_image(img)
  inky_display.show()