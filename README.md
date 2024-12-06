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

## Flask - Application

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

## Flask - Routing

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

## Flask - Variable Rules

We can also do dynamic routing using variable rules as;

```js
@app.route('/blog/<blog_id>')
// @app.route('/blog/<int:blog_id>')  // We can also specify the data type
def blogPost(blog_id):
    return "This is blog post number "+ blog_id
```

## Flask - URL Building

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

## Flask - HTTP Methods

There are various flask HTTP methods which can be used for data retrieval. We can use those methods by providing "methods" argument to "route()" decorator such as;

```js
@app.route('/login', methods=['POST', 'GET'])
```

To check the methods, we can use the "request.method" but before that we need to import "request" object;

```js
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def methods():
    if request.method == 'POST':
```

## Flask - Templates

We can render flask templates (for eg: .html files) instead of writing whole HTML code while returning. For that we need to import "render_template" and then use it to to pass the ".html" file as argument.

```js
from flask import render_template

@app.route('/')
def hello():
    return render_template("hello.html")
```

Make sure that all of your ".html" files are inside the "templates" folder of your root directory.

## Flask - Static Files

To style and add functionality to our ".html" files, we need to ".css" and ".js" files but those files cannot be kept inside our "templates" folder. We have to keep those files inside our "static" folder of the root directory. And then we can get access to those files using "<link>" or "<script>" tag as;

```js
<link rel="stylesheet" href="{{ url_for('static', filename='./css/main.css')}}" />
<script src="{{ url_for('static', filename='js/script.js') }}">
```

## Flask - Request Object

Flask "request" object allows us to acess our "form", "cookies", "files" and other data. But before that we need to import it using the following command;

```js
from flask import request
```

## Flask - Cookies

Flask cookies are used to store data on clients side for fast retrieval. The data stored are of less importance. We can only set cookies using response object. For that, we need to use "make_response()" function which should be imported as;

```js
@app.route('/setCookie', methods=['POST', 'GET'])
def setCookie():
    if request.method == 'POST':
        user= request.form['nm']
        resp = make_response(render_template('readCookie.html'))  # In Flask, cookies are attached to response object. So, we first have to make response and then set cookie
        resp.set_cookie('userID', user)
        return resp
```

Cookies must be set using "post" method because "post" method is usually more secure than "get" method. After getting response object, cookie is set using "set_cookie" method which takes two arguments (i.e key and value to be set) whose syntax is written below

```js
response.set_cookie(key, value);
```

To get cookie, we can use the "request.cookies.get()" method as;

```js
@app.route('/getCookie')
def getCookie():
    name = request.cookies.get('userID')
    return "<h1>Welcome" + name + "</h1>"
```

This method takes only key as argument and returns the corresponding value

## Flask - Sessions

We can also store clients data using "sessions". Sessions are stored on server side and are generally cleared when the user closes the browser. But it can also be stored for long time by adding some lines of code which will be explained later.
At first we need to import session using the following command;

```js
from flask import session
```

For using session, we must set secret key as;

```js
app.secret_key = "Your secret key";
```

Then you can set session data simply by assigning value to the key like we do for dictionary object and retrieve those values in the same way

```js
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True  # Makes session permanent
        user = request.form['nm']
        session['user'] = user  # Storing information using "session"
        flash("Login Successful")
        return redirect(url_for("user"))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html", user=user)
```

To set your session to permanent, you need to assign the duration as;

```js
app.permanent_session_lifetime = timedelta((minutes = 5));
```

The duration can even be "minutes", "hours" etc.
Also to use the "timedelta" function, you first need to import it form "datetime" module

```js
form datetime import timedelta
```

After setting duration, make "session.permanent" "True" before setting session data;

```js
session.permanent = True;
```

## Flask - Message flashing

We can also generate informative message in flask using "flash" method. For that we need to first import flash

```js
from flask import flash
```

Then you can simply flash the message using "flash" function as;

```js
flash("Your message", "info");
```

You can also pass another parameter which is category but is optional. The syntax is;

```js
flash(message, category);
```

After flashing the message in your python file, you need to add the following lines of code at the top of your ".html" file inside your template folder

```js
{% extends 'base.html' %}

{% block body %}

{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for msg in messages %}
            <p>{{ msg }}</p>
        {% endfor %}
    {% endif %}
{% endwith %}

{% endblock %}
```

## Flask - File Uploading

To upload the files first you must set your form method to "post" and add another attribute "enctype" and assign it to "multipart/form-data". Also to browse to your file, your input type must be file.

```js
<form
  action="http://127.0.0.1:5000/uploader"
  method="post"
  enctype="multipart/form-data"
>
  <p>
    <input type="file" name="file" />
  </p>
  <p>
    <input type="submit" value="Upload" />
  </p>
</form>
```

Then access the file using "request" method and save it using "secure_filename" but before that you need to import "secure_filename" from "werkzeug.utils" module

```js
from werkzeug.utils import secure_filename

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File uploaded successfully"
```

Since here the path to be saved is not assigned. So, by default it will be saved in your root directory.

## Flask - Mail

To send mail, we need to first install "flask_mail" module since it's and extension to flask, using the following command;

```js
pip install flask_mail
```

Then import "Mail" and "Message" class using the following command;

```js
from flask_mail import Mail, Message
```

Then first create an object using Mail class and configure your app settings as;

```js
mail = Mail(app);

app.config["MAIL_SERVER"] = "smtp.gmail.com";
app.config["MAIL_PORT"] = 465;
app.config["MAIL_USERNAME"] = "josephbohora.222@gmail.com";
app.config["MAIL_PASSWORD"] = "helluraj";
app.config["MAIL_USE_TLS"] = False;
app.config["MAIL_USE_SSL"] = True;
```

You need to pass the "app" i.e; "Flask" object as argument to the "Mail" constructor. Then create message object using "Message" class by passing 3 important arguments (i.e subject, sender and recipients). Also write message you want to send by assigning it to msg.body. Finally send the message using "mail.send()" function passing your "messasge" object as argument as;

```js
@app.route('/')
def index():
     msg = Message("Hello", sender="chyroshan066@gmail.com", recipients=['roshan98125930688@gmail.com'])
     msg.body = "Sending mail using my flask app"
     mail.send(msg)
     return "Message Sent"
```

## Flask -WTForms

To use "flask WTForms", you need to install it using the following command;

```js
pip install flask-WTF
```

After installing it, create separate file (eg: form.py) and import "FlaskForm" from "flask-wtf" and the required input fields and "validator" from "wtforms" as;

```js
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, RadioField, SelectField, validators, SubmitField
```

Then create a form class (eg: ContactForm) which extends "FlaskForm" and write the required fields you want and also the validation;

```js
class ContactForm(FlaskForm):
    name = StringField("Name of Student", [validators.DataRequired("Please enter your name.")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField('Address')
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    age = IntegerField("Age")
    language = SelectField("Languages", choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")
```

Then in your main app import the "ContactForm" class from "form" module

```js
from forms import ContactForm
```

Make sure to write a secret key

```js
app.secret_key = "development key";
```

Then create the "ContactForm" object and validate it as;

```js
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form  = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("contact.html", form=form)
        else:
            return render_template("success.html")
    else:
        return render_template("contact.html", form=form)
```

Now in your template flash the error messages as;

```js
{% for message in form.name.errors %}
    <div>{{ message }}</div>
{% endfor %}

{% for message in form.email.errors %}
    <div>{{ message }}</div>
{% endfor %}
```

Use those field names and labels inside the form dynamically as;

```js
<form action="/contact" method="post">
  <fieldset>
    <legend>Contact Form</legend>
    {{ form.hidden_tag() }}

    <div style="font-size: 20px; font-weight: bold; margin-left: 150px">
      {{ form.name.label }}<br />
      {{ form.name }}
      <br />
      {{ form.gender.label }} {{ form.gender }}
      <br />
      {{ form.address.label }}<br />
      {{ form.address }}
    </div>
  </fieldset>
```
