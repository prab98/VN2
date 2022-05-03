n=int(input("enter a number:-"))
if(n<=0):
    print("Invalid input".format(n))
else:
    print("multiplication table for:".format(n))
    i=1
    while(i<=10):
        print("\t{}*{}={}".format(n,i,n*i))
        i=i+1