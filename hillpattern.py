n=int(input("enter a num"))
for i in range(0,n+1):
    for k in range(n,i,-1):
        print("",end=" ")
    for j in range(0,i):
        print("*",end="")
    print("\r")
