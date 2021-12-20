import zipfile
from io import BytesIO
from urllib.request import urlopen

team_abr_url = 'https://www.retrosheet.org/TEAMABR.TXT'


class Scraper:

    def __init__(self, player: str, year: str) -> None:
        self.player = player.title().split()
        self.year = year
        self.event_url = 'https://www.retrosheet.org/events/' + year + 'eve.zip'
        self.team = self.find_abbreviation()

    def find_abbreviation(self):
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for i in file.namelist():
            for z in file.open(i).readlines():
                if i.endswith("ROS") and all(j in z.decode("utf-8") for j in
                                             self.player):
                    return z.decode("utf-8").split(",")[-2]

    def find_player_id(self):
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for z in file.open(self.team + '2004.ROS').readlines():
            if all(j in z.decode("utf-8") for j in self.player):
                return z.decode("utf-8")[:8]


sr = Scraper("barry bonds", "2004")
print(sr.find_player_id())
