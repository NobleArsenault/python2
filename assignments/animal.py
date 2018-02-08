class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayhealth(self):
        print self.health
        return self

class dragon(animal):
    def set_health(self):
        self.health = 170
        return self

    def fly(self):
        self.health -= 10
        return self

    def displayhealth()

animal1 = animal("Cockroach", 100)
animal1.walk().run().displayhealth()

# def __init__(self):
#         super(Wizard, self).__init__()  
#         self.intelligence = 10 