from flask import Flask, render_template,redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = "Hello, World!"
    myresult = 5 * 5
    return render_template('index.html', value=myvalue, result=myresult)

@app.route('/other')
def other():
    return render_template('other.html',value="wow ")

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)