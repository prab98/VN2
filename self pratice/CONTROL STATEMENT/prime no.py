n=int(input("Enter a number:- "))
for i in range(2,n):
    if(n%i)==0:
        print("its not a prime number",n)
        break
else:
    print("it's  a prime number")








