class Vehicle:
    def __init__(self, brand, model, engine_volume, max_speed, mileage, max_passengers):
        self.brand = brand
        self.model = model
        self.vol = float(engine_volume)
        self.speed = float(max_speed)
        self.mileage = float(mileage)
        self.people = int(max_passengers)

    def print_info(self):
        print(f'Vehicle ({self.brand}, {self.model}, {self.vol}, {self.speed}, {self.mileage}, {self.people})')


class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_volume, max_speed, mileage, price, sidecar, max_passengers=2):
        super().__init__(brand, model, engine_volume, max_speed, mileage, max_passengers)
        self.price=float(price)
        self.sidecar=bool(sidecar)

    def print_info(self):
        print(f'Vehicle ({self.brand}, {self.model}, {self.vol}, {self.speed}, {self.mileage}, {self.people}, {self.price}, {self.sidecar})')


class Car(Vehicle):
    def __init__(self, brand, model, engine_volume, max_speed, mileage, category, fuel_type, max_passengers=4):
        super().__init__(brand, model, engine_volume, max_speed, mileage, max_passengers)
        self.category = category
        self.fuel = fuel_type

    def print_info(self):
        print(f'Vehicle ({self.brand}, {self.model}, {self.vol}, {self.speed}, {self.mileage}, {self.people}, {self.fuel}, {self.category})')


class Bus(Vehicle):
    def __init__(self, brand, model, engine_volume, max_speed, mileage, max_passengers, supporting_company, year_of_manufacture):
        super().__init__(brand, model, engine_volume, max_speed, mileage, max_passengers)
        self.company = supporting_company
        self.year = year_of_manufacture

    def print_info(self):
        print(f'Vehicle ({self.brand}, {self.model}, {self.vol}, {self.speed}, {self.mileage}, {self.people}, {self.company}, {self.year})')


cls250=Car('Mercedes-Benz', 'CLS 250', 2.1, 236, 172798, 'euro5', 'diesel')
e500=Car('Mercedes-Benz', 'E 63 AMG', 5.5, 250, 150000, 'euro5', 'petrol')
outlander=Car('Mitsubushi', 'Outlander', 2.5, 200, 137000, 'euro6', 'diesel')
moskvich=Car('Moskvich', '1500', 1.0, 60, 65000, 'coupe', 'petrol')
yzf=Motorbike('Yamaha', 'YZF-R6', 0.6, 170, 41000, 11700, False)
ducati=Motorbike('Ducati', 'Multistrada', 1.2, 200, 65000, 14000, False)
shadow=Motorbike('Honda', 'Shadow VT750', 0.7, 180, 39000, 10500, True)
lion=Bus('Man', 'Lion S Classic', 12.4, 250, 900000, 58, 'Pamporovo Bus', 2009)
omnibus=Bus('Man', 'Omnibus M3', 8, 200, 344000, 25, 'Pamporovo Bus', 2005)
vclass=Bus('Mercedes-Benz', 'V 250 Lang', 3.5, 250, 126500, 7, 'Emiliya', 2017)

cls250.print_info()
e500.print_info()
outlander.print_info()
moskvich.print_info()
yzf.print_info()
ducati.print_info()
shadow.print_info()
lion.print_info()
omnibus.print_info()
vclass.print_info()





