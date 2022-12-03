#getting data
with open("day1.in") as file:
    data = {i for i in file.read().strip().split("/n")}

max_cals = 0
elf_cals = 0
for item in data:
    if item == '':
        elf_cals = 0

    else:
        num = int(item)
        elf_cals += num

    if elf_cals > max_cals:
        max_cals = elf_cals

print("'Day 1's answer is'", max_cals)
