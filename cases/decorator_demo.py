"""
Decorator practice
"""
import functools
import time

print("--------函数当做变量---------------")


def func(message):
    print("Got a message: {}".format(message))


send_message = func

send_message("Hello World")

print("--------函数当做参数--------------")


def get_message(message):
    return "Got a message" + message


def root_call(func, message):
    print(func(message))


root_call(get_message, "Hello World")

print("--------函数里定义函数-------------")


def func(message):
    def get_message(message):
        print("Got a message: {}".format(message))

    return get_message(message)


func("Hello World")

print("--------函数的返回值是函数对象（闭包）-------------")


def func_closure():
    def get_message(message):
        print("Got a message: {}".format(message))

    return get_message


send_message = func_closure()
send_message("Hello World")

print("--------简单装饰器-------------")


def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()

    return wrapper


def greet():
    print("Hello World")


greet = my_decorator(greet)
greet()

print("---------简单装饰器(改良版)----------")


@my_decorator
def greet():
    print("Hello World")


greet()

print("---------带有参数的装饰器----------")


def my_decorator(func):
    def wrapper(message):
        print("wrapper of decorator")
        func(message)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet("Hello World")

print("---------通用装饰器----------")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("wrapper of decorator")
        func(*args, **kwargs)

    return wrapper


print("---------自定义参数参数的装饰器----------")


def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print("wrapper of decorator")
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet("Hello World")
print(greet.__name__)
print(help(greet))

# def my_decorator2(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("execute decorator2")
#         func(*args, **kwargs)
#     return wrapper
#
#
# @my_decorator2
# def greet(message):
#     print(message)


print("---------解决上述原来是被装饰器内部函数wrapper函数取代的问题----------")

import functools


def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("wrapper of decorator")
        func(*args, **kwargs)

    return wrapper


@my_decorator3
def greet(message):
    print(message)


print(greet.__name__)

print("---------类装饰器----------")


# 主要依赖于函数__call__


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"num of calls is:{self.num_calls}")
        return self.func(*args, **kwargs)


@Count
def example():
    print("Hello World")


example()

example()

print("---------类装饰器----------")


# 主要依赖于函数__call__


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"num of calls is:{self.num_calls}")
        return self.func(*args, **kwargs)


@Count
def example():
    print("Hello World")


example()

example()

print("---------嵌套装饰器·----------")


def my_decorator5(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("execute decorater5")
        func(*args, **kwargs)

    return wrapper


def my_decorator6(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("execute decorater6")
        func(*args, **kwargs)

    return wrapper


@my_decorator5
@my_decorator6
def greet(message):
    print(message)


greet("Hello World")

print("---------装饰器案例【身份认证】·----------")

# def authenticate(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         request = args[0]
#         if check_user_logged_in(request):
#             return func(*args,**kwargs)
#         else:
#             raise Exception("Authentication failed")
#     return wrapper
#
# @authenticate
# def post_comment(request, ...):
#     ...


print("---------装饰器案例【日志记录】·----------")


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000} ms")
        return res

    return wrapper


@log_execution_time
def calculate_similarity(items):
    ...


print("---------装饰器案例【输入合理性检查】·----------")


def validation_check(input):
    @functools.wraps(input)
    def wrapper(*args, **kwargs):
        ...


@validation_check
def neural_network_training(params1, param2, ):
    ...
