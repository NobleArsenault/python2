sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


def checktype(val):
    if type(val) is int:
        if val > 100:
            print "big number"
        else:
            print "small number"

    if type(val) is str:
        if len(str(val)) > 50:
            print "big sentence"
        else:
            print "small sentence"

    if type(val) is list:
        if len(val) >= 10:
            print "big list"
        else:
            print "small list"






checktype(lL)