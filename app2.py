from flask import Flask,request,render_template


app = Flask(__name__, template_folder='templatesfoeapp2')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form.get('password')

        return f"Welcome {username} and your password is : {password}"
    elif request.method == 'GET':
        return render_template('indexs.html',value="Hello from app2!")


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    return file.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)