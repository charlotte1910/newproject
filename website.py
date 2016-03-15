from flask import Flask, render_template, redirect, url_for, request

app = Flask (__name__)

@app.route('/students/')
def students():
    list_of_students = ["Jack", "Rachel", "Anna", "Mark", "Sue"]
    return render_template('students.html', students=list_of_students)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    return "Welcome page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']!= 'admin' or request.form['password']!= 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
