import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('running {} with arg {}'.format(func.__name__,args))
        print(func(*args))

    return log_func

def add(x,y):
    return x + y

def sub(x,y):
    return x - y


add_log = logger(add)
sub_log = logger(sub)

add_log(4,5)
sub_log(4,5)