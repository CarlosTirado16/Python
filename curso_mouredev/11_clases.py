### Clases ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Carlos", "Tirado")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Carlos", "Tirado", "Charlie")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Saldo insuficiente")


cuenta1 = BankAccount("Carlos", 5000)
print(cuenta1.balance)
cuenta1.deposit(3000)
print(cuenta1.balance)

class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def show_inventory(self):
        for product in self.inventory:
            print(product)

cafeteria = Store()
cafeteria.show_inventory()
cafeteria.add_product("Capuchino")
cafeteria.show_inventory()