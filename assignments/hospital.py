class patient(object):
    def __init__(self, idn, name, allergies):
        self.idn = idn
        self.name = name
        self.allergies = allergies #what exactly is being stated after the equals sign
        self.bedno = "none"
    def displayinfo(self):
        print str(self.idn), str(self.name), str(self.allergies), (self.bedno)
        return self





class hospitals(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity 
    def displayinfo(self):
        print str(self.patients), str(self.name), str(self.capacity)
        return self
    def admit(self):
        self.patients += 
        return self





#     def ride(self):
#         print "riding...."
#         self.miles = self.miles + 10
#         return self
#     def reverse(self):
#         print "reversing..."
#         self.miles = self.miles - 5
#         if self.miles < 0:
#             self.miles = 0
#         return self



# bike1 = bike(1500, "140mph", 0)

# bike1.ride().ride().reverse().reverse().reverse().reverse().reverse().displayinfo()

patient1 = patient(1, "lucy", "none")

patient1.displayinfo()