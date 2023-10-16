__author__ = "Ebire Folayemi Michael, ArcadeDesigns"
__email__ = "folayemiebire@gmail.com"
__status__ = "development"


import os
import subprocess
import webbrowser

def rename_project(project_name):
    # Ask the user for the renaming option
    print(f"How would you like to rename '{project_name}'?")
    print("1. Remove Spaces")
    print("2. Add Hyphens")
    print("3. Join Separated Words")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        new_project_name = project_name.replace(' ', '')
    elif choice == '2':
        new_project_name = project_name.replace(' ', '-')
    elif choice == '3':
        new_project_name = ''.join(project_name.split())
    else:
        print("Invalid option. Please choose a valid option (1/2/3).")
        return

    # Rename the project directory
    os.rename(project_name, new_project_name)
    print(
        f"Project '{project_name}' has been renamed to '{new_project_name}'.")


def create_flask_project():
    # Create the project directory

    project_name = input("Confirm your project name: ")
    if os.path.exists(project_name):
        print(
            f"The project directory '{project_name}' already exists. Please choose a different name.")
        exit(1)

    os.makedirs(project_name)

    # Option to include a virtual environment
    create_venv = input(
        "Create a virtual environment for the project? (y/n): ").strip().lower()
    if create_venv == 'y':
        os.system(f"python -m venv {project_name}/venv")

    # Create static folder and subfolders
    static_path = os.path.join(project_name, "static")
    os.makedirs(static_path)
    os.makedirs(os.path.join(static_path, "css"))
    os.makedirs(os.path.join(static_path, "img"))
    os.makedirs(os.path.join(static_path, "js"))

    # Create template folder and HTML files
    template_path = os.path.join(project_name, "templates")
    os.makedirs(template_path)

    with open(os.path.join(template_path, "index.html"), "w") as index_file:
        index_file.write("""<header class="header">
    <h1 class="project-title">{{ project_name }}</h1>
    <p class="tagline">{{ tagline }}</p>
</header>

<main class="main">
    <section class="container">
        <h2>About {{ project_name }}</h2>
        <p>This is a Python Flask project created with Create@Flask.</p>
        <p>It includes a virtual environment and a basic project structure for your web application.</p>
    </section>

    <section class="container">
        <h2>Getting Started</h2>
        <p>Follow the instructions below to set up and run your Flask project:</p>
        <ol>
            <li>Activate the virtual environment (if created).</li>
            <li>Export environment variables:</li>
            <code class="code-block">
                export FLASK_DEBUG=True
                export FLASK_APP={{ project_name }}/app.py
            </code>
            <li>Run the Flask application:</li>
            <code class="code-block">flask run</code>
        </ol>
    </section>
</main>

<footer class="footer">
    <p>&copy; <span id="year"></span> {{ project_name }}</p>
</footer>""")

    with open(os.path.join(template_path, "base.html"), "w") as base_file:
        base_file.write("""<!DOCTYPE html>
    <html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta property="og:type" content="website">
        <meta property="type" content="website">
        <title>{{ title }}</title>

        <!-- Links -->
        <link rel="canonical" href="{{ link }}">
        <link rel="shortcut icon" type="image/png" href="{{ favicon_url }}">

        <!-- Other Meta Functions -->
        <meta name="apple-touch-fullscreen" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta property="og:image" content="{{ og_image_url }}">
        <meta property="twitter:image" content="{{ twitter_image_url }}">
        <meta property="twitter:card" content="summary_large_image">
        <meta name="google-site-verification" content="{{ google_verification }}">
        <link rel="icon" href="{{ icon_url }}">

        <!-- SEO Functions -->
        <meta name="og:description" content="{{ meta_description }}">
        <meta name="description" content="{{ meta_description }}">
        <meta name="og:keywords" content="{{ keywords }}">
        <meta name="keywords" content="{{ keywords }}">

        <!-- Editing Required -->
        <meta name="rating" content="General">
        <meta content="all" name="Googlebot-Image">
        <meta content="all" name="Slurp">
        <meta content="all" name="Scooter">
        <meta content="ALL" name="WEBCRAWLERS">
        <meta name="revisit-after" content="1 day">
        <meta name="robots" content="index, follow">
        <meta name="author" content="{{ author }}">
        <meta name="revised" content="{{ revised }}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- Bootstrap CSS CDN Link -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <!-- FontAwesome CDN Link -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">

        <!-- BoxIcons CDN Link -->
        <link href="https://unpkg.com/boxicons@2.1.2/css/boxicons.min.css" rel="stylesheet">

        <!-- Scroll Reveal -->
        <script src="https://unpkg.com/scrollreveal"></script>

        <!-- Style Sheet -->
        <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">
    </head>

    <body>
        {% include "navbar.html" %}

        {% block content %}

        {% endblock %}

        {% include "footer.html" %}

        <!-- JavaScript Section -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    </body>
    </html>
    """)

    with open(os.path.join(template_path, "navbar.html"), "w") as navbar_file:
        navbar_file.write("<div>Navbar content</div>")

    with open(os.path.join(template_path, "footer.html"), "w") as footer_file:
        footer_file.write("<div>Footer content</div>")

    with open(os.path.join(template_path, "404.html"), "w") as error_file:
        error_file.write("<div>404 Error Code</div>")

    with open(os.path.join(template_path, "500.html"), "w") as server_error_file:
        server_error_file.write("<div>500 Error Code</div>")

    with open(os.path.join(static_path, "css", "style.css"), "w") as css_file:
        css_file.write("""/* Add your CSS styles here */\n\n""")

    with open(os.path.join(static_path, "js", "main.js"), "w") as js_file:
        js_file.write("""// Add your JavaScript code here\n\n""")

    with open(os.path.join(project_name, "app.py"), "w") as app_file:
        app_file.write("""from flask import Flask, render_template
from models import Users
from forms import UserForm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)

    """)

    with open(os.path.join(project_name, "forms.py"), "w") as forms_file:
        forms_file.write("""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField

class UserForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    bio_summary = StringField()
    location = StringField()
    facebook_account = StringField()
    twitter_account = StringField()
    instagram_account = StringField()
    password_hash = PasswordField(validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField(validators=[DataRequired()])
    profile_pic = FileField()
    submit = SubmitField()

    """)

    with open(os.path.join(project_name, "models.py"), "w") as models_file:
        models_file.write("""from database import db
from datetime import date, datetime
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    bio_summary = db.Column(db.Text(), nullable=True)
    profile_pic = db.Column(db.String(), nullable=True)
    password_hash = db.Column(db.String())

    location = db.Column(db.Text(), nullable=True)
    facebook_account = db.Column(db.Text(), nullable=True)
    twitter_account = db.Column(db.Text(), nullable=True)
    instagram_account = db.Column(db.Text(), nullable=True)
    
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def formatted_date(self):
        return self.date_added.strftime("%B %Y")

    def formatted_date_with_day(self):
        return self.date_added.strftime("%d %B %Y")

    def formatted_time(self):
        return self.date_added.strftime("%I:%M %p").lstrip('0')

    def time_since_posted(self):
        time_diff = datetime.now() - self.date_added
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if time_diff.days > 0:
            return f"{time_diff.days} days ago"
        elif hours > 0:
            return f"{hours} hours ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return "just now"

    @property
    def password(self):
        raise AttributeError(' Password Not A Readable Attribute !!! ')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # create string
    def __repr__(self):
        return '<Name %r>' % self.name
""")

    with open(os.path.join(project_name, "create_db.py"), "w") as create_db_file:
        create_db_file.write("""from app import app, db

with app.app_context():
    db.create_all()""")

    with open(os.path.join(project_name, "database.py"), "w") as database_file:
        database_file.write("""from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


""")

    with open(os.path.join(project_name, ".gitignore"), "w") as gitignore_file:
        gitignore_file.write(""".gitignore

/venv
packages.py""")

    with open(os.path.join(project_name, "packages.py"), "w") as install_dependencies_files:
        install_dependencies_files.write("""import os
import subprocess
import webbrowser

def activate_and_run_project():
    # Ensure the 'venv' folder exists
    if not os.path.exists('venv'):
        print("Virtual environment 'venv' does not exist. Please create it using 'main.py'.")
        return

    # Activate the virtual environment (Windows and non-Windows)
    if os.name == 'nt':
        venv_activate_cmd = os.path.join("venv", "Scripts", "activate")
    else:
        venv_activate_cmd = "source venv/bin/activate"
    
    subprocess.call(venv_activate_cmd, shell=True)

    # Install dependencies from requirements.txt
    subprocess.call("pip install -r requirements.txt", shell=True)

    # Set FLASK_APP environment variable with the full path to app.py
    app_path = os.path.abspath("app.py")
    os.environ['FLASK_APP'] = app_path

    while True:
        print("Select a port to run Flask:")
        print("1. 5000")
        print("2. 8000")
        print("3. 5050")
        print("4. 8080")
        print("5. 7000")
        print("6. 7070")
        selected_option = input("Choose an option (1/2/3/4/5/6): ").strip()
        if selected_option in ['1', '2', '3', '4', '5', '6']:
            break
        else:
            print("Invalid option. Please choose a valid option.")

    flask_run_port = {
        '1': '5000',
        '2': '8000',
        '3': '5050',
        '4': '8080',
        '5': '7000',
        '6': '7070'
    }[selected_option]

    os.environ['FLASK_RUN_PORT'] = flask_run_port

    # Run the Flask application
    flask_run_cmd = f"flask run --port={flask_run_port}"
    subprocess.Popen(flask_run_cmd, shell=True)

    webbrowser.open_new_tab(f"http://127.0.0.1:{flask_run_port}")

if __name__ == '__main__':
    activate_and_run_project()
""")

    # Create requirements.txt file for dependencies
    with open(os.path.join(project_name, "requirements.txt"), "w") as requirements_file:
        requirements_file.write("Flask\nalembic==1.10.2\ncertifi==2022.12.7\ncharset-normalizer==3.1.0\nclick==8.1.3\ncolorama==0.4.6\nFlask==2.2.3\nFlask-CKEditor==0.4.6\nFlask-Login==0.6.2\nFlask-Migrate==4.0.4\nFlask-SQLAlchemy==3.0.3\nFlask-WTF==1.1.1\ngreenlet==2.0.2\nidna==3.4\nimportlib-metadata==6.0.0\nitsdangerous==2.1.2\nJinja2==3.1.2\nMako==1.2.4\nMarkupSafe==2.1.2\npsycopg2-binary==2.9.5\nrequests==2.28.2\nSQLAlchemy==2.0.5.post1\ntyping-extensions==4.5.0\nurllib3==1.26.14\nWerkzeug==2.2.3\nWTForms==3.0.1\nzipp==3.14.0\n")

    print(
        f"Created Flask project '{project_name}' with the desired structure.")

if __name__ == '__main__':
    project_name = input("Enter the project name: ")
    create_flask_project()
    
    # Additional instructions
    print("Your project has been created. To set up and run your Flask project, please follow these steps:")
    print("1. Navigate to your created project folder.")
    print("2. Activate your virtual environment using the following commands:")
    print("   - For Bash: source venv/Scripts/activate")
    print("   - For Command Prompt (Windows): venv\\Scripts\\activate")
    print("3. Once the virtual environment is activated, run the following command to install dependencies and run your Flask app:")
    print("   - cd <Project Name>")
    print("   - Start your venv")
    print("   - run 'python packages.py' to start the application")