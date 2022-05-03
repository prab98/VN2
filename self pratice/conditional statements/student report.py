p=float(input("Enter student's Marks:"))
if(p < 0 and p>100):
    print("invalid input".format(p))
elif(p<25):
    print("{} is D grade".format(p))
elif(p>=25 and p < 45):
    print("{} is C grade".format(p))
elif(p>=45 and p<50):
    print("{} is B grade".format(p))
elif(p>=50 and p<60):
    print("{} is B+ grade".format(p))
elif(p>=60 and p <= 80):
    print("{} is A grade".format(p))
else:
    print("{} is A+ grade".format(p))
print("THANK YOU")

