from string import ascii_letters
with open('Day3.in') as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0
j = 3
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            total += priority + 1

print(total)