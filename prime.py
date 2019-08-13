n=int(input("enter n"))
for i in range(2,n):
    if n%i==0:
        print("not a prime no")
        break
else:
    print("prime no")
