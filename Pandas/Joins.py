import pandas as pd

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
students = pd.DataFrame({'id': [1, 2], 'names': ['erick', 'juma']})
newStudents = pd.DataFrame({'student_id': [4, 5], 'course': ['BMC', 'IT']})
oldStudents = pd.DataFrame({'student_id': [2, 3], 'course': ['BMC', 'IT']})

# animals.to_csv('cows_and_goats.csv')

# print(animals.loc[:, ['Cows', 'Goats']])
# print(animals.loc['Year 1':, :])

#Added new columns merged along the rows
print(pd.concat([students, newStudents], axis=1))

#Merged along columns
print(pd.concat([newStudents, oldStudents], axis=1))

#All rows are added incase they are different and replaced with none

print('# Inner Join #')

print(pd.merge(students, oldStudents, left_on ='id', right_on = 'student_id'))

print('\n', '# Left Join #')

print(pd.merge(students, oldStudents, left_on ='id', right_on = 'student_id', how = 'left'))

print('\n', '# Right Join #')

print(pd.merge(students, oldStudents, left_on ='id', right_on = 'student_id', how = 'right'))

print('\n', '# Outer Join #')

print(pd.merge(students, oldStudents, left_on ='id', right_on = 'student_id', how = 'outer'))

print(students.set_index('id').reset_index())