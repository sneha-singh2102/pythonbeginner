import json

word_stats = {}

file_read = open("D:\\7.Coding\\Git repo\\pythonbeginner\\beginner\\filehandlingread.txt", "r")
for line in file_read:
    words = line.split(' ')
    for word in words:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] = 1

print(word_stats)
file_read.close()

file_out = open("D:\\7.Coding\\Git repo\\pythonbeginner\\beginner\\filehandlingwrite.txt", "w")
file_out.write(json.dumps(word_stats))
file_out.close()