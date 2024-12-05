from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Roshan"  # It is necessary to set "secret_key" while storing session data
app.permanent_session_lifetime = timedelta(minutes=5)  # Stores the session data for time defined even if the user closes the browser

@app.route('/')
def home():
    return "<h1>You are in homepage</h1>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True  # Makes session permanent
        user = request.form['nm']
        session['user'] = user  # Storing information using "session"
        flash("Login Successful")
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            flash("You are already logged In!")
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash("You are not logged In!")
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash("You have been logged out successfully", "info")  # Flashes out with this message
    session.pop('user', None)  # Removes the user data from the session. "None" is a message
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 