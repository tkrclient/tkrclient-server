if __name__ == '__main__':
    app.run(debug=True)

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'
