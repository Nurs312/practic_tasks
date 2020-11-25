class Transport:
    attr1 = 'motor'
    attr2 = 'saloon'
    attr3 = 'steering weel'

    def move(self):
        print('All kind of transport moves.')


class Airplane(Transport):
    def fly(self):
        print('Airplane flies.\n')


class Car(Transport):
    def drive(self):
        print('Car rides.\n')


class Ship(Transport):
    def sail(self):
        print('Ship sails.\n')


airplane = Airplane()
airplane.move()
airplane.fly()

car = Car()
car.move()
car.drive()

ship = Ship()
ship.move()
ship.sail()
