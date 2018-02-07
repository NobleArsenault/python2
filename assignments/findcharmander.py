# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'

# def findchar(list, char):
#     for i in list:
#         if i in list == char:
#             print list

# findchar(word_list, char)

seq = ['hello','world','my','name','is','Anna']
sub = 'o'
newlist = []

for text in seq:
    if sub in text:
        newlist.append(text)

print(newlist)


