from scrape_retrosheet import Scraper

x = input("Type a player and year they played in, in the form 'Player Player"
          " 2021'")

x = x.split(' ')

sr = Scraper(x[0].join(x[1]), x[-1])

print(sr.scrape())

