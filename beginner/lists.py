#Expenses list from Jan to April
expense = [2200, 2250, 2600, 2190]
print("in feb I spent", expense[1] - expense[0], "extra from Jan")
print("Expense for first quarter:", expense[0]+expense[1]+expense[2])
print("Did I spend exactly 2000 in any month?", 2000 in expense)
expense.append(2380)
print("expenses till june", expense)
expense[3]= expense[3]-200
print("Expense in April after 200 refund ", expense[3])
expense.insert(2,2000)
print("expenses after inserting 2000", expense)
sortedExpenses = expense
sortedExpenses.sort()
print("sorting list by number", sortedExpenses)
sortedExpenses.sort(reverse=True)
print("sorting reverse list by number", sortedExpenses)
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]
print(programming_languages)
programming_languages.sort()
print("Sort string list: ", programming_languages)
programming_languages.sort(key=len)
print("sort string list by length of word", programming_languages)
programming_languages.sort(key=len, reverse=True)
print("sort string list by length of word in reverse order", programming_languages)