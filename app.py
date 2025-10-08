from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('works.html', result=result)

@app.route('/toUpperCase', methods=['GET', 'POST'])
def toUpperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/areaofCircle', methods=['GET', 'POST'])
def area_of_circle():
    result = None
    if request.method == 'POST':
        diameter = float(request.form['diameter'])
        radius = diameter / 2
        area = 3.1416 * (radius ** 2)
        result = round(area, 2)
    return render_template('areaofCircle.html', result=result)

@app.route('/areaofTriangle', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
        result = round(area)
    return render_template('areaofTriangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
