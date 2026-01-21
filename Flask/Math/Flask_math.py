from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        # Get numbers and operation from the form
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        except (ValueError, TypeError):
            result = "Error: Please enter valid numbers"

    return render_template('math.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)