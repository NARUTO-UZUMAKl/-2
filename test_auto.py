class Auto:
    def __init__(self, make, model, year, mileage, price, origin_ru):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.origin_ru = origin_ru

    def makeModel(self):
        return f"{self.make} {self.model}"
    
    def getAttrValue(self, attr):
        return getattr(self, attr)

    def __repr__(self):
        return (f"{self.make} {self.model} - Price: RUR{self.price}, "
                f"Production Year: {self.year}, Mileage: {self.mileage}")


# Создаем объекты
KiaSor = Auto("Kia", "Sorrento", 2003, 223000, 415000, "Россия")
HyunSol = Auto("Hyundai", "Solaris", 2015, 41000, 869000, "Корея")
VolkPas = Auto("Volkswagen", "Passat", 2012, 127000, 900000, "Германия")
LadaPri = Auto("Lada", "Priora", 2011, 139000, 150000, "Россия")
UazPat = Auto("UAZ", "Patriot", 2011, 150000, 345400, "Россия")

# Создаем список названий автомобилей
listOfCarNames = [car.makeModel() for car in [KiaSor, HyunSol, VolkPas, LadaPri, UazPat]]

# Функция для сортировки по пробегу
def sort_by_mileage(cars):
    return sorted([(car.makeModel(), car.mileage) for car in cars], key=lambda x: x[1])

sortedByMileage = sort_by_mileage([KiaSor, HyunSol, VolkPas, LadaPri, UazPat])

# Вывод результатов для проверки

# Список названий автомобилей
print("List of Car Names:")
for name in listOfCarNames:
    print(name)

# Сортировка по пробегу
print("\nSorted by Mileage:")
for car in sortedByMileage:
    print(f"{car[0]}: {car[1]} km")

# Вывод всех свойств объектов для проверки __repr__
print("\nCar details:")
print(KiaSor)
print(HyunSol)
print(VolkPas)
print(LadaPri)
print(UazPat)