import time

def decor(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        print(time.perf_counter_ns() - start_time)
    return inner

@decor
def man():
    print("hello")

man()


