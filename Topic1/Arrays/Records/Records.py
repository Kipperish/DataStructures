class Record():
    def __init__ (self, theID, theLastName, theFirstName, theDept):
        self.id = theID
        self.lastName = theLastName
        self.firstName = theFirstName
        self.dept = theDept

record1 = Record(2468, "Jones", "John", 243)
record2 = Record(3579, "Smith", "Sam", 634)
record3 = Record(1428, "Zimmer", "Zoe", 243)

print(record1.id)

people = [Record(2468, "Jones", "John", 243), Record(3579, "Smith", "Sam", 634), Record(1428, "Zimmer", "Zoe", 243)]