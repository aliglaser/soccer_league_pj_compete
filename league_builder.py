import csv
import random


#to put the result of the list of csv.DictReader(csvfile)
rows = []

#experienced/unexperienced students' lists
experienced = []
unexperienced = []

#lists of three teams
Sharks = []
Dragons = []
Raptors = []


#open soccer_players.csv file
#create the lists of experinced/unexperienced students
def open_file():
	with open('soccer_players.csv', newline="") as csvfile:
		playerDict = csv.DictReader(csvfile, delimiter=",")
		playerDictList = list(playerDict)
		rows.extend(playerDictList)
		for player in playerDictList:
			if player['Soccer Experience']=="YES":
				experienced.append(player['Name'])
			else:
				unexperienced.append(player['Name'])
				

#enlist the experienced students evenly to each list
#use random.sample() method to pick the students from the experienced list
#after randomly pick the students, remove them from the original(experienced list)
#repeat 2 times and enlist the remaining students to the last team(in this case Raptors)
def divide_ex():
	exlen = int(len(experienced)/3)
	exrandom = random.sample(experienced, exlen)
	Sharks.extend(exrandom)
	for player in exrandom:
		experienced.remove(player)
	exrandom = random.sample(experienced, exlen)
	Dragons.extend(exrandom)	
	for player in exrandom:
		experienced.remove(player)
	Raptors.extend(experienced)



#enlist the unexperienced students evenly to each list
#use random.sample() method to pick the students from the unexperienced list
#after randomly pick the students, remove them from the original(unexperienced list)
#repeat 2 times and enlist the remaining students to the last team(in this case Raptors)
def divide_unex():
	unex = int(len(unexperienced)/3)
	unexrandom = random.sample(unexperienced, unex)
	Sharks.extend(unexrandom)
	for player in unexrandom:
		unexperienced.remove(player)
	unexrandom = random.sample(unexperienced, unex)
	Dragons.extend(unexrandom)	
	for player in unexrandom:
		unexperienced.remove(player)
	Raptors.extend(unexperienced)	



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


if __name__ == '__main__':
	open_file()
	divide_ex()
	divide_unex()
	write_file()
