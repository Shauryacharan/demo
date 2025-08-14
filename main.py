 class Bird:
    def stance(self):
        print("The bird is standing.")

class Sparrow(Bird):
    def stance(self):
        print("The sparrow is hopping.")

class Penguin(Bird):
    def stance(self):
        print("The penguin is waddling.")

# Polymorphism in action
birds = [Bird(), Sparrow(), Penguin()]

for b in birds:
    b.stance()
