schematic = [];
with open("9.txt", "r") as file:
    for line in file:
        schematic.append(list(line))

def getPoint(x,y):
    return schematic[x][y];

def options(point):
    x,y = point
    
    
        
currPos = (0,6)

