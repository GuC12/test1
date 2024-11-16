class Cat:
    name = "cat"
    def __init__(self, name, age, lifes):
        self.name = name
        self.age = age
        self.lifes = lifes
    def infor(self):
        print("Имя", self.name, "Возраст", self.age, "Года,", "Жизни", self.lifes)
    def sound(self):
cat = Cat("kot,", 2, 6)
print(cat.infor())