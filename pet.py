class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health 
        self.energy = energy
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def sound (self):
        print(self.noise)


class Cat (Pet):
    def __init__(self, name, type, is_outdoor, tricks, health, energy, noise):
        super().__init__(name, type, tricks, health, energy, noise)
        self.is_outdoor = is_outdoor

class Dog (Pet):
    def __init__(self, name, type, tricks, health, energy, noise, is_good_boy):
        super().__init__(name, type, tricks, health, energy, noise)
        self.is_good_boy = is_good_boy


momo = Pet('Momo', 'kitty', 'butt-scratches', 80, 65, 'MEEOOWWWPURRRR')
