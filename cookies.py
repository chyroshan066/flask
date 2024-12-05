from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setCookie.html') 

@app.route('/setCookie', methods=['POST', 'GET'])
def setCookie():
    if request.method == 'POST':
        user= request.form['nm']
        resp = make_response(render_template('readCookie.html'))  # In Flask, cookies are attached to response object. So, we first have to make response and then set cookie
        resp.set_cookie('userID', user)
        return resp
    
@app.route('/getCookie')
def getCookie():
    name = request.cookies.get('userID')
    return "<h1>Welcome" + name + "</h1>"

if __name__ == '__main__':
    app.run(debug=True)