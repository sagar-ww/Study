"""Create Employee class."""


class Employee:

    payment_increment = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = '{}{}'.format(fname, lname) + '@company.com'
        self.pay = pay

    def paymet(self):
        self.pay = self.pay * self.payment_increment


    @classmethod
    def set_raise_amt(cls, amount):
        cls.payment_increment = amount

    @staticmethod
    def is_weekday():
        if day.weekday() == 5 or day.weekday == 6:
            retrun True
        else:
            return False
            



emp1 = Employee('sagar', 'gosavi', 25000)
print(emp1.payment_increment)
emp1.set_raise_amt(2.5)
print(emp1.payment_increment)
emp1.paymet()
print(emp1.pay)
print(emp1.email)
