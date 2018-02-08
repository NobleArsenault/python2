class product(object):
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def displayinfo(self):
        print self.name
        print "$" + str(self.price)
        print str(self.weight) + "Gs"
        print self.brand
        print self.status
        return self

    def sell(self):
        self.status = "sold"
        print self.status
        return self

    def tax(self):
        self.price = self.price + (self.price * 0.15) 
        print self.price
        return self

    def returnitem(self, reason):
        if reason is "defective":
            self.status = "Defective"
            self.price = 0
        if reason is "like new":
            self.status = "For Sale"
        if reason is "opened":
            self.status = "For Sale"
            self.price = self.price - (self.price * 0.20)

        return self


tomato = product("Gucci'mato",15,15,"Gucci")

tomato.returnitem("opened").displayinfo()