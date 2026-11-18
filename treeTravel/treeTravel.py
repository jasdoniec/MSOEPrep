schematic = [];
with open("9.txt", "r") as file:
    for line in file:
        schematic.append(list(line.strip()))

def getPoint(x,y):
    return schematic[y][x];

def options(point):
    x,y = point
    
    out = []
    
#    if getPoint(x,y) == "-":
#        if getPoint
    
    
        
currPos = (0,len(schematic)-7)

#print (schematic)

print (getPoint(currPos[0], currPos[1]))