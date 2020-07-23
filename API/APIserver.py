from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, static_url_path='')
logged_in = False

@app.route('/', methods=['GET'])
def home():
    return render_template('welcomepage.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        if user == "admin" and password == "123456":
            logged_in = True
            return render_template('moodpage.html')
        else:
            return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
