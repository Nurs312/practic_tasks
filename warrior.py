import random


class Warrior:
    health = 100

    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f'{self.name} attacked!')

    def get_damage(self):
        print(f'{self.name} got damage!')
        self.health -= random.randint(10, 20)

    def __super_power(self):
        self.health = self.health + 10
        return self.health


warrior1 = Warrior('Hector')
warrior2 = Warrior('Achilles')
warriors = [warrior1.name, warrior2.name]
fight = True
while fight:
    x = random.choice(warriors)
    for warrior in warriors:
        if warrior == x:
            if x == 'Hector':
                x = warrior1
                warrior1.attack()
                print(f"Now {warrior1.name}'s health is {warrior1.health} HP!\n\n")
                warrior2.get_damage()
                print(f"After attack {warrior2.name}'s health is {warrior2.health} HP!\n\n\n")
            else:
                x = warrior2
                warrior2.attack()
                print(f"Now {warrior2.name}'s health {warrior2.health} HP!\n\n")
                warrior1.get_damage()
                print(f"After attack {warrior1.name}'s health is {warrior1.health} HP!\n\n\n")
    if 40 >= warrior1.health >= 20:
        warrior1._Warrior__super_power()
        # warrior1.super_power()
        print(f"""\t\t{warrior1.name} used Super Power! 
        Now {warrior1.name}'s health is {warrior1.health} HP!\n""")
    if 40 >= warrior2.health >= 20:
        warrior2._Warrior__super_power()
        # warrior2.super_power()
        print(f"""\t\t{warrior2.name} used Super Power! 
        Now {warrior2.name}'s health is {warrior2.health} HP!\n""")
    if warrior1.health <= 0 or warrior2.health <= 0:
        fight = False

