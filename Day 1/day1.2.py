
with open("day1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

max_cals = 0
top_2 = 0
top_3 = 0
elf_cals = 0
for item in data:
    if item == '':
        elf_cals = 0

    else:
        num = int(item)
        elf_cals += num

    if elf_cals > top_3:

        if elf_cals > top_2:

            if elf_cals > max_cals:
                top_3 = top_2
                top_2 = max_cals
                max_cals = elf_cals
            
            else:
                top_3 = top_2
                top_2 = elf_cals
        else:
            top_3 = elf_cals
    
# print("'Day 1 Part 2's answer is'", max_cals, top_2, top_3)
print(f"Day 1 Part 2's answer is {max_cals}, {top_2}, {top_3}, 'total: {max_cals + top_2 + top_3}")
