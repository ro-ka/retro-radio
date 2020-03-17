import display
import csv
import vlc

stationsFileName = 'stations.csv'
currentStationFileName = 'station-current.txt'

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()

class Station:
  def __init__(self, name, url):
    self.name = name
    self.url = url

class Radio:
  currentStationIndex = 0
  allStations = []

  def __init__(self):
    # Load stations
    with open(stationsFileName, newline='') as stationsData:
      stationsRaw = csv.reader(stationsData, delimiter=',')
      for row in stationsRaw:
        self.allStations.append(Station(row[0], row[1]))

    # Load current station
    try:
      with open(currentStationFileName, 'r') as currentStationData:
        currentStation = int(currentStationData.read())
        if currentStation >= 0 and currentStation < len(self.allStations):
          self.updateTo(currentStation)
        else:
          self.updateTo(self.currentStationIndex)
    except:
      self.updateTo(self.currentStationIndex)

  def getCurrent(self):
    return self.allStations[self.currentStationIndex]

  def nextStation(self):
    newIndex = self.currentStationIndex + 1
    if newIndex > len(self.allStations) - 1:
      newIndex = 0
    self.updateToAndStart(newIndex)

  def prevStation(self):
    newIndex = self.currentStationIndex - 1
    if newIndex < 0:
      newIndex = len(self.allStations) - 1
    self.updateToAndStart(newIndex)

  def updateTo(self, newIndex):
    self.currentStationIndex = newIndex
    self.writeCurrent(newIndex)

  def updateToAndStart(self, newIndex):
    self.updateTo(newIndex)
    self.start()

  def writeCurrent(self, newIndex):
    currentStationData = open(currentStationFileName, 'w')
    currentStationData.write(str(newIndex))
    currentStationData.close()

  def playUrl(self, url):
    media = instance.media_new(url)
    media.get_mrl()
    player.set_media(media)
    player.play()

  def setVolume(self, volume):
    player.audio_set_volume(volume)

  def start(self):
    current = self.getCurrent()
    print('Now playing: ' + current.name)
    self.playUrl(current.url)
    display.showRadioStation(current.name)

  def stop(self):
    player.stop()
