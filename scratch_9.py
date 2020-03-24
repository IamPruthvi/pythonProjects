def f(s = "12345678999", n = 3):
    ls = [int(x) for x in str(s)]
    newLs = []
    string = ""
    for j in range(7):
        if max(ls) in ls:
            newLs.append(max(ls))
            ls.remove(max(ls))
    for k in range(n):
        string = string+"".join(str(newLs[k]))
    print(string) 
f() #nochanges
