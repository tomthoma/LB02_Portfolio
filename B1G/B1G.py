from flask import Flask

app = Flask(__name__)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci/<int:n>')
def fibonacci_route(n):
    fibonacci_sequence = [fibonacci(i) for i in range(n + 1)]
    return f"Fibonacci-Folge bis zur Position {n}: {fibonacci_sequence}"

if __name__ == '__main__':
    app.run(debug=True)
