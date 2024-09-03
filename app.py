from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return f'<h1> HI I AM JERIN </h1>'

if __name__ == '__main__':
    app.run(debug=True)
