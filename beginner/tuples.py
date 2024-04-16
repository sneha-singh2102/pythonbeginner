marks={
    'maths': 85,
    'social science': 90,
    'chemistry': 78,
    'physics': 90,
    'english':98,
    'biology': 76,
    'history': 87,
    'geography': 82,
}

def add_subject(subject, score):
    marks[subject]= score

def remove_subject(subject):
    del marks[subject]

def show_subject(subject):
    print(marks[subject])

print("add subject english literature with 88 marks")
add_subject("english literature", "88")
print(marks)
print("remove subject english literature with 88 marks")
remove_subject("english literature")
print(marks)
print("Show marks in english")
show_subject("english")
print(marks)