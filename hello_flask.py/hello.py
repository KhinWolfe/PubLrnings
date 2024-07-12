from flask import Flask
import random

print(random.__name__)  # prints "random"
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

# @app.route('/') is a python decorator that is only accessed if you go to home + /
@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'# flask can take html code as well.
            '<p>This is a paragraph. </p>') # and you can split lines and return multiple values`


# this decorator runs when you go to home/bye
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined # can add multiple wrappers
def say_bye():
    return "Bye"


# < something > turns into a variable that can be used
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


# This snippet allows code to be run from pycharm by hitting play vs running
# code from the terminal.
if __name__ == "__main__":  # if name of the current file is main, then execute code
    app.run(debug=True) # allows active running/rerunning of code change on website


