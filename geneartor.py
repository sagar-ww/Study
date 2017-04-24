def fibo(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

for i in fibo(10):
    print(i)
