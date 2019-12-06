from flask import Flask, request, redirect, render_template
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods =['GET','POST'])
def index():

    user_error = ''
    pass_error = ''
    reenter_error = ''
    email_error = ''

    if request.method == 'POST':
        username = request.form['username']
        if (' ' in username) or (not username) or (username.strip() == "") or (len(username) <= 2) or (len(username) >=21):
            user_error = "Please enter a username between 3 and 20 characters and no spaces."
            username = ''
            # return redirect("/?error=" + user_error)

        password = request.form['password']
        if (' ' in password) or (not password) or (password.strip() == "") or (len(password) <= 2) or (len(password) >=21):
            pass_error = "Please enter a password between 3 and 20 characters and no spaces."
            # return redirect("/?error=" + pass_error)

        reenter = request.form['reenter']
        if (reenter != password):
            reenter_error = "Please reenter your same password."
            # return redirect("/?error=" + reenter_error)

        email = request.form['email']
        if email:
            if not (re.search(regex, email)):
                email_error = "An email in optional, but if one is entered, it must be valid."
                email = ''
                # return render_template('index.html', email_error=email_error)
                # return redirect("/?error=" + email_error)

        if not user_error and not pass_error and not reenter_error and not email_error:
            return redirect('/welcome?user=' + username)

        return render_template('index.html', username=username, email=email, user_error=user_error, pass_error=pass_error, reenter_error=reenter_error, email_error=email_error)
        
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('user')
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run()
