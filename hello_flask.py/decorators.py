import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before function
        function()
        function()# also could run twice
        # or do something after function
    return wrapper_function


# a decorator function wraps another function and gives it additional functionality
@delay_decorator # decorator usage causes the function to wait 2s before running
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greetings():
    print("How are you?")

say_hello()
say_greetings()
say_bye()


# additional syntax - assign a function to a variable, then call the variable as a function when wanted
decorated_function = delay_decorator(say_greetings)
decorated_function()