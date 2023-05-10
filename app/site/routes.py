from flask import Blueprint, render_template


# looks for site_templates in site folder, lets us use site inside other python files
site = Blueprint('site', __name__, template_folder='site_templates')



# index.html - Games Home
# lists third-party api in a data table
@site.route('/')
def gamesHome():
    return render_template('index.html')



# shows user's email, token, and db info in a table
@site.route('/profile')
def profile():
    return render_template('profile.html')









