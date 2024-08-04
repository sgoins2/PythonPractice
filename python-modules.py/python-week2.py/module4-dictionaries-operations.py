
grades = {}

grades['john'] = 'A-'
grades['lisa'] = 'B'

print(grades)


#############################

grades['lisa'] = 'A'

print(grades)


#############################


grades.update({'john': 'A'})

print(grades)




#############################

print(len(grades))





#############################

if 'john' in grades:
    print('John got a(n):', grades['john'] )




#############################

del grades['john']
print(grades)




#############################

grades = {}

grades['john'] = 'A-'
grades['lisa'] = 'B'

for students in grades:
    print(students)




#############################

for students in grades.keys():
    print(students)






#############################

for students in grades.values():
    print(students)







#############################

for person, grade in grades.items():
    print(person, 'got a(n)', grade)





#############################