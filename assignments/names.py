# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }

# for key, data in context.items():
#     print data
#     for value in data:
#         print "Question #", value["id"], ": ", value["content"]
#         print "----"

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]


# for key in students:
#     #print key
#     print students[str(key)]




# #print students[0]['first_name']

# girls = [
#      {'first_name':  'Ashley', 'last_name' : 'Kim'},
#      {'first_name' : 'Mya', 'last_name' : 'Baker'},
#      {'first_name' : 'Emily', 'last_name' : 'Milton'},
#      {'first_name' : 'Cecelia', 'last_name' : 'Tucker'}
# ]

# def dames (mylistwdic):
#     for anywordyouwant in mylistwdic:
#         print anywordyouwant['first_name'] + " " + anywordyouwant['last_name']

# dames (girls)



users = {
 'Students': [
     {'first_name':  'Nick', 'last_name' : 'Russ'},
     {'first_name' : 'Aly', 'last_name' : 'Kandeel'},
     {'first_name' : 'Jake', 'last_name' : 'Aramayo'},
     {'first_name' : 'Tye', 'last_name' : 'Online'}
  ],
 'Instructors': [
     {'first_name' : 'Noble', 'last_name' : 'Arsenault'},
     {'first_name' : 'Chow', 'last_name' : 'From The Hangover'}
  ]
 }

for keys, data in users.iteritems():
    print keys, data





#     def peep(dic):
#     for key,data in dic.iteritems():
#         print key
#         count = 0
#         for value in data:
#             count += 1
#             print str(count) + ' - ' + value['first_name'] + ' ' + value['last_name'] + ' - ' + str(len(value['first_name']) + len(value['last_name']))

# peep(users)