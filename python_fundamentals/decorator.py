from datetime import datetime

"""
decorator는 
"""
def print_process_time(func):
    def process_time():
        start = datetime.now()
        func()
        end = datetime.now()
        print(end - start)

    return process_time


class PrintProcessTime:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        self.func(*args, **kwargs)
        end = datetime.now()
        print(end - start)


# @print_process_time
@PrintProcessTime
def print_sample(a=None):
    print('decorator test')


# res = {}
# def fibo(n):
#     if n < 3:
#         res[n] = 1
#         return 1
#     if res.get(n):
#         return res.get(n)
#     res[n] = fibo(n - 1) + fibo(n - 2)
#     return res[n]

def fibo_deco(func):
    res = {}

    def inner(*args):
        n = args[0]
        if res.get(n):
            return res.get(n)
        r = func(n)
        res[n] = r
        return r

    return inner


@fibo_deco
def fibo(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    print_sample(1)

    # print(fibo(8))
    # print(fibo(3))
    # print(res)
