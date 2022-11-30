class Animal:
    def __init__(self, name, age, food):
        self.name=name
        self.age=age
        self.food=food

    def make_sound(self):
        pass

    def eat_food(self, quantity):
        pass


class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print('Meow!')

    def eat_food(self, quantity):
        if quantity==0:
            for i in range(4):
                print(self.make_sound())
            return quantity

        elif quantity>10:
            pass






class Dog(Animal):
    pass


class Duck(Animal):
    pass


class Horse(Animal):
    pass