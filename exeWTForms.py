from flask import Flask, request, flash, render_template 
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

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
        

if __name__ == '__main__':
    app.run(debug=True)