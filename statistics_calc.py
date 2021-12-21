from typing import Dict, List

from scrape_retrosheet import Scraper


class StatisticsCalculator:

    def __init__(self, pa_list: Dict) -> None:
        self.pa_list = {}
        for i in pa_list:
            j = i.replace('*', '').replace('>', '').\
                replace('.', '').replace('+', '').\
                replace('1', '').replace('2', '').replace('3', '')

            self.pa_list[j] = pa_list[i]


