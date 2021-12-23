from retrosheet_utils.scraper import Scraper
from retrosheet_utils.events import Events

from urllib.request import urlopen


class People(Scraper):
    def __init__(self, person: str, year: str) -> None:
        super().__init__(year)
        self.person = person.title().split()

        self.player_info_url = "https://www.retrosheet.org/boxesetc/B/P" + \
                               Events(person, self.year).find_player_id() + \
                               ".htm"

    def find_player_info(self):
        handle = urlopen(self.player_info_url)


People("Barry Bonds", '2004').find_player_info()
