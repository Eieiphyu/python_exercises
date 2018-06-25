from flask import Flask 
myapp = Flask(__name__)

@myapp.route('/')
def hello_word():
    greeting = "World"
    return f'Hello, {greeting}'
if __name__ == "__main__":
    myapp.run()
