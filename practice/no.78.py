class Animal():
    zoo_name = 'samsal'
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return(f"the {self.name} sound is {self.sound}.")

    def info(self):
        return(f"""this animal name is {self.name},
it's {self.species} animal,
it's {self.age} years old,
it's sound is {self.sound},
and we found it in {self.zoo_name}.""")

    def __str__(self):
         return(f"{self.name}, {self.species}, {self.age}, {self.sound}")

    
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
            return(f"the {self.name} bird sound is {self.sound}.")

    def info(self):
            return(f"""this animal name is {self.name},
it's {self.species} animal,
it's {self.age} years old,
it's sound is {self.sound},
it's wing span is {self.wing_span}
and we found it in {self.zoo_name}.""")

    def __str__(self):
             return(f"{self.name}, {self.species}, {self.age}, {self.sound}, {self.wing_span}")

    
lion = Animal('Lion', 'mammal', 10, 'haaaaaaaaa')

print(lion.make_sound())
print(lion.info())
print(lion)