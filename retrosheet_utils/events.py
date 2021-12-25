from retrosheet_utils.scraper import Scraper

import zipfile
from io import BytesIO
from typing import List
from urllib.request import urlopen


class Events(Scraper):
    def __init__(self, player: str, year: str) -> None:
        super().__init__(year)
        self.player = player.title().split()

        self.event_url = Scraper(year).event_url

        self.team = self.find_abbreviation()

    def find_abbreviation(self) -> str:
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for i in file.namelist():
            for z in file.open(i).readlines():
                if all(j in z.decode("utf-8") for j in self.player):
                    return z.decode("utf-8").split(",")[-2]

    def find_player_id(self) -> str:
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for z in file.open(self.team + self.year+'.ROS').readlines():
            if all(j in z.decode("utf-8") for j in self.player):
                return z.decode("utf-8")[:8]

    def find_every_plate_appearance(self) -> List:
        plate_a = []
        handle = urlopen(self.event_url)
        file = zipfile.ZipFile(BytesIO(handle.read()))
        for i in file.namelist():
            for z in file.open(i).readlines():
                if i.endswith("EVN") or i.endswith("EVA"):
                    ab = z.decode("utf-8").split(',')
                    if ab[-2] and self.find_player_id() in ab and ab[0] == \
                            'play':
                        x = ab[-1].replace('/', "*").replace(".", "*"). \
                            replace("+", "*").replace("\r", "*"). \
                            replace("\n", "*")

                        plate_a.append((ab[-2], x.split('*')[0]))
        return self.clean_data(plate_a)

    @staticmethod
    def clean_data(pa_list):
        clean_list = []
        for i in pa_list:
            j = i[0].replace('*', '').replace('>', ''). \
                replace('.', '').replace('+', ''). \
                replace('1', '').replace('2', '').replace('3', '')

            clean_list.append((j, i[-1]))
        return clean_list
