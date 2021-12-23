# baseball-bats
This work is inspired by my desire to create a simple algorithm that can simulate a baseball player's season as if they didn't have a bat (see below for more info). My big barrier arose when I was trying to find easy ways to collect the information I was looking for, but I couldn't find any libraries that had the information I was searching for. Thus comes the body of this program, I will be attempting to make a python module that scrapes RetroSheet, the most comprehensive baseball records I have been able to find.

The first iteration of this algorithm will try to cover the majority of RetroSheet without considering the run time just as a proof of concept, once the proof of concept has been established, I will be working to make the program more robust and improve run time by using NumPy arrays and Pandas dataframes which should drastically improve run time.

Hopefully that wasn't too boring, but nevertheless, enjoy :)


The Project:

What if baseball bats didn't exist

The purpose of this project is to simulate any given MLB player's regular season (data availability permitting) as if they didn't have a baseball bat. Obviously, every pitcher would just throw easy floaters into the strike zone and there would just be a lot of strike outs, however; the catch is the pitchers don't know that our player doesn't have a bat, therefore the pitchers will throw exactly the same pitches they did in real life and the player will just never swing.

The program will return the player's At Bats, Bases On Balls, Intentional Bases On Balls, and On-Base Percentage. Granted there will be many players that will not have very interesting statistics, but the best hitters will have the the fear of a home-run on their side, which will lead to many intentional walks (see Barry Bonds 2004).

The information for this project if collected from RetroSheet and the inspiration for this project comes from "What if Barry Bonds had played without a baseball bat?" by SecretBase on Youtube.

RetroSheet: https://www.retrosheet.org/
SecretBase video: https://www.youtube.com/watch?v=JwMfT2cZGHg&ab_channel=SecretBase
