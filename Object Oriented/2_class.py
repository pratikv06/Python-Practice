class Dog():

    def __init__(self, name, age):
        ''' Its like constructor - called when object is created (once)'''
        # self - represent object of that instance
        self.name = name
        self.age = age

    def get_name(self):
        ''' Display dog name'''
        print("Name: " + self.name)

    def get_age(self):
        print("Age: " + str(self.age))

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def bark(self):
        '''user method'''
        print(self.name + " is barking...")

print(">> Creating object")
d = Dog('Tom', 5)
print(type(d))
print(type(d.bark))

print(">> accessing attribute")
print(d.name) #bad practice


# create method to access variable
d.get_name()
d.get_age()

d.set_age(10)
d.get_age()
