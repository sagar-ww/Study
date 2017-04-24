def gen(n):
    for i in n:
        yield (i * i)

a = gen([1, 2, 3, 4])

print next(a)



def my_sqr(n):
    for i in n:
        yield (i*i)

a = (x*x for x in [1,2,3,4,5])
for i in a:
    print i

# making changes for clone

