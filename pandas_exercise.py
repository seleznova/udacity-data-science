import pandas as pd

series = pd.Series(['Ivanna', 'Ivanova', 'Udacity', 30, - 1789719578])
print series


series = pd.Series(['Ben', 'Benenko', 359,9001],
                         index = ['Instructor', 'Curriculum Manager',
                                  'Course Number', 'Power Level'])
print series

series = pd.Series(['Dave', 'Cheng-Han', 395, 9001],
                    index = ['Instructor', 'Curriculum Manager',
                             'Course Number', 'Power Level'])
print series['Instructor']
print ""

print series[['Instructor', 'Curriculum Manager', 'Course Number']]

cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                             'Pippy', 'Kitten'])
print cuteness > 3
print ""
print cuteness[cuteness > 3]
