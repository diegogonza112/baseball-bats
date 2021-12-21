import zipfile
from io import BytesIO
from typing import Dict, List
from urllib.request import urlopen

team_abr_url = 'https://www.retrosheet.org/TEAMABR.TXT'


class Scraper:

    def __init__(self, player: str, year: str) -> None:
        self.player = player.title().split()
        self.year = year
        self.event_url = 'https://www.retrosheet.org/events/' + year + 'eve.zip'
        self.team = self.find_abbreviation()
        self.playerID = self.find_player_id()

    def find_abbreviation(self) -> str:
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for i in file.namelist():
            for z in file.open(i).readlines():
                if i.endswith("ROS") and all(j in z.decode("utf-8") for j in
                                             self.player):
                    return z.decode("utf-8").split(",")[-2]

    def find_player_id(self) -> str:
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for z in file.open(self.team + '2004.ROS').readlines():
            if all(j in z.decode("utf-8") for j in self.player):
                return z.decode("utf-8")[:8]

    def find_every_plate_appearance(self) -> Dict:
        plate_a = {}
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for i in file.namelist():
            for z in file.open(i).readlines():
                if i.endswith("EVN") or i.endswith("EVA"):
                    ab = z.decode("utf-8").split(',')
                    if ab[-2] and self.playerID in ab and ab[0] == 'play':
                        x = ab[-1].replace('/', "*").replace(".", "*").\
                            replace("+", "*").replace("\r", "*").\
                            replace("\n", "*")

                        plate_a[ab[-2]] = x.split('*')[0]
        return plate_a


sr = Scraper('Barry bonds', '2004')
print(sr.find_every_plate_appearance())
