import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rnd

#Import postseason (bubble) data for LA Lakers and MIA Heat
df = pd.read_csv("/Users/jchoudhri1/01-NBA-Project/nba-postseason2020.csv")
lal = df[df.Team == 'LAL']
mia = df[df.Team == 'MIA']

#Fix Date
lal.Date = lal.Date.apply(lambda x: pd.to_datetime(x, format= '%Y-%m-%d', errors='ignore'))
lal = lal[lal['Date'] > pd.to_datetime('20201808', format= '%Y%m%d', errors='ignore')]
mia.Date = mia.Date.apply(lambda x: pd.to_datetime(x, format= '%Y-%m-%d', errors='ignore'))
mia = mia[mia['Date'] > pd.to_datetime('20201808', format= '%Y%m%d', errors='ignore')]

#Show differences in total team points
lal.TeamPoints.hist()
mia.TeamPoints.hist()

#Calculate mean and standard deviation (SD) points for each team
lalmeanpts = lal.TeamPoints.mean()
lalsdpts = lal.TeamPoints.std()
miameanpts = mia.TeamPoints.mean()
miasdpts = mia.TeamPoints.std()
#Calculate mean and standard deviation (SD) points for each team
lalmeanopp = lal.OpponentPoints.mean()
lalsdopp = lal.OpponentPoints.std()
miameanopp = mia.OpponentPoints.mean()
miasdopp = mia.OpponentPoints.std()

print("LA Lakers Points Mean:", lalmeanpts)
print("LA Lakers Points SD:", lalsdopp)
print("Miami Heat Points Mean:" ,miameanpts)
print("Miami Heat Points SD:" , miasdpts)
print("----------------")
print("LA Lakers OppPoints Mean ", lalmeanopp)
print("LA Lakers OppPoints STD", lalsdopp)
print("Miami Heat OppPoints Mean", miameanopp)
print("Miami Heat OppPoints STD", miasdopp)

rnd.gauss(lalmeanpts, lalsdpts)

#Define gameSim. Simulates outcome of game. Returns 1 if LAL win, returns -1 if MIA win.
def gameSim():
    LALScore = (rnd.gauss(lalmeanpts, lalsdpts) + rnd.gauss(miameanopp, miasdopp)) / 2
    MIAScore = (rnd.gauss(miameanpts, miasdpts) + rnd.gauss(lalmeanopp, lalsdopp)) / 2

    if int(round(LALScore)) > int(round(MIAScore)):
        return 1
    elif int(round(LALScore)) < int(round(MIAScore)):
        return -1
    else:
        return 0

#Finals simulator. Simulates a 7 game series between MIA Heat and LAL Lakers.
def gamesSim(ns):
    gamesout = []
    team1win = 0
    team2win = 0
    tie = 0
    winner = ""
    for i in range(ns):
        if team1win == 4 or team2win == 4:
            break
        gm = gameSim()
        gamesout.append(gm)
        if gm == 1:
            team1win += 1
        elif gm == -1:
            team2win += 1
        elif (team1win == 4 or team2win == 4):
            break
    if team1win == 4:
        winner = "Los Angeles Lakers"
    if team2win == 4:
        winner = "Miami Heat"
    numGames = len(gamesout)
    print("The",winner,"have won the NBA finals in",numGames, "games!")
    print('Team1 Win', team1win / (team1win + team2win + tie), '%')
    print('Team2 Win', team2win / (team1win + team2win + tie), '%')
    print('Tie', tie / (team1win + team2win + tie), '%')
    return gamesout

gamesSim(7)