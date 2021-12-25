import textwrap

from retrosheet_utils.scraper import Scraper
from retrosheet_utils.events import Events

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
CATEGORIES = ["Born", "First", "Final", "Bat:", "Throw:", "Height:", "Weight:"]


class People(Scraper):
    def __init__(self, person: str, year: str, person_type) -> None:
        super().__init__(year)
        self.person = person.title().split()
        self.person_type = person_type
        if person_type == "P":
            self.player_info_url = "https://www.retrosheet.org/boxesetc/B/P" + \
                               Events(person, self.year).find_player_id() + \
                               ".htm"
        elif person_type == "M":
            self.manager_info_url = "https://www.retrosheet.org/boxesetc/A/P" \
                                    + self.find_manager_id() + ".htm"
        else:
            self.ump_info_url = "https://www.retrosheet.org/boxesetc/A/P" \
                                    + self.find_ump_id()+ ".htm"

    def find_info(self):
        if self.person_type.title() == "P":
            return self.find_player_info()
        elif self.person_type.title() == "M":
            return self.find_manager_info()
        else:
            return

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

    def find_manager_info(self):
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

    def umpire_info(self):
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

    def find_manager_id(self):
        iden = ""

        return iden

    def find_ump_id(self):
        iden = ""

        return iden


print(People("Manny Acta", '2011', "M").find_info())
