schematic = [];
with open("9.txt", "r") as file:
    for line in file:
        schematic.append(list(line))

def getPoint(x,y):
    return schematic[y][x];

def options(point):
    x,y = point
    
    out = []
    
    if getPoint(x,y) == "-" and getPoint(x+1, y) != "-":
        if getPoint(x,y+1) != " ":
            out.append(("d",1))
        elif getPoint(x,y+2)  == " ":
            out.append(("d",2))
        return out

    if getPoint(x,y) == "-" or getPoint(x,y) == "+":
        i = 1
        while(getPoint(x+i, y) == "-"):
            i+=1
        if (getPoint(x+i,y) == "+" or getPoint(x+i,y) == "#"):
            out.append(("f",i))
        else:
            out.append(("f",i-1))
    if getPoint(x,y) == "|" or getPoint(x,y) == "+":
        i = 1
        while(getPoint(x, y+i) == "|"):
            i+=1
        if (getPoint(x,y+i) == "+" or getPoint(x,y+i) == "#"):
            out.append(("d",i))
        elif getPoint(x,y+i) != "=":
            out.append(("d",i-1))
        i = 1
        while(getPoint(x, y-i) == "|"):
            i+=1
        if (getPoint(x,y-i) == "+"):
            out.append(("u",i))
        else:
            out.append(("u",i-1))
    return out

def printDot(pos):
    schematic[pos[1]][pos[0]] = "."


currPos = (0,len(schematic)-7)

print (getPoint(currPos[0], currPos[1]))

movements = []

movements.append(options(currPos))

while True:
    if len(movements[-1]) <= 0:
        movements.pop()
        l_dir, c = movements[-1][0]
        x,y = currPos
        if l_dir == "d":
            y -= c
        elif l_dir == "u":
            y += c
        else:
            x -= c
        movements[-1].pop(0);
        currPos =(x,y)
        continue
    l_dir, c = movements[-1][0]
    x,y = currPos
    if l_dir == "d":
        y += c
    elif l_dir == "u":
        y -= c
    else:
        x += c

    if getPoint(currPos[0],currPos[1]) == "#":
        break;
    movements.append(options(currPos))
    print("HI")

currPos = (0,len(schematic)-7)

for mov in movements:
    a = 0
    b = 0
    
    dir, len = mov[0]

    if dir == "u":
        a = -1
    elif dir == "d":
        a = 1
    else:
        b = 1
    for i in range(mov[0][1]):
       printDot(currPos)
       x,y = currPos
       x += b
       y += a
       currPos = (x,y)

for part in schematic:
    print("".join(part))
