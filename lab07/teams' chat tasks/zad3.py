import random


class InvalidParameterError(Exception):
    def __init__(self, name):
        super().__init__(name)
        self.name = str(name)
        print(f'Invalid class parameter: {self.name}')


class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super().__init__(age)
        self.age = int(age)
        print(f'Invalid parameter: age')


class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        super().__init__(sound)
        self.sound = str(sound)
        print(f'Invalid parameter: sound')


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = str(name)
        self.age = int(age)
        self.sound = str(sound)

        try:
            if type(name) != str:
                raise InvalidParameterError(name)

            if type(age) != int:
                raise InvalidAgeError(age)

            if type(sound) != str:
                raise InvalidSoundError(sound)
        except InvalidAgeError as ex:
            print(ex)
        except InvalidSoundError as ex:
            print(ex)

    def make_sound(self):
        print(f'{self.name} says {self.sound}')

    def print(self):
        pass

    def daily_task(self, *args):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)

        try:
            if age > 15:
                raise InvalidAgeError(age)
            if sound.count('r') < 2:
                raise InvalidSoundError(sound)
        except InvalidAgeError as ex:
            print(ex)
        except InvalidSoundError as ex:
            print(ex)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for x in animals:
            if x == 'Lemur' or x == 'Human':
                animals.remove(x)
                print(f'{self.name} the Jaguar hunted down {x.name} the {x.__class__.__name__}')


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)

        try:
            if age>10:
                raise InvalidAgeError(age)
            if 'e' not in sound:
                raise InvalidSoundError(sound)
        except InvalidAgeError as ex:
            print(ex)
        except InvalidSoundError as ex:
            print(ex)

    def print(self):
        print(f'Lemur({self.name}, {self.age}, {self.sound})')

    def daily_task(self, fruit_count):

        if type(fruit_count) != int:
            print('Invalid parameter input.')

        if fruit_count >= 10:
            fruit_count -= 10
            print(f'{self.name} the Lemur ate a full meal of 10 fruits and now has {fruit_count} left.')
        elif 0 < fruit_count < 10:
            print(f'{self.name} the Lemur could only find {fruit_count} fruits and now has 0 left.')
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat.")
            fruit_count = 0
            return fruit_count


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)

        try:
            if age > 10:
                raise InvalidAgeError(age)
            if 'e' not in sound:
                raise InvalidSoundError(sound)
        except InvalidAgeError as ex:
            print(ex)
        except InvalidSoundError as ex:
            print(ex)

    def print(self):
        print(f'Human({self.name}, {self.age}, {self.sound})')

    def daily_task(self, animals, buildings):
        for a in animals:
            if type(a) == Human:
                if animals.index(a) == 0:
                    if type(animals[animals.index(a)+1]) == Human:
                        buildings.append('building')
                elif animals.index(a) == -1:
                    if type(animals[animals.index(a)-1]) == Human:
                        buildings.append('building')
                elif animals.index(a) > 0 and type(animals[animals.index(a)-1]) == Human and type(animals[animals.index(a)+1]) == Human:
                    buildings.append('building')


class Building:
    def __init__(self, btype):
        self.btype = str(btype)


fruit_count = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]


for i in range(102):
    n = random.randint(0, 9)
    name = names[random.randrange(len(names))]
    age = random.randint(7, 20)
    sound = sounds[random.randrange(len(sounds))]
    try:
        if 0 <= n <= 3:
            animals.append(Lemur(name, age, sound))
        elif 4 <= n <= 7:
            animals.append(Jaguar(name, age, sound))
        else:
            animals.append(Human(name, age, sound))
    except InvalidAgeError as ex:
        print(ex)
    except InvalidSoundError as ex:
        print(ex)

print(f"The jungle now has {len(animals)} animals")


for anim in animals:
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Lemur:
        fruits = anim.daily_task(fruit_count)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)