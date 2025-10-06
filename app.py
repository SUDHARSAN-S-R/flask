from flask import Flask,request


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/square/<int:number>')
def square(number):
    return str(number * number)

@app.route('/handle_url')
def handle_url():
    if 'greeting' not in request.args or 'name' not in request.args:
        return "Error: Please provide both 'greeting' and 'name' parameters."
    greeting = request.args['greeting'] # key access from dictionary
    name = request.args.get('name')
    return f"{greeting}, {name}!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)