class Dog:

    def __init__(self, name, breed="Дворняга"):
        self.name = name
        self.breed = breed

    def __str__(self) -> str:
        return f"Собаку зовут {self.name}, и ее порода это {self.breed}"

    def fas(self):
        print("Гав Гав")

dog_1 = Dog("Бобик", "коргишпиц")

print(f"{dog_1.name =}, {dog_1.breed = }")
dog_1.fas()
print(dog_1)

dog_2 = Dog("Тузик")
print(dog_2)

import hashlib

print(hash("Vladimir"))

t = 0
for i in range(100000):
    t += i

print(hash("Vladimir"))