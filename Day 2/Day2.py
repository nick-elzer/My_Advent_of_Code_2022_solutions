with open("Day2.in") as f:
	lines = f.readlines()

myChoice = {
	88 : 0,
	89 : 0,
	90 : 0
}
Outcomes = {
	'Win' : 0,
	'Draw' : 0,
	'Loss' : 0
}

for line in lines:
	plays = list(map(ord,line.split()))
	myChoice[plays[1]] += 1
	match plays[1] - plays[0] - 23:
		case -1 | 2 : Outcomes['Loss'] += 1
		case 0: Outcomes['Draw'] += 1
		case 1 | -2: Outcomes['Win'] += 1

		
choiceScore = myChoice[88] + myChoice[89] * 2 + myChoice[90] * 3
outcomeScore = Outcomes['Win'] * 6 + Outcomes['Draw'] * 3 
print(choiceScore + outcomeScore)