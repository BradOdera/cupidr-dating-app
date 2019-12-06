from flask import render_template,url_for
from . import main
from flask_login import login_required,current_user


#display categories on the landing page
@main.route('/index')
def index():
    """ View root page function that returns index page """

    title = 'Home | cupidR'
    return render_template('index.html', title = title)

@main.route('/')
def sessions():
    return render_template('session.html')
