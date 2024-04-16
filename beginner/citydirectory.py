# check if city input by user is present in directory or not
karnataka=["Bangalore", "Hosur", "Hampi", "Mysore"]
tamilnadu=["Chennai", "Coimbatore", "Salem", "Nilgiri"]
kerela = ["Munnar", "Thekaddey", "Kochi", "Thiruvananthapuram"]
city1 = input("Enter city name: ")
city2 = input("Enter city name: ")

if city1 in karnataka:print(city1, " found in Karnataka")
elif city1 in tamilnadu: print(city1, " found in Tamil Nadu")
elif city1 in kerela: print(city1, " found in Kerela")
else: print(city1, " not found in dictionary")

if city1 in karnataka and city2 in karnataka: print(city1,", ", city2, " found in Karnataka")
elif city1 in tamilnadu and city2 in tamilnadu: print(city1,", ", city2, " found in Tamil Nadu")
elif city1 in kerela and city2 in kerela: print(city1,", ", city2, " found in Kerela")
else: print(city1,", ", city2, " not found in same state")