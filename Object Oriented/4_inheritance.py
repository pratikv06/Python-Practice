class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} year old.")

    def speak(self):
        print("hahahaha")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!!!")

    def show(self):
        print(f"I am {self.name} and I am {self.age} year old and {self.color} in color.")


class Dog(Pet):
    def speak(self):
        print("Bark!!!")

    
class Fish(Pet):
    pass

p = Pet("Tom", 14)
p.show()
p.speak()
c = Cat("Jerry", 12, "White")
c.show()
c.speak()
d = Dog("Oscar", 10)
d.show()
d.speak()
f = Fish("Tommy", 8)
f.show()
f.speak()