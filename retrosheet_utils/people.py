import textwrap

from retrosheet_utils.scraper import Scraper
from retrosheet_utils.events import Events

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
CATEGORIES = ["Born", "First", "Final", "Bat:", "Throw:", "Height:", "Weight:"]


class People(Scraper):
    def __init__(self, person: str, year: str) -> None:
        super().__init__(year)
        self.person = person.title().split()

        self.player_info_url = "https://www.retrosheet.org/boxesetc/B/P" + \
                               Events(person, self.year).find_player_id() + \
                               ".htm"

    def find_player_info(self):
        handle = urlopen(self.player_info_url)
        soup = BeautifulSoup(handle.read(), 'html.parser')
        clean_text = re.sub(CLEANER, '', str(soup.find_all("table")[0]))
        final = """"""
        i = 0

        splt = clean_text.replace(";", "").split()
        while i <= splt.index("Weight:")+1:
            if splt[i] == "name":
                final += (splt[i] + ":" + " ")
            elif splt[i] == "Born":
                final += ("\n" + splt[i] + ":" + " ")
            elif splt[i] in CATEGORIES:
                final += ("\n" + splt[i] + " ")
            else:
                final += (splt[i] + " ")
            i += 1
        return final


print(People("Barry Bonds", '2004').find_player_info())
