try:
    f = open('test1.txt')

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print("I am in final block")