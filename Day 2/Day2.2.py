with open("Day2.in") as f:
	lines = f.readlines()

mychoicescore = 0
roundscore = 0

for line in lines:
    plays = line.split()
# win/draw score
    if plays[1] == 'Y':
        roundscore += 3
    if plays[1] == 'Z':
        roundscore += 6
# my shape score based on all possible game outcomes
    if  (plays[0] == 'A' and plays[1] == 'X') or (plays[0] == 'B' and plays[1] == 'Z') or (plays[0] == 'C' and plays[1] == 'Y'):
        mychoicescore += 3
    if (plays[0] == 'A' and plays[1] == 'Y') or (plays[0] == 'B' and plays[1] == 'X') or (plays[0] == 'C' and plays[1] == 'Z'):
        mychoicescore += 1
    if (plays[0] == 'B' and plays[1] == 'Y') or (plays[0] == 'C' and plays[1] == 'X') or (plays[0] == 'A' and plays[1] == "Z"):
        mychoicescore += 2
print(roundscore + mychoicescore)