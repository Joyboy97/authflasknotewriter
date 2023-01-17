from flask import Blueprint, render_template
#urls organization
views =Blueprint('views', __name__)

@views.route('/') #decorator
#url to home when this is typed in search bar the following code is run
def home():
    return render_template("home.html")