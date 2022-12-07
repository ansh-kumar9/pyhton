L=[int(x) for x in(input("Enter the number(s): ")).split()]
for n in L:
    c=0
    a=1
    b=1
    if n==0 or n==1:
        print(n, "Valid")
    else:
        while c<n:
            c=a+b
            b=a
            a=c
        if c==n:
            print(n, "Valid")
        else:
            print(n, "Invalid")