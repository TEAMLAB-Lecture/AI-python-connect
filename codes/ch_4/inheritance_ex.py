class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Korean(Person):
    pass

first_korean = Korean("Sungchul", 35)
print(first_korean.name)
