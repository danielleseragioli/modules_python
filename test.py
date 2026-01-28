# classe
# 1 encapsulamento (proteger/privar permitir apenas por meios controlados (gets e setters)) - 2 abstracao
# 3 polimorfismo - usando 4 herança (is a)
# 5 composicao (has a)

class Animal:

    def __init__ (self, name: str, age: int):
        self.name = name
        self.age = age
    def make_noise(self):
        print ("animal sound")
    def walk(self):
        print ("animal walking")


animal_1 = Animal("Garfield", 4)
print(f"nome: {animal_1.name}, idade: {animal_1.age}")
animal_1.make_noise()


class Gato: Animal



