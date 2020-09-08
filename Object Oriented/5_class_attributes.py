# - class attribute is variable within class but outside the methods
# - it can be access by className.variableName
# - it's value will be same for all the objects that is created

class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


print(Person.number_of_people)
p1 = Person("Noddy")
print(p1.number_of_people)

p2 = Person("Oswald")
print(p2.number_of_people)

