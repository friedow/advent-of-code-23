import regex as re

sum = 0

with open("input.txt") as file:
    for line in file:
        numbers = re.findall(r"\d", line)
        sumstring = int(numbers[0]) + int(numbers[len(numbers) - 1])
        sum += int(sumstring)
print(sum)
