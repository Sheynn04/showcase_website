from flask import Flask, render_template, request

app = Flask(__name__)

from flask import Flask, render_template, request

app = Flask(__name__)

def shunting_yard(infix):
   
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative = {'^'}
    
    output = []
    operator_stack = []
    
    tokens = []
    i = 0
    while i < len(infix):
        char = infix[i]
        
        if char.isspace():
            i += 1
            continue
        
        if char.isdigit() or char == '.':
            num = ''
            while i < len(infix) and (infix[i].isdigit() or infix[i] == '.'):
                num += infix[i]
                i += 1
            tokens.append(num)
            continue
        
        if char.isalpha():
            var = ''
            while i < len(infix) and infix[i].isalpha():
                var += infix[i]
                i += 1
            tokens.append(var)
            continue
        
        tokens.append(char)
        i += 1
    
    for token in tokens:
        if token[0].isdigit() or token[0].isalpha():
            output.append(token)
        
        elif token == '(':
            operator_stack.append(token)
      
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()
        
        elif token in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   operator_stack[-1] in precedence and
                   (precedence[operator_stack[-1]] > precedence[token] or
                    (precedence[operator_stack[-1]] == precedence[token] and 
                     token not in right_associative))):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output.append(operator_stack.pop())
    
    return ' '.join(output)

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

@app.route('/infixToPostfix', methods=['GET', 'POST'])
def infix_to_postfix():
    result = None
    error = None
    if request.method == 'POST':
        try:
            infix_expr = request.form.get('infixExpression', '')
            if infix_expr:
                result = shunting_yard(infix_expr)
            else:
                error = "Please enter an infix expression"
        except Exception as e:
            error = f"Error: {str(e)}"
    return render_template('infixToPostfix.html', result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
