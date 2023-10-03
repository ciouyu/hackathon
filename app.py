from flask import Flask,requese,render_template, redirect,Response

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('/figma/iphone_14_1/iphone_14___1.html')

if __name__ == '__main__':
    app.debug = True
    app.run()


