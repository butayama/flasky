https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html
# application instance
object of class Flask  
The web server passes all requests it receives from clients to this object for handling, using a protocol called Web Server Gateway Interface (WSGI, pronounced “wiz-ghee”)
```python
from flask import Flask
app = Flask(__name__)
```

# routes - view functions
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

# app.route decorator
defines a defines a route that has a dynamic component  
```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```
when the view function is invoked, the dynamic component will be passed as an argument  

# Development Web Server
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

# Dynamic Routes
```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```

# Debug Mode
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

# The Request-Response Cycle

## request object
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

