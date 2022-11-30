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
        if quantity<0:
            print('invalid input')
        elif quantity==0:
            for i in range(4):
                print(self.make_sound())
            return quantity

        elif quantity<10:
            for i in range(2):
                print(self.make_sound())
            return quantity
        else:
            quantity-=10
            return quantity


class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def eat_food(self, quantity, eat_quantity=5):
        if quantity>eat_quantity:
            return quantity-eat_quantity
        return 0


class Duck(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print('Quack!')

    def eat_food(self, quantity):
        import random
        self.make_sound()
        r_quantity=random.randint(1,9)
        if quantity>r_quantity:
            return quantity-r_quantity
        return 0


class Horse(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def eat_food(self, quantity):
        if 8<quantity<30:
            return quantity-8
        elif quantity<8:
            return 0
        return quantity-15


l_animals=[Cat('Panayot', 3, 'rakiya'), Dog('Reyhan', 6, 'ogreten'), Duck('Paella', 2, 'slanina'), Horse('Boyko', 10, 'furaj'), Duck('Nikolina', 4, 'slanina'), Dog('Boris Dali', 7, 'ogreten'), Cat('Kalina', 5, 'rakiya'), Horse('Azis', 4, 'furaj'), Horse('Mladen', 12, 'furaj'), Duck('Tsvetanka', 3, 'slanina')]
dict_food={'rakiya': 230, 'ogreten': 200, 'furaj': 303, 'slanina': 78}

for i in range(10):
    print('=======')
    for l in l_animals:
        all_food = dict_food[l.food]
        dict_food[l.food] = l.eat_food(all_food)
        print(f"{l.name} the {type(l).__name__} just ate {all_food - dict_food[l.food]} {l.food}. There's {dict_food[l.food]} left")




