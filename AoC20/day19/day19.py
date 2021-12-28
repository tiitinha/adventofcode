
def timer(func):
    def wrapper_func(*args, **kwargs):
        start = time.time()
        returnable = func(*args, **kwargs)
        end = time.time()

        print(end - start)

        return returnable
    return wrapper_func

@timer
def pt1():
    pass

@timer
def pt2():
    pass

with open('input.txt') as f:
    datum = [l.strip('\n') for l in f.read().split('\n')]


