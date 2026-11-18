followers = []

with open("input.txt", "r") as file:
    count = 0
    lim = 0
    for line in file:
        line = line.strip()
        if count == 0:
            lim = int(line)
            count += 1
            continue
        if count > lim:
            break
        followers.append(line.split())
        
print(followers);

count = 0;

while True:
    longest = followers[0];
    for fol in followers:
        if len(fol) > len(longest):
            longest = fol;
    
    if len(longest) == 1:
        break
    
    followers.remove(longest);
    
    for fol in followers:
        for id in longest:
            if id in fol:
                idx = fol.index(id);
                if idx > 0:
                    fol.pop(idx)
    
    count += 1;
    
print (count);