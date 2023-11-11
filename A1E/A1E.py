from flask import Flask

app = Flask(__name__)

# Objektorientiertes Paradigma
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"

user1 = User("JohnDoe", "john@example.com")

# Prozedurales Paradigma
def calculate_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

numbers = [1, 2, 3, 4, 5]
total = calculate_sum(numbers)

# Funktionales Paradigma
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

squared = square_numbers(numbers)

@app.route('/')
def index():
    return (
        f"Objektorientiertes Paradigma: {user1.display_info()}<br>"
        f"Prozedurales Paradigma: Die Summe der Zahlen ist {total}<br>"
        f"Funktionales Paradigma: Quadrierte Zahlen: {squared}"
    )

if __name__ == '__main__':
    app.run(debug=True)
