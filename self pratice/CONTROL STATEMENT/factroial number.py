n=int(input("ENTER A NUMBER:-"))
if(n<=0):
    print("invalid input",n)
else:
    num=n
    i=1
    while(n>0):
        i=i*n
        n=n-1
    else:
        print("factorial of {}={}".format(num,i))







