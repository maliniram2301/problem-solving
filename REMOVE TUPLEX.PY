def Remove(duplicate): 
    l = [] 
    for n in duplicate: 
        if n not in l: 
            l.append(n) 
    return l
duplicate =[12,24,35,24,88,120,155,88,120,155] 
print(Remove(duplicate)) 
