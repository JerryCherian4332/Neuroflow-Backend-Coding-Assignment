from flask import Flask, render_template


app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def home():
    return render_template('welcomepage.html')


if __name__ == '__main__':
    app.run()