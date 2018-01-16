# minimal-flask-example
The simplest complex example that I can think of to show main Flask app concepts.

# example 1

The first example is `app.py`. In this example, I show you how to embed a `pandas.DataFrame()` table inside an HTML page served up using Flask.

Key concepts here:

- Jinja2 templating: (`{{ variable_name }}` syntax)
- Template inheritance: (`{% extends "parent.html" %}`)
- Styling with Bootstrap CSS
- Marking strings as safe to render: (`{{ string|safe }}`)

# example 2

The second example is `display_bokeh.py`. In this example, I show you how to embed a Bokeh plot on an HTML page served up using Flask.

Key concepts here:

- Marking strings as safe to render (see above)
- Refactoring granular logic into a utility function, so that only application "business logic" remains.

# notes

- Watch out for BokehJS, BokehCSS and Bokeh.py versioning. Make sure the Bokeh versions in `data.html` are the same as the Bokeh version installed locally.