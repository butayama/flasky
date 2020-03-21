https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html
#Chapter 2. Basic Application Structure
## application instance
object of class Flask  
The web server passes all requests it receives from clients to this object for handling, using a protocol called Web Server Gateway Interface (WSGI, pronounced “wiz-ghee”)
```python
from flask import Flask
app = Flask(__name__)
```

## routes - view functions
AThe association between a URL and the function that handles it is called a route  
a route is declared using the **app.route** decorator.
```python
@app.route('/')  
def index():  
    return '<h1>Hello World!</h1>'
```
A common use of decorators is to register functions as handler functions to be invoked when certain events occur.  
The function registers **index()** as the **handler** for the application’s root URL.   
Functions like index() that handle application URLs are called **view functions**.  
Jinja2 is used to generate HTML responses for better maintainance.  

## app.route decorator
defines a defines a route that has a dynamic component  
```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```
when the view function is invoked, the dynamic component will be passed as an argument  

## Development Web Server
FLASK_APP environment variable
Linux, macOS:
```python
export FLASK_APP=hello.py
flask run  
```
Windows:
```python
set FLASK_APP=hello.py
flask run
```

http://localhost:5000/  
This loop continues until you stop the application by pressing Ctrl+C

Start also possible with:
```python
if __name__ == '__main__':
    app.run()
```

## Dynamic Routes
```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```

## Debug Mode
export FLASK_DEBUG=1  
To enable debug mode programmatically, use app.run(debug=True)

# Command-Line Options 

Options:  
  --version  Show the flask version  
  --help     Show this message and exit.  

Commands:  
  db       Perform database migrations.  
  deploy   Run deployment tasks.  
  profile  Start the application under the code...  
  routes   Show the routes for the app.  
  run      Run a development server.  
  shell    Run a shell in the app context.  
  test     Run the unit tests.    
  
```
(venv) $ flask run --host 0.0.0.0
 * Serving Flask app "hello"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```  

## The Request-Response Cycle

### request object
It encapsulates the HTTP request sent by the client.  

Flask context globals

Variable name | Context | Description 
------------- | ------- | ----------- 
current_app | Application context | The application instance for the active application.
g | Application context | An object that the application can use for temporary storage during the handling of a request. This variable is reset with each request.
request | Request context | The request object, which encapsulates the contents of an HTTP request sent by the client.
session | Request context | The user session, a dictionary that the application can use to store values that are “remembered” between requests.

If any of these variables are accessed without an active application or request context, an error is generated.

Table 2-2. Flask request object  

Attribute or Method | Description  
------------------- | -------------------------------  
form | A dictionary with all the form fields submitted with the request.
args | A dictionary with all the arguments passed in the query string of the URL.
values | A dictionary that combines the values in form and args.
cookies | A dictionary with all the cookies included in the request.
headers | A dictionary with all the HTTP headers included in the request.
files | A dictionary with all the file uploads included with the request.
get_data() | Returns the buffered data from the request body.
get_json() | Returns a Python dictionary with the parsed JSON included in the body of the request.
blueprint | The name of the Flask blueprint that is handling the request. 
endpoint | The name of the Flask endpoint that is handling the request. Flask uses the name of the view function as the endpoint name for a route.
method | The HTTP request method, such as GET or POST.
scheme | The URL scheme (http or https).
is_secure() | Returns True if the request came through a secure (HTTPS) connection.
host | The host defined in the request, including the port number if given by the client.
path | The path portion of the URL.query_stringThe query string portion of the URL, as a raw binary value.
full_path | The path and query string portions of the URL.
url | The complete URL requested by the client.
base_url | Same as url, but without the query string component.
remote_addr | The IP address of the client.
environ | The raw WSGI environment dictionary for the request.


```python
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```
Dieser Output funktioniert bei mir nicht. Ich bekomme folgende Fehlermeldung:  
```
Funktioniert bei mir nicht in der Python Console - Auch nicht in PyCharm
>>> 
(flasky) uwes@hpi5:/mnt/Volume/GitHub/flasky$ python
Python 3.8.1 (default, Feb 16 2020, 15:26:26) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from flasky import app
Python-dotenv could not parse statement starting at line 1
Python-dotenv could not parse statement starting at line 2
Python-dotenv could not parse statement starting at line 3
Python-dotenv could not parse statement starting at line 4
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'current_app' is not defined
```

# Request Hooks
hook | description
------------------ | ---------------------------------
before_request | Registers a function to run before each request.
before_first_request | Registers a function to run only before the first request is handled. This can be a convenient way to add server initialization tasks.
after_request | Registers a function to run after each request, but only if no unhandled exceptions occurred.
teardown_request | Registers a function to run after each request, even if unhandled exceptions occurred.  

###**share data** between request hook functions and view functions:  
use the g context global as storage.

# Responses
**make_response()** function takes one, two, or three arguments, the same values that can be returned from a view function, and returns an equivalent response object.   

Flask response object 

Attribute or Method | Description
------------------ | ---------------------------------
status_code | The numeric HTTP status code
headers | A dictionary-like object with all the headers that will be sent with the response
set_cookie() | Adds a cookie to the response
delete_cookie() | Removes a cookie
content_length | The length of the response body
content_type | The media type of the response body
set_data() | Sets the response body as a string or bytes value
get_data() | Gets the response body	Description
status_code | The numeric HTTP status code
headers |A dictionary-like object with all the headers that will be sent with the response
set_cookie() | Adds a cookie to the response
delete_cookie() | Removes a cookie
content_length | The length of the response body
content_type |The media type of the response body
set_data() | Sets the response body as a string or bytes value
get_data() | Gets the response body

# Chapter 3. Templates

Flask view functions have two completely independent purposes disguised as one, which creates a problem.  
These two types of tasks are formally called business logic and presentation logic, respectively.Mixing business and presentation logic leads to code that is hard to understand and maintain.  
Moving the presentation logic into templates helps improve the maintainability of the application.  
A template is a file that contains the text of a response, with placeholder variables for the dynamic parts that will be known only in the context of a request. The process that replaces the variables with actual values and returns a final response string is called rendering.  

## The Jinja2 Template Engine
### Rendering Templates
The function render_template() provided by Flask integrates the Jinja2 template engine with the application.  
### Variables
The **{{ name }}** construct used in the template shown in Example 3-2 references a variable, a special placeholder that tells the template engine that the value that goes in that place should be obtained from data provided at the time the template is rendered.  
Jinja2 recognizes variables of any type, even complex types such as lists, dictionaries, and objects.

Variables can be modified with **filters**, which are added after the variable name with a pipe character as separator.  

Jinja2 variable filters

Filter name | Description  
------------ | --------------  
safe | Renders the value without applying escaping
capitalize | Converts the first character of the value to uppercase and the rest to lowercase
lower | Converts the value to lowercase characters
upper | Converts the value to uppercase characters
title | Capitalizes each word in the value
trim | Removes leading and trailing whitespace from the value
striptags | Removes any HTML tags from the value before rendering  

## Control Structures
## Bootstrap Integration with Flask-Bootstrap
The extension is usually imported from a flask_<name> package, where <name> is the extension name. Most Flask extensions follow one of two consistent patterns for initialization.  
Once Flask-Bootstrap is initialized, a base template that includes all the Bootstrap files and general structure is available to the application.  
The Jinja2 extends directive implements the template inheritance by referencing **bootstrap/base.html** from Flask-Bootstrap. The base template from Flask-Bootstrap provides a skeleton web page that includes all the Bootstrap CSS and JavaScript files.  

Flask-Bootstrap’s base template blocks 

Block name | Description
----------- | -----------
doc | The entire HTML document
html_attribs | Attributes inside the \<html> tag  
html | The contents of the \<html> tag
head | The contents of the \<head> tag
title | The contents of the \<title> tag
metas | The list of \<meta> tags
styles | CSS definitions
body_attribs | Attributes inside the \<body> tag
body | The contents of the \<body> tag
navbar | User-defined navigation bar
content | User-defined page content
scripts | JavaScript declarations at the bottom of the document

If the application needs to add its own content to a block that already has some content, then **Jinja2’s super() function** must be used.

## Custom Error Pages
## own base templates
the application can define its own base template with a uniform page layout that includes the navigation bar and leaves the page content to be defined in derived templates.   

## Links
Any application that has more than one route will invariably need to include links that connect the different pages, such as in a navigation bar.  
URLs written explicitly create an unwanted dependency on the routes defined in the code. If the routes are reorganized, links in templates may break.  
Flask provides the **url_for()** helper function, which generates URLs from the information stored in the application’s URL map.  

**Relative URLs** are sufficient when generating links that connect the different routes of the application. **Absolute URLs** are necessary only for links that will be used outside of the web browser, such as when sending links by email.  

## Static Files
In its default configuration, Flask looks for static files in a subdirectory called static located in the application’s root folder.  


## Localization of Dates and Times with Flask-Moment
``` 
pip install flask-moment  
```
Flask-Moment assumes that timestamps handled by the server-side application are “naive” datetime objects expressed in UTC. See the documentation for the datetime package in the standard library for information on naive and aware date and time objects. 

# Chapter 4. Web Forms
With HTML, it is possible to create web forms, in which users can enter information. The form data is then submitted by the web browser to the server, typically in the form of a POST request. The Flask request object, introduced in Chapter 2, exposes all the information sent by the client in a request and, in particular for POST requests containing form data, provides access to the user information through request.form.  
The Flask-WTF extension makes working with web forms a much more pleasant experience. This extension is a Flask integration wrapper around the framework-agnostic WTForms package.  
```
(venv) $ pip install flask-wtf
```

## 
Flask-WTF does not need to be initialized at the application level, but it expects the application to have a secret key configured.  
 ```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

## Form Classes
The FlaskForm base class is defined by the Flask-WTF extension, so it is imported from flask_wtf. The fields and validators, however, are imported directly from the WTForms package.  

WTForms standard HTML fields 

Field type | Description
----------- | ------------
BooleanField | Checkbox with True and False values
DateField | Text field that accepts a datetime.date value in a given format
DateTimeField | Text field that accepts a datetime.datetime value in a given format
DecimalField | Text field that accepts a decimal.Decimal value
FileField | File upload field
HiddenField | Hidden text field
MultipleFileField | Multiple file upload field
FieldList | List of fields of a given type
FloatField | Text field that accepts a floating-point value
FormField | Form embedded as a field in a container form
IntegerField | Text field that accepts an integer value
PasswordField | Password text field
RadioField | List of radio buttons
SelectField | Drop-down list of choices
SelectMultipleField | Drop-down list of choices with multiple selection
SubmitField | Form submission button
StringField | Text field
TextAreaField | Multiple-line text field

WTForms validators Validator | Description
-----------------------------|------------
DataRequired | Validates that the field contains data after type conversion
Email | Validates an email address
EqualTo | Compares the values of two fields; useful when requesting a password to be entered twice for confirmation
InputRequired | Validates that the field contains data before type conversion
IPAddress | Validates an IPv4 network address
Length | Validates the length of the string entered
MacAddress | Validates a MAC address
NumberRange | Validates that the value entered is within a numeric range
Optional | Allows empty input in the field, skipping additional validators
Regexp | Validates the input against a regular expression
URL | Validates a URL
UUID | Validates a UUID
AnyOf | Validates that the input is one of a list of possible values
NoneOf | Validates that the input is none of a list of possible values  

## HTML Rendering of Forms
```jinja2
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```
Note that in addition to the name and submit fields, the form has a form.hidden_tag() element. This element defines an extra form field that is hidden, used by Flask-WTF to implement CSRF protection.  

The Flask-Bootstrap extension provides a high-level helper function that renders an entire Flask-WTF form using Bootstrap’s predefined form styles, all with a single call. Using Flask-Bootstrap, the previous form can be rendered as follows:  
```jinja2
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```
## Form Handling in View Functions
A form view function will have two tasks. First it will render the form, and then it will receive the form data entered by the user.  

## Redirects and User Sessions
### Post/Redirect/Get pattern.
Consequently, it is considered good practice for web applications to never leave a POST request as the last request sent by the browser.This is achieved by responding to POST requests with a redirect instead of a normal response.   

## Message Flashing
Calling flash() is not enough to get messages displayed; the templates used by the application need to render these messages. The best place to render flashed messages is the base template, because that will enable these messages in all pages. Flask makes a get_flashed_messages() function available to templates to retrieve the messages and render them  

# Chapter 5 Databases
## Database Operations
Flask-SQLAlchemy database URLs  

Database engine | URL
--------------- | --------
MySQL | mysql://username:password@hostname/database
Postgres | postgresql://username:password@hostname/database
SQLite (Linux, macOS) | sqlite:////absolute/path/to/database
SQLite (Windows) | sqlite:///c:/absolute/path/to/database

In these URLs, hostname refers to the server that hosts the database service, which could be localhost or a remote server.  

**SQLite databases** do not have a server, so hostname, username, and password are omitted and database is the filename on disk for the database.  

The db object instantiated from the class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.  

## Model Definition
The term model is used when referring to the persistent entities used by the application. In the context of an ORM, a model is typically a Python class with attributes that match the columns of a corresponding database table.

Flask-SQLAlchemy requires all models to define a primary key column, which is commonly named id.  

## Most common SQLAlchemy column types
 
Type name | Python type | Description
--------- | ----------- | ------------
Integer | int | Regular integer, typically 32 bits
SmallInteger | int | Short-range integer, typically 16 bits
BigInteger | int or long | Unlimited precision integer
Float | float | Floating-point number
Numeric | decimal.DecimalFixed-point number
String | str | Variable-length string
Text | str | Variable-length string, optimized for large or unbounded length
Unicode | unicode | Variable-length Unicode string
UnicodeText | unicode | Variable-length Unicode string, optimized for large or unbounded length
Boolean | bool | Boolean value
Date | datetime.date | Date value
Time | datetime.time | Time value
DateTime | datetime.datetime | Date and time value
Interval | datetime.timedelta | Time interval
Enum | str | List of string values
PickleType | Any Python object | Automatic Pickle serialization
LargeBinary | str | Binary blob

Most common SQLAlchemy column options
 
Option name | Description
----------- | -----------
primary_key | If set to True, the column is the table’s primary key.
unique | If set to True, do not allow duplicate values for this column.
index | If set to True, create an index for this column, so that queries are more efficient.
nullable | If set to True, allow empty values for this column. If set to False, the column will not allow null values.
default | Define a default value for the column.

## Relationships

### Common SQLAlchemy relationship options

Option name | Description
----------- | -----------
backref | Add a back reference in the other model in the relationship.
primaryjoin | Specify the join condition between the two models explicitly. This is necessary only for ambiguous relationships.
lazy | Specify how the related items are to be loaded. Possible values are select (items are loaded on demand the first time they are accessed), immediate (items are loaded when the source object is loaded), joined (items are loaded immediately, but as a join), subquery (items are loaded immediately, but as a subquery), noload (items are never loaded), and dynamic (instead of loading the items, the query that can load them is given).
uselist | If set to False, use a scalar instead of a list.
order_by | Specify the ordering used for the items in the relationship.
secondary | Specify the name of the association table to use in many-to-many relationships.
secondaryjoin | Specify the secondary join condition for many-to-many relationships when SQLAlchemy cannot determine it on its own.

## Database Operations
most common database operations in a shell started with the flask shell command:

## Querying Rows
Role.query.all()  
User.query.all()  
User.query.filter_by(role=user_role).all()  
user_role = Role.query.filter_by(name='User').first()  

### Common SQLAlchemy query filters

Option      | Description
----------- | -----------
filter() | Returns a new query that adds an additional filter to the original query
filter_by() | Returns a new query that adds an additional equality filter to the original query
limit() | Returns a new query that limits the number of results of the original query to the given number
offset() | Returns a new query that applies an offset into the list of results of the original query
order_by() | Returns a new query that sorts the results of the original query according to the given criteria
group_by() | Returns a new query that groups the results of the original query according to the given criteria

### Most common SQLAlchemy query executors

Option      | Description
----------- | -----------
all() | Returns all the results of a query as a list
first() | Returns the first result of a query, or None if there are no results
first_or_404() | Returns the first result of a query, or aborts the request and sends a 404 error as the response if there are no results
get() | Returns the row that matches the given primary key, or None if no matching row is found
get_or_404() | Returns the row that matches the given primary key or, if the key is not found, aborts the request and sends a 404 error as the response
count() | Returns the result count of the query
paginate() | Returns a Pagination object that contains the specified range of results

## 8. User Authentication
### Authentication Extensions for Flask


    Flask-Login: Management of user sessions for logged-in users
    Werkzeug: Password hashing and verification
    itsdangerous: Cryptographically secure token generation and verification
In addition to authentication-specific packages, the following general-purpose extensions will be used:
    Flask-Mail: Sending of authentication-related emails
    Flask-Bootstrap: HTML templates
    Flask-WTF: Web forms

### Password Security
Hashing Passwords with Werkzeug  
generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)  
check_password_hash(hash, password)  

### Creating an Authentication Blueprint

### User Authentication with Flask-Login
Preparing the User Model for Logins  

Flask-Login required items

Property/method Option | Description
---------------------- | -----------
is_authenticated | Must be True if the user has valid login credentials or False otherwise.
is_active | Must be True if the user is allowed to log in or False otherwise. A False value can be used for disabled accounts.
is_anonymous | Must always be False for regular users and True for a special user object that represents anonymous users.
get_id() | Must return a unique identifier for the user, encoded as a Unicode string.

These properties and methods can be implemented directly in the model class, but as an easier alternative Flask-Login provides a **UserMixin** class that has default implementations that are appropriate for most cases.  
Flask-Login is initialized in the application factory function,  
The **login_manager.user_loader decorator** is used to register the function with Flask-Login, which will call it when it needs to retrieve information about the logged-in user.  
 
### Protecting Routes
@login_required
Thanks to the login_required decorator, if this route is accessed by a user who is not authenticated, Flask-Login will intercept the request and send the user to the login page instead.  

### Adding a Login Form
