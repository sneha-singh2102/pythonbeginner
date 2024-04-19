class School:
    def __init__(self, name, affiliated_board, highest_class, teaching_medium, established_year):
        self.name = name
        self.affiliated_board = affiliated_board
        self.teaching_medium = teaching_medium
        self.established_year = established_year
        self.highest_class = highest_class
        self.teaching_medium = teaching_medium
        self.established_year = established_year

    def display_school(self):
        print(
            f"Name: {self.name}\n Affiliated Board: {self.affiliated_board}\n Highest Class: {self.highest_class}\n Teaching Medium: {self.teaching_medium}\n Established Year: {self.established_year}")

