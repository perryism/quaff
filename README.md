# Quick start

<pre>
# Assume we already have some functionality implemented in the system
def add(x, y):
    return x + y

# We can create an endpoint quickly, and it will look up the inputs in query string or form variables
@quaff(flask_app, "/add")
def add_api(y: int = 0, x: int = 0):
    return add(x, y)
</pre>
