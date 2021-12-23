import zipfile
from io import BytesIO
from typing import List
from urllib.request import urlopen

team_abr_url = 'https://www.retrosheet.org/TEAMABR.TXT'


class Scraper:

    def __init__(self, year: str) -> None:
        self.year = year
        self.event_url = 'https://www.retrosheet.org/events/' + year + 'eve.zip'

