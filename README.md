# Create@Flask: A Python Flask Project Generator

**Create@Flask** is a Python open-source package that allows you to quickly generate a basic Flask project structure for web development. It simplifies the process of setting up a Flask project, including creating directories for static files, templates, and generating essential Python files. You can also choose to create a virtual environment for your project.

**Author:** Ebire Folayemi Michael, ArcadeDesigns
**Email:** folayemiebire@gmail.com
**Status:** Development

## Usage

To use Create@Flask, follow these steps:

### 1. Installation

Install the Create@Flask package using pip:

```bash
pip install create-at-flask
```

### 2. Running the Generator

You can run the generator by importing the package and calling the `create_flask_project` function. This will guide you through setting up your Flask project.

```python
from create_at_flask import create_flask_project

if __name__ == '__main__':
    create_flask_project()
```

### 3. Project Generation

When you run the generator, it will walk you through the following steps:

1. **Project Name**: Enter the name for your Flask project.

2. **Virtual Environment**: Optionally create a virtual environment for your project.

3. **Project Structure**: Create the necessary directories and files for a basic Flask application.

### 4. Running the Flask App

After setting up the project, you can follow the instructions provided to start your Flask application. This includes activating the virtual environment (if created) and running Flask:

#### Linux/Unix

```bash
export FLASK_DEBUG=True
export FLASK_APP=your_project_name/app.py
flask run
```

#### Windows (cmd)

```bash
set FLASK_DEBUG=True
set FLASK_APP=your_project_name\app.py
flask run
```

### 5. Accessing Your App

Your Flask application will be running at `http://127.0.0.1:5000` (or your chosen port). You can access it in your web browser to start building your web application.

## Features

- Automatic generation of Flask project structure.
- Option to create a virtual environment for the project.
- Pre-configured template files and directories for static files.
- Example Flask application code.
- Easy deployment to start developing your web application.

## Project Structure

After running the generator, your Flask project will have the following structure:

```
your_project_name/
├── app.py
├── database.py
├── forms.py
├── models.py
├── templates/
│   ├── base.html
│   ├── footer.html
│   ├── index.html
│   ├── 404.html
│   ├── 500.html
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── img/
│   ├── js/
│   │   ├── main.js
├── requirements.txt
├── create_db.py
```

## Dependencies

The generated Flask project includes a `requirements.txt` file with the following dependencies:

- Flask
- Flask-CKEditor
- Flask-Login
- Flask-Migrate
- Flask-SQLAlchemy
- Flask-WTF

## License

This project is open source and is available under the [BSD License](https://opensource.org/licenses/BSD).

## Contribute

If you would like to contribute to this project or report any issues, please visit the [GitHub repository](https://github.com/ArcadeDesigns/Create-Flask).

## Contact

If you have any questions or need support, feel free to reach out to the author at [folayemiebire@gmail.com](mailto:folayemiebire@gmail.com).

Start building your Flask web application easily with Create@Flask!