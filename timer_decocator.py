import time

def timer(func):
    """
    Function that measures the time of the function called func

    params: func -> any function that you want to check for
    returns: real -> function that really shows the time and measures
    """
    def real(*args, **kwargs):

        time1 = time.time()

        func(*args, **kwargs)

        total = time.time() - time1

        print(f"The function {func.__name__} took {total} seconds ")

    return real

# @timer
# def test():
#     """
#     Function that tests the function timer() which is decorator for this class

#     params: none
#     returns: none
#     """
#     for x  in range(1000):
#         if x==1 or x == 1000:
#             print(x)


