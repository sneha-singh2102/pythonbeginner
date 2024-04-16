#print a pattern of stars by taking the number of rows as input from user
rows = input("Enter number of rows for stars : ")
if(rows.isnumeric() & int(rows)>0):
    for row in range(int(rows)):
        s = ""
        for column in range(row+1):
            s=s+"* "
        print(s)
else:
    print("Enter a number greater than 0")
