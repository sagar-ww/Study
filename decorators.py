from functools import wraps
import time

def decorator_fun(my_func):
    def wrapper_fun(*args, **kwargs):
        print('I am before the function {}'.format(my_func.__name__))
        return my_func(*args, **kwargs)
    return wrapper_fun


class decorator_class(object):
    def __init__(self, myfunc):
        self.myfunc = myfunc

    def __call__(self, *args, **kwargs):
        print('I am before the function {}'.format(self.myfunc.__name__))
        return self.myfunc(*args, **kwargs)


@decorator_class
def new_function():
    print('i am in new functon')


@decorator_class
def new_function_info(fname, lname):
    print('my name is {} {}'.format(fname, lname))



new_function()
new_function_info('john', 'terry')




def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)