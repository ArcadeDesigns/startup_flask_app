from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python Flask setup library'
LONG_DESCRIPTION = 'A package that simplifies the creation of Python Flask applications with a pre-configured project structure.'

setup(
    name="create_at_flask",
    version=VERSION,
    author="ArcadeDesigns (Ebire Folayemi Michael)",
    author_email="folayemiebire@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['Flask'],
    keywords=['python', 'Flask', 'Flask setup', 'web application', 'full-stack development'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)