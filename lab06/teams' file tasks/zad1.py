class Person:
    def __init__(self, name, lname, age, nationality):
        self.name=name
        self.lname=lname
        self.age=age
        self.nationality=nationality

    def print(self):
        print(f'My name is {self.name} {self.lname}. I am {self.age} years old and I am {self.nationality}.')


class Student(Person):
    def __init__(self, name,lname, age, nationality, university, yearofstudy):
        super().__init__(name, lname, age, nationality)
        self.university=university
        self.yearofstudy=yearofstudy

    def print(self):
        print(f'My name is {self.name} {self.lname}. I am {self.age} years old and I am {self.nationality}. I study at {self.university} and I am in my year {self.yearofstudy} of study.')


class Lecturer(Person):
    def __init__(self, name, lname, age, nationality, university, experience):
        super().__init__(name, lname, age, nationality)
        self.university=university
        self.experience=experience

    def print(self):
        print(f'My name is {self.name} {self.lname}. I am {self.age} years old and I am {self.nationality}. I have been a lecturer for {self.experience} years and currently I am teaching at {self.university}.')

# Ivan=Person('Ivan', 'Ivanov', 25, 'Bulgarian')
# John=Peron('John', 'Carter', 17, 'American')
# Marija=Person('Marija', 'Risteska', 30, 'Macedonian')


Ivan = Student('Ivan', 'Ivanov', 25, 'Bulgarian', 'Technical University of Sofia', 3)
John = Student('John', 'Carter', 17, 'American', 'UCLA', 1)
Marija = Student('Marija', 'Risteska', 30, 'Macedonian', 'Skopije University', 4)

Gregor = Lecturer('Gregor', 'Vasilevich', 40, 'Russian', 'Moskow University', 10)

Ivan.print()
John.print()
Marija.print()

Gregor.print()
