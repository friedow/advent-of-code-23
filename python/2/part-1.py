import regex as re

def stripred(numberandred):
    return int(numberandred.rstrip(' red')) <= 12

def stripblue(numberandblue):
    return int(numberandblue.rstrip(' blue')) <= 14

def stripgreen(numberandgreen):
    return int(numberandgreen.rstrip(' green')) <= 13
    
result = 0    
with open('input.txt') as file:
    for gameID, game in enumerate(file):
        reds = re.findall(r'\d+ red',game)
        rednumbers = list(map(stripred,reds))
        if all(rednumbers) == False:
            continue
        blues = re.findall(r'\d+ blue',game)
        bluenumbers = list(map(stripblue,blues))
        if all(bluenumbers) == False:
            continue
        greens = re.findall(r'\d+ green',game)
        greennumbers = list(map(stripgreen,greens))
        if all(greennumbers) == False:
            continue
        result = result + gameID + 1

print(result)
        
        
        


        

