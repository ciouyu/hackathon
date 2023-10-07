from flask import Flask,request,render_template, redirect,Response

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('spacetravel.html')

@app.route('/aboutus')
def au():
    return render_template('aboutus.html')

@app.route('/contactus')
def cu():
    return render_template('contactus.html')

@app.route('/1')
def info1():
    return render_template('1.html')
@app.route('/2')
def info2():
    return render_template('2.html')
@app.route('/3')
def info3():
    return render_template('3.html')
@app.route('/4')
def info4():
    return render_template('4.html')
@app.route('/5')
def info5():
    return render_template('5.html')
@app.route('/6')
def info6():
    return render_template('6.html')
@app.route('/7')
def info7():
    return render_template('7.html')
@app.route('/8')
def info8():
    return render_template('8.html')



if __name__ == '__main__':
    app.debug = True
    app.run()


