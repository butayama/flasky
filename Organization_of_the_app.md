configuration  
-------------
config.py: application configuration  

Application Factory
-------------------
app/__init__.py: application package constructor  

Blueprints
----------
app/main/__init__.py: main blueprint creation  
app/main/views.py: routes of the application
app/main/errors.py: error handlers  
**the modules are imported at the bottom of the app/main/__init__.py script to avoid errors due to circular dependencies**  

The blueprint is registered with the application inside the create_app() factory function  

app/__init__.py: main blueprint registration  
app/main/errors.py: error handlers in main blueprint

the form objects are also stored inside the blueprint in the app/main/forms.py module.  

Application Script
------------------
flasky.py: main script  
The configuration is taken from the environment variable FLASK_CONFIG if it’s defined, or else the default configuration is used  

Unit Tests
----------
tests/test_basics.py: unit tests  

Database Setup
--------------
(venv) $ flask db upgrade  

Running the Application
-----------------------
(venv) $ flask run  
