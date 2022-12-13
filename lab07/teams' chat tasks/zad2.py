import random


class InvalidParameterError(Exception):
    def __init__(self, error="Input numbers must be of type ""float""."):
        super().__init__(error)
        self.error=error
        print(error)


class NutrientError(Exception):
    def __init__(self, error="The sum of the nutrients' grams is greater than 100."):
        super().__init__(error)
        self.error = error
        print(error)


class InvalidFoodError(Exception):
    def __init__(self, error="All nutrients are zero."):
        super().__init__(error)
        self.error = error
        print(error)


class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs=float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)

    def print_label(self):
        print(f'{__class__.__name__}: ({self.carbs}, {self.protein}, {self.fats}, {self.salt})')


for i in range(0,120,10):
    i=float(i)
    food=Food(i+random.randrange(10),i+random.randrange(10),i+random.randrange(10),i+random.randrange(10))
    food_list=[food.carbs, food.protein, food.fats, food.salt]

    try:
        if type(i) != float:
            raise InvalidParameterError()

        elif sum(food_list) > 100:
            raise NutrientError()

        elif sum(food_list) == 0:
            raise InvalidFoodError()

        elif i<0:
            raise RuntimeError

        food.print_label()

    except InvalidParameterError as ex:
        print(ex)

    except InvalidFoodError as ex:
        print(ex)

    except NutrientError as ex:
        print(ex)

    except RuntimeError:
        print('There is an error with one or more of the parameters.')



