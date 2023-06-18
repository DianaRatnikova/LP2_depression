



class Person:
    def __init__(self, fname, lname, gender = "Male"):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    def save_gender(self):
       # возможно, запись в csv-файл
       pass