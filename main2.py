class Cat:
    name = "cat"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def infor(self):
        print("Имя", self.name, "Возраст", self.age)
cat = Cat("kot", 2)
print(cat.infor())