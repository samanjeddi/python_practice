import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print('took {} second'.format(end))
    return wrapper

@timer
def counter():
    total = 0
    for i in range(0,10000000):
        total += 1
    return total

counter()