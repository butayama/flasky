/home/uwes/Pictures/Screenshot from 2020-03-06 12-50-57.png

# nav.html
```jinja2
<li class="nav-item"><a href="{{ url_for('post_op1') }}"    
    class="nav-link {% if index %}active{% endif %}">post_op1</a></li>
```

# nav_items.py
```python
from flask_nav.elements import Navbar, View
#....

class NavItems:
    topbar = Navbar('',
                    View('HOME', 'home.index'),
                    # ...
                    View('POST_OP1', 'home.post_op1'),
                    # ...
                    )
```
# home_views.py
```python
import flask

from ..infrastructure.view_modifiers import response
import app.services.angles_service as angles_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/post_op1')
@response(template_file='home/post_op1.html')
def post_op1():
    return {}
```
# routes.py
```python


@app.route("/post_op1")
def _post_op1():
    return render_template("home/post_op1.html", post_op1=True)
```
![Listing01](/home/uwes/Pictures/Screenshot from 2020-03-06 12-50-57.png)