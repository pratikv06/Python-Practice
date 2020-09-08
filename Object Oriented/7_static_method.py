# - method is called by it class name
# - no need to create object for that class
# - cannot access or change state of class
# - biund to class, not object

class Sample:
    @staticmethod # Decorator
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10


print(Sample.add5(10))
print(Sample.add10(10))


'''NOTE:
Being educated under Java background, static method and class method are the same thing.

But not so in Python, there is subtle difference:

Say function a() is defined in Parent Class, while Sub Class extends Parent Class

If function a() has @staticmethod decorator, Sub.a() still refers to definition inside Parent Class. Whereas,

If function a() has @classmethod decorator, Sub.a() will points definition inside Sub Class.

Let’s talk about some definitions here:

@staticmethod function is nothing more than a function defined inside a class. It is callable without instantiating the class first. It’s definition is immutable via inheritance.

@classmethod function also callable without instantiating the class, but its definition follows Sub class, not Parent class, via inheritance. That’s because the first argument for @classmethod function must always be cls (class).
'''