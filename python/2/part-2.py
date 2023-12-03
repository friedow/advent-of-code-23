import regex as re


def stripred(numberandred):
    return int(numberandred.rstrip(" red"))


def stripblue(numberandblue):
    return int(numberandblue.rstrip(" blue"))


def stripgreen(numberandgreen):
    return int(numberandgreen.rstrip(" green"))


result = 0
with open("input.txt") as file:
    for gameID, game in enumerate(file):
        reds = re.findall(r"\d+ red", game)
        rednumbers = list(map(stripred, reds))
        rednumbers.sort(reverse=True)
        redmultiplier = rednumbers[0]

        blues = re.findall(r"\d+ blue", game)
        bluenumbers = list(map(stripblue, blues))
        bluenumbers.sort(reverse=True)
        bluemultiplier = bluenumbers[0]

        greens = re.findall(r"\d+ green", game)
        greennumbers = list(map(stripgreen, greens))
        greennumbers.sort(reverse=True)
        greenmultiplier = greennumbers[0]

        result = result + (redmultiplier * bluemultiplier * greenmultiplier)

print(result)
