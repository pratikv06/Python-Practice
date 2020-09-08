# - Doesn't require creation of class object
# - Bound to class rather than object
# - method is called by it class name
# - first parameter is class itself, So it know about class
# - Modify class state

class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # Called decorator
    def total_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

print(Person.number_of_people)
p1 = Person("Noddy")
print(Person.total_people())

p2 = Person("Oswald")
print(Person.total_people())

