class Developer:
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self. salary = salary
        self.framework = framework


employee1 = Developer("Drake", 20, 50000, "Visual Studio")

print(employee1.__slots__)

'''
Slots are faster, each instance doesn't have to save itself in its own dictionary.
If you are going to create a lot of instances, you should use slots!
'''