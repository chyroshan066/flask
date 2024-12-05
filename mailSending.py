from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "josephbohora.222@gmail.com"
app.config['MAIL_PASSWORD'] = "helluraj"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def index():
     msg = Message("Hello", sender="chyroshan066@gmail.com", recipients=['roshan98125930688@gmail.com'])
     msg.body = "Sending mail using my flask app"
     mail.send(msg)
     return "Message Sent"

if __name__ == '__main__':
     app.run(debug=True)