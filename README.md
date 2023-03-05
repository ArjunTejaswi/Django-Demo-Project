# Django-Demo-Project
Commands to create a project: django-admin startproject <projectName>

__init__.py is an empty file that instructs Python to treat this directory as a Python package.
settings.py contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.
urls.py defines the site URL-to-view mappings. While this could contain all the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
wsgi.py is used to help your Django application communicate with the web server. You can treat this as boilerplate.
asgi.py is a standard for Python asynchronous web apps and servers to communicate with each other. ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous Python apps (whereas WSGI provided a standard for synchronous apps only). It is backward-compatible with WSGI and supports multiple servers and application frameworks.

The manage.py script is used to create applications, work with databases, and start the development web server.

Command to create the app: 
# Linux/macOS
python3 manage.py startapp <appName>

# Windows
py manage.py startapp catalog <appName>


A migrations folder, used to store "migrations" — files that allow you to automatically update your database as you modify your models.
__init__.py — an empty file created here so that Django/Python will recognize the folder as a Python Package and allow you to use its objects within other parts of the project.

Commands for migration: 
	python3 manage.py makemigrations
python3 manage.py migrate

To run a server:
	python3 manage.py runserver
