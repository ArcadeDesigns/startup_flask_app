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

    project_name = input("Enter the project name: ")
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
        forms_file.write("# Forms code goes here")

    with open(os.path.join(project_name, "models.py"), "w") as models_file:
        models_file.write("# Models code goes here")

    with open(os.path.join(project_name, "create_db.py"), "w") as create_db_file:
        create_db_file.write("# Database creation code goes here")

    # Create requirements.txt file for dependencies
    with open(os.path.join(project_name, "requirements.txt"), "w") as requirements_file:
        requirements_file.write("Flask\n")

    print(
        f"Created Flask project '{project_name}' with the desired structure.")
    
    # Navigate to the project directory
    os.chdir(project_name)

    # Provide instructions for setting up the virtual environment
    if create_venv == 'y':
        print(
            f"Virtual environment has been created. Activate it using 'source {project_name}/venv/bin/activate' on Linux/Unix, or 'venv\\Scripts\\activate' on Windows.")
        
         # Set the FLASK_APP environment variable to point to your application
        os.environ['FLASK_APP'] = f"{project_name}/app.py"

        # Automatically activate the virtual environment (Windows and Unix compatible)
        if os.name == 'nt':
            venv_activate_cmd = os.path.join("venv", "Scripts", "activate")
        else:
            venv_activate_cmd = f"source venv/bin/activate"
        
        subprocess.Popen(venv_activate_cmd, shell=True)
        
        # Menu for selecting Flask run port
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

        print(f"Exporting FLASK_RUN_PORT={flask_run_port}")
        os.environ['FLASK_RUN_PORT'] = flask_run_port
        print("To start Flask, use the following commands:")
        print("1. On Linux/Unix:")
        print(f"   export FLASK_DEBUG=True")
        print(f"   export FLASK_APP={project_name}/app.py")
        print(f"   flask run")
        print("2. On Windows (cmd):")
        print(f"   set FLASK_DEBUG=True")
        print(f"   set FLASK_APP={project_name}\\app.py")
        print(f"   flask run")

        # Automatically activate the virtual environment
        venv_activate_cmd = os.path.join(project_name, "venv", "Scripts", "activate") if os.name == 'nt' else f"source {project_name}/venv/bin/activate"
        subprocess.call(venv_activate_cmd, shell=True)

        # Set the FLASK_APP environment variable to point to your application
        os.environ['FLASK_APP'] = f"{project_name}/app.py"

        # Automatically run the Flask application using the Python interpreter within the virtual environment
        flask_run_cmd = f"python -m flask run --port={flask_run_port}"
        subprocess.Popen(flask_run_cmd, shell=True)

        # Open the default web browser
        webbrowser.open_new_tab("http://127.0.0.1:" + flask_run_port)

if __name__ == '__main__':
    create_flask_project()
