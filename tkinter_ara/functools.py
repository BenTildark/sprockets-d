# import functools


def trackcalls(func):
# @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper


# @trackcalls
def example():
    pass


example()

# Actual Code!:
if example.has_been_called:
    print("foo bar")
