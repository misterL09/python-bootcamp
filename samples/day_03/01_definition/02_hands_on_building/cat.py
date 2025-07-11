class Cat:

    meows = 0
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print("Meow")
        Cat.meows += 1

cat_1 = Cat("Garf","Orange", 5)
cat_1.meow()
cat_2 = Cat("Ming","Orange", 3)
cat_2.meow()

print(Cat.meows)
