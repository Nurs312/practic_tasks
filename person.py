class Person:
    def __init__(self, name, age, sex, weight, hair, job, meal):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.hair = hair
        self.job = job
        self.meal = meal

    def bday(self):
        self.age += 1
        print(f'{self.name} becomes older to one more year.')

    def eat(self):
        print(f"{self.name}'s weight is {self.weight} kg.")
        print(f'{self.name} eats {self.meal}.')
        self.weight += 0.5
        print(f"Now {self.name}'s weight is {self.weight} kg.")

    def work(self):
        print(f"{self.name}'s {self.job}.\n")


asian = Person('Tadashi', 20, 'male', 73, 'brown', 'engineer', 'sushi')
american = Person('Jennifer', 26, 'female', 53, 'dark', 'artist', 'burger')
asian.eat()
asian.work()
american.eat()
american.work()
