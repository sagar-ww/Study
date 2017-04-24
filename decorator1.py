"""first import."""
from functools import wraps


"""Sec Function."""
def first_decorator_function(my_function):
    """under first decorator."""

    @wraps(my_function)
    def wrapper(*args, **kwargs):
        print('i am in first decorator function')
        print('{} '.format(my_function.__name__))
        print('parameter first deco: {} {}'.format(args, kwargs))
        return my_function(*args, **kwargs)

    return wrapper
""" sec function """
def sec_decorator_function(my_function):
    @wraps(my_function)
    def wrapper(*args, **kwargs):
        print('i am in second decorator function')
        print('{} '.format(my_function.__name__))
        print('parameter sec deco: {} {}'.format(args, kwargs))
        return my_function(*args, **kwargs)
    return wrapper


@sec_decorator_function
@first_decorator_function
def employee(fname, lname):
    print('employee name {} {}'.format(fname, lname))

employee('john', 'terry')

