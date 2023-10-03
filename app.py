from flask import Flask,request,render_template, redirect,Response

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('spacetravel.html')

if __name__ == '__main__':
    app.debug = True
    app.run()


