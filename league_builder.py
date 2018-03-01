import csv
import random

rows = []
players = []
Sharks = []
Dragons = []
Raptors = []



def open_file():
	with open('soccer_players.csv', newline="") as csvfile:
		playerDict = csv.DictReader(csvfile, delimiter=",")
		playerDictList = list(playerDict)
		rows.extend(playerDictList)
		for player in playerDictList:
			players.append(player['Name'])
			



def divide_team():
	randomsix = random.sample(players, 6)
	Sharks.extend(randomsix)
	for player in randomsix:
		players.remove(player)
	randomsix = random.sample(players, 6)
	Dragons.extend(randomsix)
	for player in randomsix:
		players.remove(player)
	Raptors.extend(players)


def show_players():
	print(Sharks)
	print(Dragons)
	print(Raptors)


def write_file():
	with open('teams.txt', 'w') as team:
		fieldnames = ['Name', 'Soccer Experience', 'Guardian Name(s)']
		playerWriter = csv.DictWriter(team, fieldnames = fieldnames)
		team.write("*********** Sharks ***********"+"\n")
		for member in Sharks:
			for row in rows:
				if member == row['Name']:
					playerWriter.writerow({
						'Name':member,
						'Soccer Experience':row['Soccer Experience'],
						'Guardian Name(s)':row['Guardian Name(s)']
					})
		team.write("*********** Dragons ***********"+"\n")	
		for member in Dragons:
			for row in rows:
				if member == row['Name']:
					playerWriter.writerow({
						'Name':member,
						'Soccer Experience':row['Soccer Experience'],
						'Guardian Name(s)':row['Guardian Name(s)']
					})
		team.write("*********** Raptors ***********"+"\n")			
		for member in Raptors:
			for row in rows:
				if member == row['Name']:
					playerWriter.writerow({
						'Name':member,
						'Soccer Experience':row['Soccer Experience'],
						'Guardian Name(s)':row['Guardian Name(s)']
					})			

open_file()
divide_team()
show_players()
write_file()
