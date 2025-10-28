from flask import Flask,request,render_template,session,make_response,request,flash


app = Flask(__name__, template_folder='templatesforapp3')
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('indexs.html',value="Hello from app3!")


@app.route('/set_data')
def set_data():
    session['name'] = 'John Doe'
    session['age'] = 30
    return render_template('indexs.html', value="Data has been set!")
    

@app.route('/get_data')
def get_data():
    name = session.get('name', 'Not set')
    age = session.get('age', 'Not set')
    return render_template('indexs.html', value=f"Name: {name}, Age: {age}")


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('indexs.html', value='sessiion cleared')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('indexs.html', value="Cookie has been set!"))
    response.set_cookie('username', 'John Doe')
    return response
@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', 'Not set')
    return render_template('indexs.html', value=f"Username from cookie: {username}")
@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('indexs.html', value="Cookie has been removed!"))
    response.set_cookie('username', expires=0)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            flash('Login successful!')
            return render_template('indexs.html', value="Login if!")
        else:
            flash('Invalid credentials. Please try again.')
            return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)