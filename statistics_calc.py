from typing import List

from retrosheet_utils.scrape_retrosheet import Scraper


class StatisticsCalculator:

    def __init__(self, pa_list: List) -> None:
        self.pa_list = pa_list

    def count_iw(self) -> int:
        count = 0
        for i in self.pa_list:
            if i[-1] == 'IW':
                count += 1
        return count


sr = Scraper('Barry bonds', '2004')
x = sr.find_every_plate_appearance()
sc = StatisticsCalculator(x)
print(len(x))
print(x)
print(sc.count_iw())

