from string import ascii_letters
with open('Day3.in') as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0

for rucksack in data:
    half = len(rucksack)//2

    first = set(rucksack[:half])
    second = set(rucksack[half:])

    for priority, char in enumerate(ascii_letters):
        if char in first and char in second:
            total += priority + 1

print(total)