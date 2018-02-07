class bike(object):
    def __init__(self, price, speed, miles):
        self.price = price
        self.speed = speed
        self.miles = miles #what exactly is being stated after the equals sign
    def displayinfo(self):
        print "Bike price $" + str(self.price), "Maximum speed " + str(self.speed), "Miles " + str(self.miles)
        return self
    def ride(self):
        print "riding..."
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "reversing..."
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0
        return self


bike1 = bike(1500, "140mph", 0)

bike1.ride().ride().reverse().reverse().reverse().reverse().reverse().displayinfo()