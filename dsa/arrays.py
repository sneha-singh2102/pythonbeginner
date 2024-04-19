# monthly expenses from Jan to May
expense = [2200, 2350, 2300, 2130, 2190]
print("Extra amount spent in Feb wrt to JAN", expense[1]-expense[0])
print("Total expense in Q1", expense[0]+expense[1] +expense[2])
print("Is there any month when spent exactly 2000", 2000 in expense)
expense.append(1980)
print("updated expense list after adding for the month of June", expense)
expense[3]= expense[3]-200
print("updated expense list after adjusting refund for the month of April", expense)

#heros list
heros=["spider man", "thor", "hulk", "iron man", "captain america"]
print("total heros found", len(heros))
heros.append("black panther")
print("list after adding black panther", heros)
heros.remove("black panther")
heros.insert(2,"black panther")
print("list after inserting black panther before hulk", heros)
heros[1:3]=["doctor strange"]
print("list after removing hulk and thor and adding doctor strange ", heros)
heros.sort()
print("list after alphabetical sorting ", heros)
# print a list of all odd numbers between 1 and n where n is given by the user
n = int(input("Enter max number: "))
oddnum= []
for i in range(1, n):
    if i%2 ==1:
        oddnum.append(i)
print("odd numbers list: ", oddnum)

