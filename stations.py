import csv

stationsFileName = 'stations.csv'
currentStationFileName = 'station-current.txt'

class Station:
  def __init__(self, name, url):
      self.name = name
      self.url = url

class Stations:
  currentIndex = 0
  all = []

  def __init__(self, player, display):
    self.player = player
    self.display = display

    # Load stations
    with open(stationsFileName, newline='') as stationsData:
      stationsRaw = csv.reader(stationsData, delimiter=',')
      for row in stationsRaw:
        self.all.append(Station(row[0], row[1]))

    # Load current station
    try:
      with open(currentStationFileName, 'r') as currentStationData:
        currentStation = int(currentStationData.read())
        if currentStation >= 0 and currentStation < len(self.all):
          self.updateTo(currentStation)
        else:
          self.updateTo(self.currentIndex)
    except:
      self.updateTo(self.currentIndex)

  def getCurrent(self):
    return self.all[self.currentIndex]

  def next(self):
    newIndex = self.currentIndex + 1
    if newIndex > len(self.all) - 1:
      newIndex = 0
    self.updateTo(newIndex)

  def prev(self):
    newIndex = self.currentIndex - 1
    if newIndex < 0:
      newIndex = len(self.all) - 1
    self.updateTo(newIndex)

  def updateTo(self, newIndex):
    self.currentIndex = newIndex
    self.writeCurrent(newIndex)
    current = self.getCurrent()
    print('Now playing: ' + current.name)
    self.player.playUrl(current.url)
    self.display.showStationName(current.name)

  def writeCurrent(self, newIndex):
    currentStationData = open(currentStationFileName, 'w')
    currentStationData.write(str(newIndex))
    currentStationData.close()