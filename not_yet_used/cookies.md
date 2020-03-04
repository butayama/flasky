Useage of cookies in RESTful Web Services with Flask
====================================================
source: https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch14.html

The current login functionality implemented with the help of Flask-Login stores data in the user session, which Flask stores by default in a client-side cookie, so the server does not store any user-related information; it asks the client to store it instead. It would appear that this implementation complies with the stateless requirement of REST, but the use of cookies in RESTful web services falls into a gray area, as it can be cumbersome for clients that are not web browsers to implement them. For that reason, it is generally seen as a bad design choice to use cookies in APIs.  

NoteThe stateless requirement of REST may seem overly strict, but it is not arbitrary. Stateless servers can scale very easily. If servers store information about clients, it is necessary to ensure that the same server always gets requests from a given client, or else to use shared storage for client data. Both are complex problems to solve that do not exist when the server is stateless.  

