# minimal-flask-example

The simplest complex example that I can think of to show main Flask app concepts.

All examples are in `app.py`. There are 3 view functions embedded, each showing a different example of how to build Flask apps.

Key concepts applicable throughout:

- View functions
- Routes
- Returning a template.

## example 1

The first example is under [`/df`](http://minimal-flask-table.herokuapp.com/df). In this example, I show you how to embed a `pandas.DataFrame()` table inside an HTML page served up using Flask, essentially as a dump of the table.

Key concepts here:

- Jinja2 templating: (`{{ variable_name }}` syntax)
- Template inheritance: (`{% extends "parent.html" %}`)
- Styling with Bootstrap CSS
- Marking strings as safe to render: (`{{ string|safe }}`)

## example 2

The second example is under [`/dfcustom`](http://minimal-flask-table.herokuapp.com/dfcustom). In this example, I show you how to apply custom formatting to a DataFrame rendered as an HTML table.

Key concepts here, building on top of example 1:

- Jinja2 syntax is very Python-like.
- Macros behave like Python functions.
- Looping is very Pythonic.

## example 3

The second example is [`/bokehplot`](http://minimal-flask-table.herokuapp.com/bokehplot). In this example, I show you how to embed a Bokeh plot on an HTML page served up using Flask.

Key concepts here:

- Marking strings as safe to render (see above)
- Refactoring granular logic into a utility function, so that only application "business logic" remains.
- It is possible to cleverly pass strings around so that you can keep things like versioning automatically correct.
