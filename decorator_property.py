class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    @property
    def email(self):
        return '{}.{}@company.com'.format(self.fname, self.lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)


emp = Employee('sagar', 'gosavi')
print(emp.fullname)
emp.fname = 'test'
print(emp.fullname)
print(emp.email)
print(emp.fname)
print(emp.lname)