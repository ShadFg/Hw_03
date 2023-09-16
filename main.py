class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def setAnimalInfo(self, newName, newBreed, newAge):
        self.name = newName
        self.breed = newBreed
        self.age = newAge

    def showAnimalInfo(self):
        return f"{self.breed} {self.name} {self.age} years"

class Zoo:
    def __init__(self):
        self.animals = []

    def addAnimal(self, *args):
        for animal in args:
            self.animals.append(animal)

    def removeAnimal(self, *args):
        for animal in args:
            self.animals.remove(animal)

    def showZooAnimals(self):
        if self.animals != []:
            print("\nIn the zoo:")
            for animal in self.animals:
                print(animal.showAnimalInfo())
        else:
            print("No animals in the zoo")

zoo = Zoo()
animal1 = Animal("dog", "shepherd", "4")
animal2 = Animal("cat", "angora", "1")
animal3 = Animal("tiger", "common", "3")
animal4 = Animal("giraffe", "common", "4")
zoo.addAnimal(animal1, animal2, animal3, animal4)
zoo.showZooAnimals()
zoo.removeAnimal(animal2, animal3)
zoo.showZooAnimals()