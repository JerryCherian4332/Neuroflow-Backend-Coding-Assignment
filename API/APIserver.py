from flask import Flask, render_template, url_for, redirect, request
from datetime import date, timedelta

app = Flask(__name__, static_url_path='')

#Should be stored in a database so it can be retrieved
today = date.today()
yesterday = today - timedelta(days = 1)
previousLoginDate = False

#Should be authenticated better
logged_in = False

#Should be stored in a database so it can be retrieved
streak = 1

@app.route('/', methods=['GET'])
def home():
    return render_template('welcomepage.html')


@app.route('/login', methods=['GET','POST'])
def login():
    global logged_in
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #Should be retrieved from database, password should be hashed. Users should in a database and retrieved
        user = request.form.get('username')
        password = request.form.get('password')
        if user == "admin" and password == "123456":
            logged_in = True
            return render_template('moodpage.html')
        else:
            return redirect(url_for('login'))

@app.route('/mood', methods=['GET', 'POST'])
def mood():
    global streak
    global previousLoginDate
    if request.method == 'GET':
        if logged_in:
            return render_template("moodpage.html")
        else:
            return redirect(url_for('login'))
    if request.method == 'POST':
            #Needs to be looked at more to see if functionality works
            if previousLoginDate == yesterday:
                streak += 1
            previousLoginDate = today
            return render_template("ratingpage.html", rating = request.form.get('rating'), streak=streak)

@app.route('/logout')
def logout():
    global logged_in
    logged_in = False
    return render_template('welcomepage.html')



if __name__ == '__main__':
    app.run()
