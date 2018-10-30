from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def display_user_signup():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def validate_signup():

    user_name = request.form['user_name']
    password = request.form['password']
    password_validate = request.form['password_validate']
    email = request.form['email']

    user_name_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    if len(user_name) > 20 or len(user_name)<3 or " " in user_name:
        user_name_error = "Adjust username length."


    if len(password) > 20 or len(password)<3 or " " in password:
        password_error = "Adjust password length."

    if password_validate != password:
        password_validate_error = "Passwords must match"
    
    if len(email) > 1:
        if "@" and "." not in email or len(email) > 20 or len(email) < 3 or ' ' in email:
            email_error = 'Not a Valid E-mail'
        
            

    if not user_name_error and not password_error and not password_validate_error and not email_error:
        
        return redirect('/welcome?user_name={0}'.format(user_name))
    else:
        return render_template('index.html', user_name_error=user_name_error, password_error=password_error, password_validate_error=password_validate_error,email_error=email_error)


@app.route('/welcome')
def valid_signup():
    user_name = request.args.get('user_name')

    return render_template('welcome.html', user_name=user_name)

app.run()