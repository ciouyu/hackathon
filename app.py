from flask import Flask,request,render_template, redirect,Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
#map
@app.route('/race')
def race():
    return render_template('map.html')
@app.route('/map1')
def race1():
    return render_template('map1.html')
@app.route('/map2')
def race2():
    return render_template('map2.html')
@app.route('/map3')
def race3():
    return render_template('map3.html')
@app.route('/map4')
def race4():
    return render_template('map4.html')
@app.route('/map5')
def race5():
    return render_template('map5.html')
@app.route('/map6')
def race6():
    return render_template('map6.html')
@app.route('/map7')
def race7():
    return render_template('map7.html')
@app.route('/map8')
def race8():
    return render_template('map8.html')



@app.route('/aboutus')
def au():
    return render_template('aboutus.html')

#craft
@app.route('/craft')
def craft():
    return render_template('craft.html')
@app.route('/craft2')
def craft2():
    return render_template('craft2.html')
@app.route('/craft3')
def craft3():
    return render_template('craft3.html')
@app.route('/craft4')
def craft4():
    return render_template('craft4.html')
@app.route('/craft5')
def craft5():
    return render_template('craft5.html')

@app.route('/info')
def info():
    return render_template('info.html')

#info    
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


