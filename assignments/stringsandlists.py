# string = "i like to take walks while walking downtown"
# print string.count('walk')

# print string.endswith('town')

# print string.find('walking')

# words = "It's thanksgiving day. It's my birthday too!"

# print words.find('day')

# print words.replace('day', 'month', 1)

# x = [2,54,-2,7,12,98]

# print min(x)
# print max(x)

# y = ["hello",2,54,-2,7,12,98,"world"]
# print y[-len(y)], y[-1]
# new_list = y[-len(y)] + ' ' + y[-1]
# print new_list

# a = [19,2,54,-2,7,12,98,32,10,-3,6]

# print sorted(a)


# for split in a:
#     print split 

# print len(a)
alist = [19,2,54,-2,7,12,98,32,10,-3,6]

def splitthis(alist):
    length = len(alist)
    time = (length / 2)
    print [alist[:time]] + alist[time:]



splitthis(alist)