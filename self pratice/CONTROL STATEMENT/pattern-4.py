r = int(input("Enter number of rows: "))
for i in range(r, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\n")