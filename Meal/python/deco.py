
def decorator_func(ori_func):
    def wrapper(n):
        print("before call")
        res = ori_func(n)
        print("after call")
        return res
    return wrapper

@decorator_func
def call_dad(n):
    for i in range(n):
        print("dady's home")
    pass

call_dad(5)