import zipfile
from io import BytesIO
from urllib.request import urlopen

team_abr_url = 'https://www.retrosheet.org/TEAMABR.TXT'


class Scraper:

    def __init__(self, player: str, year: str, team: str) -> None:
        self.player = player.split()
        self.year = year
        self.team = team.split()
        self.event_url = 'https://www.retrosheet.org/events/' + year + 'eve.zip'

    def find_abbreviation(self):
        for i in urlopen(team_abr_url):
            if all(j in i.decode("utf-8") for j in self.team):
                return i.decode("utf-8")[1:4]

    def find_player_id(self):
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for z in file.open(self.find_abbreviation() + '2004.ROS').readlines():
            if all(j in z.decode("utf-8") for j in self.player):
                return z.decode("utf-8")[:8]
