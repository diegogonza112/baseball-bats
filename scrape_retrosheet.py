import os
import zipfile
from io import BytesIO, StringIO
from urllib.request import urlopen


class Scraper:

    def __init__(self, player: str, year: str, team: str) -> None:
        self.player = player
        self.year = year
        self.team = team.split()
        self.event_url = 'https://www.retrosheet.org/events/' + year + 'eve.zip'


sc = Scraper("bondb001", "2004", "San Francisco Giants")

handle = urlopen(sc.event_url)

for z in zipfile.ZipFile(BytesIO(handle.read())).open('SFN2004.ROS').readlines():
    if sc.player in z.decode("utf-8"):
        print(z.decode("utf-8"))

