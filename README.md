# Flask

## Getting Started with Flask

To manage dependencies using virtual environment, follow these steps;

1. Open the terminal in VS Code and navigate to your project folder:

```js
cd / path / to / project;
```

2. Install the virtualenv package if not already installed:

```js
pip install virtualenv
```

3. Create a virtual environment in your project folder:

```
virtualenv venv
```

4. Activate the virtual environment

```js
.\venv\Scripts\activate
```

5. Install flask and other dependencies as you required:

```js
pip3 install flask flask-sqlalchemy
```

## Flask-Application

This the simplest application using flask;

```js
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!

if __name__ == '__main__':
    app.run(debug=True)
```

## Flask-Routing

We can also use "add_url_rule()" for routing instead of "route()" as;

```js
def hello_world():
    return "Hello World!
app.add_url_rule('/', 'hello_world', hello_world)
```

The sytax for "add_url_rule()" is;

```js
app.add_url_rule(<urlRule>, <endpoint>, <functionName>)
```

The endpoint should be the same function name but enclosed in "", (i.e; it should be a string)

## Flask-Variable Rules

We can also do dynamic routing using variable rules as;

```js
@app.route('/blog/<blog_id>')
// @app.route('/blog/<int:blog_id>')  // We can also specify the data type
def blogPost(blog_id):
    return "This is blog post number "+ blog_id
```

## Flask-URL Building

We can use "url_for()" for dynamically building a URL

```js
@app.route('/admin')
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
        return redirect(url_for("student"))
```

We need to pass the function name as argument in "url_for()"
