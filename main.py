from flask import Flask, request, redirect, render_template, session, flash
import html
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods =['GET','POST'])
def index():

    if request.method == 'POST':
        username = request.form['username']
        if (not username) or (username.strip() == "") or (len(username) <= 2) or (len(username) >=21):
            user_error = "Please enter a username between 3 and 20 characters."
            return render_template('index.html', user_error=user_error)
            # return redirect("/?error=" + user_error)

        password = request.form['password']
        if (not password) or (password.strip() == "") or (len(password) <= 2) or (len(password) >=21):
            pass_error = "Please enter a password between 3 and 20 characters."
            return render_template('index.html', pass_error=pass_error)
            # return redirect("/?error=" + pass_error)

        reenter = request.form['reenter']
        if (reenter != password):
            reenter_error = "Please reenter your same password."
            return render_template('index.html', reenter_error=reenter_error)
            # return redirect("/?error=" + reenter_error)
            
        email = request.form['email']
        if (re.search(regex,email)):
            return redirect('/welcome?user=' + username)
        else:
            email_error = "A password in optional, but if one is entered, it must be valid."
            return render_template('index.html', email_error=email_error)
            # return redirect("/?error=" + email_error)
        
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('user')
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run()
