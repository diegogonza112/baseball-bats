from scrape_retrosheet import Scraper

x = input("Type a player in the form 'Player Player'")
y = input(f"Type the year {x} played in")
z = input(f"Type the team {x} played for")


sr = Scraper(x, y, z)

print(sr.find_player_id())
print(sr.find_abbreviation())
