import regex as re


def wordtonumber(word):
    if word == "one":
        return "1"
    if word == "two":
        return "2"
    if word == "three":
        return "3"
    if word == "four":
        return "4"
    if word == "five":
        return "5"
    if word == "six":
        return "6"
    if word == "seven":
        return "7"
    if word == "eight":
        return "8"
    if word == "nine":
        return "9"
    return word


sum = 0

with open("input-1.txt") as file:
    for line in file:
        numbers = re.findall(
            r"one|two|three|four|five|six|seven|eight|nine|\d", line, overlapped=True
        )
        sumstring = wordtonumber(numbers[0]) + wordtonumber(numbers[len(numbers) - 1])
        sum += int(sumstring)
print(sum)
