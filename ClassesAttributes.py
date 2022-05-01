class Person:
    number_of_persons = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_persons

    @classmethod
    def add_person(cls):
        cls.number_of_persons +=1


p1 = Person("Tim")
p2 = Person("jill")


