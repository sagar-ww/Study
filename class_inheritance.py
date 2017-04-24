class UserClass():
    init_value = 12

    def __init__(self, user_type, name, lang):
        print "init called for base class"
        self.name = name
        self.lang = 'Python'
        self.user_type = user_type

    def test(self):
        print self.name
        print self.lang
        self.user_type = 'super admin'
        print self.user_type

class DeriveClass(UserClass):
    derived_value = "dummy value"

    def check(self):
        self.test()




base = UserClass('admin', 'adnan', 'python')
base.init_value = 43
print base.init_value
base.test()



print("********")
child = DeriveClass('sagar','gosavi','python')
print(child.check())
print(child.derived_value)