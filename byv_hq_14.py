from random import randint
# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить 
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте 
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 

class Car:
    def __init__(self, name_model,  year_release, company, motor_volume, color_car, cost):
        self.name_model = name_model
        self.year_release = year_release
        self.company = company
        self.motor_volume = motor_volume
        self.color_car = color_car
        self.cost = cost

    def car_info(self, color_car,cost):
        print(f"Car info: Car - {self.name_model} Color - {color_car}, Price -  {cost} $")

    def company_volume(self, company,motor_volume):
        print(f'Company & volume: Car {self.name_model} of {company} Motor {motor_volume} ')

car1 = Car("Model 3",2022, "Tesla", "Electric", "Dark Blue", 33333)
car2 = Car("S 150",2021, "Porshe", "6L", "Gold",55555)


print("Car1 motor volume",car1.motor_volume)
print("Car1 cost",car1.cost,'$')
print("Car2 motor volume",car2.motor_volume)
print("Car2 cost",car2.cost,'$')

car1.car_info("Green", 99999)
car2.company_volume("Reno", "1.8L" )

car2.cost = 44444
car1.color_car= 'Red'

print("Car1 new color", car1.color_car)
print("Car2 new cost", car2.cost, "$")
# print("car2 company&volume" )
# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, 
# издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса.
class Book:
    def __init__(self, name_book,  year_releas_book, company_publisher, genre, author, cost_book):
        self.name_book = name_book
        self.year_releas_book = year_releas_book
        self.company_publisher = company_publisher
        self.genre=genre
        self.author= author
        self.cost_book = cost_book
def genre_author(self, genre, author):
    print(f"Book info: Book - {self.name_book} , Author - {author}, Genre -  {genre} ")

def company_year_releas(self, company_publisher,year_releas_book):
    print(f'Company & Year: Book {self.name_book} of {company_publisher} Year {year_releas_book} ')

book1 = Book("Python 3",2002, "Programming", "Electric Book", "Dark Hacker", 33.33)
book2 = Book("HTML 5",2020, "WEB Disign", "Soliter PH", "Naum Gold",5.55)


print("Car1 motor volume",car1.motor_volume)
print("Book1 cost",car1.cost,'$')
print("Car2 motor volume",car2.motor_volume)
print("Book2 cost",book2.cost,'$')

car1.car_info("Green", 99999)
car2.company_volume("Reno", "1.8L" )

car1.cost = 44444
car1.color_car= 'Red'

print("Car1 new color", car1.color_car)
print("Car1 new cost", car1.cost, "$")
# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату
#  открытия, страну,город, вместимость. Реализуйте методы класса для ввода 
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса

class Stadium:
    def __init__(self, name_stadium,  year_opening, country, city, capacity):
        self.name_stadium = name_stadium
        self.year_opening = year_opening
        self.country = country
        self.city=city
        self.capacity= capacity

def car_info(self, color_car,cost):
        print(f"Car info: Car - {self.name_model} Color - {color_car}, Price -  {cost} $")

    def company_volume(self, company,motor_volume):
        print(f'Company & volume: Car {self.name_model} of {company} Motor {motor_volume} ')

car1 = Car("Model 3",2022, "Tesla", "Electric", "Dark Blue", 33333)
car2 = Car("S 150",2021, "Porshe", "6L", "Gold",55555)


print("Car1 motor volume",car1.motor_volume)
print("Car1 cost",car1.cost,'$')
print("Car2 motor volume",car2.motor_volume)
print("Car2 cost",car2.cost,'$')

car1.car_info("Green", 99999)
car2.company_volume("Reno", "1.8L" )

car1.cost = 44444
car1.color_car= 'Red'

print("Car1 new color", car1.color_car)
print("Car1 new cost", car1.cost, "$")
