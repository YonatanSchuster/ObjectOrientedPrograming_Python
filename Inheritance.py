class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Im a {self.name} and Im {self.age} years old")

    def speak(self):
        print("I dont know what i say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,
                         age)  # super() that is the class that we inherited from. and then the method we want to call
        self.color = color

    def speak(self):
        print("MEOW")

    def show(self):
        print(f"Im a {self.name} and Im {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("BARK!")


class Fish(Pet):
    pass


p = Pet("tim", 19)
p.show()
p.speak()

c = Cat("Bill", 22, "black")
c.show()
c.speak()

d = Dog("Gill", 9)
d.show()
d.speak()

f = Fish("Bubbles", 10)
f.show()
f.speak()
