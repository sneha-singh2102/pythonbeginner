#array to store temprature for first few days of january
weather_arr = []

file_read = open("D:\\7.Coding\\Git repo\\pythonbeginner\\dsa\\nyc_weather.csv", "r")
for line in file_read:
    tokens = line.split(',')
    try:
        weather_arr.append(int(tokens[1]))
    except:
        print("invalid temperature found at line :", tokens, ", Ignoring the row")
file_read.close()

avg_7days = sum(weather_arr[0:7])/len(weather_arr[0:7])
print("Average temperature in last 7 days:", avg_7days)
print("Maximum temperature in first 10 days of Jan ", max(weather_arr[0:10]))

# store weather of jan in dictionary to retrieve day specific temperature
weather_dict = {}
file_read = open("D:\\7.Coding\\Git repo\\pythonbeginner\\dsa\\nyc_weather.csv", "r")
for line in file_read:
    tokens = line.split(',')
    try:
        weather_dict[tokens[0]] = int(tokens[1])
    except:
        print("invalid temperature found at line :", tokens, ", Ignoring the row")
file_read.close()
print("Temperature on 9th Jan: ", weather_dict["Jan 9"])
print("Temperature on 4th Jan: ", weather_dict["Jan 4"])
