with open("Day2.in") as f:
	lines = f.readlines()

mychoicescore = 0
roundscore = 0

for line in lines:
    plays = line.split()
    if plays[1] == 'X':
        mychoicescore += 1
    if plays[1] == 'Y':
        mychoicescore += 2
    if plays[1] == 'Z':
        mychoicescore += 3
    
# draw
    if plays[0] == 'A' and plays[1] == 'X':
        roundscore += 3
    if plays[0] == 'B' and plays[1] == 'Y':
        roundscore += 3
    if plays[0] == 'C' and plays[1] == 'Z':
        roundscore += 3
# win
    if plays[0] == 'A' and plays[1] == 'Y':
        roundscore += 6
    if plays[0] == 'C' and plays[1] == 'X':
        roundscore += 6
    if plays[0] == 'B' and plays[1] == 'Z':
        roundscore += 6
    # print(roundscore)

print(mychoicescore + roundscore)

    