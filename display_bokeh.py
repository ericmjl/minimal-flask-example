# Another example chaining Bokeh's to Flask.

from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure
from bokeh.embed import components
from flask import Flask, render_template

app = Flask(__name__)

def make_plot():
    colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    colors = [colormap[x] for x in flowers['species']]

    p = figure(title = "Iris Morphology")
    p.xaxis.axis_label = 'Petal Length'
    p.yaxis.axis_label = 'Petal Width'

    p.circle(flowers["petal_length"], flowers["petal_width"],
             color=colors, fill_alpha=0.2, size=10)

    return p


@app.route('/')
def main():
    figure = make_plot()
    fig_script, fig_div = components(figure)

    return render_template('data.html', fig_script=fig_script, fig_div=fig_div)


if __name__ == '__main__':
    app.run(debug=True, port=5678)
