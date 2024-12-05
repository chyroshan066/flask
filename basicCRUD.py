from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

"""@app.route('/')
def hello_world():
    return "Hello World!"""

# Routing using "add_url_rule"
"""def hello_world():
    return "Hello World!"
app.add_url_rule('/', 'hello_world', hello_world)"""

# Variable Rules in Routing
"""@app.route('/blog/<blog_id>')
# @app.route('/blog/<int:blog_id>')  # We can also specify the data type 
def blogPost(blog_id):
    return "This is blog post number "+ blog_id"""

# Dynamic URL binding
"""@app.route('/admin')
def admin():
    return "<h1>Hello Admin</h1>"

@app.route('/librarian')
def librarian():
    return "<h1>Hello Librarian</h1>"

@app.route('/student')
def student():
    return "<h1>Hello Student</h1>"

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for("admin"))
    elif name == 'librarian':
        return redirect(url_for("librarian"))
    elif name == 'student':
        return redirect(url_for("student"))"""

# Templates
@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)