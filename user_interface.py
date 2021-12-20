from scrape_retrosheet import Scraper

x = input("Type a player and season in the form 'Player Player YEAR',")

z = x.split()
x = z[0] + z[1]
y = z[-1]
sr = Scraper(x, y)

print(sr.find_player_id())
print(sr.find_abbreviation())
