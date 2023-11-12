from flask import Flask, render_template

app = Flask(__name__)

def compare_elements(a, b):
    return a > b

def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr, compare_func, swap_func):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if compare_func(arr[j], arr[j+1]):
                swap_func(arr, j, j+1)

@app.route('/sort/<numbers>')
def sort_numbers(numbers):
    num_list = list(map(int, numbers.split(',')))
    bubble_sort(num_list, compare_elements, swap_elements)
    return f"Sortierte Zahlen: {num_list}"

if __name__ == '__main__':
    app.run(debug=True)
