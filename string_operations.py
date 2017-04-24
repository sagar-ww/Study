import datetime


person = {'fname':'sagar','lname':'Gosavi'}

print('my full name using dictionary {fname} {lname}'.format(**person))


class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

fullname = Person('sagar','gosavi')
print('my full name using class {0.fname} {0.lname}'.format(fullname))


sentence = '1 MB is equal to {} bytes'.format(1000**2)
print(sentence)

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence)


pi = 3.149739862
print('{:.2f}'.format(pi))

amount = 1000000000000
print('{:,.2f}'.format(amount))