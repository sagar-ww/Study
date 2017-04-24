def loged(msg):
    def loging_msg():
        print "log msg is {}".format(msg)
    return loging_msg

a = loged("HI")
a()




def Html_tag(tag):
    def html_msg(msg):
        print '<{0}>{1}</{0}>'.format(tag,msg)
    return html_msg

m = Html_tag('p')
m('This is paragraph msg')
b = Html_tag('b')
b('This is owesome')

