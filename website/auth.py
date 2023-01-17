from flask import Blueprint,render_template, request, flash
#urls organization
auth =Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Testing", user="Tim", boolean=True) #how to pass variables to html

@auth.route('/logout') #http://127.0.0.1:5000/logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email= request.form.get('email')
        firstName= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')
        if len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName)<2:
            flash('Name must be greater than 1.', category='error')
        elif password1!= password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1)<7:
            flash('Password must be greater than 6', category='error')
        else:
            flash('Account created!', category='success')
    return render_template("sign_up.html")



