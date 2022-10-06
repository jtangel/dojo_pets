
class Ninja:
    def __init__(self, f_name,l_name,pet,treats,pet_food):
        self.f_name = f_name
        self.l_name = l_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed (self):
        self.pet.eat()
        return self

    def bathe (self):
        self.pet.sound()
        return self

import pet

jack = Ninja('Jack', 'Tangel', pet.momo, ['salmon', 'pineapple', 'donuts'], ['kibble', 'sardines', 'baby mice'])

jack.feed().walk().bathe()


