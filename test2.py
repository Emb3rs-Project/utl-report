import mpld3
from mpld3 import plugins
from mpld3.utils import get_id
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")


N_paths = 5
N_steps = 100

x = np.linspace(0, 10, 100)
y = 0.1 * (np.random.random((N_paths, N_steps)) - 0.5)
y = y.cumsum(1)

fig, ax = plt.subplots()
labels = ["a", "b", "c", "d", "e"]
line_collections = ax.plot(x, y.T, lw=4, alpha=0.2)
interactive_legend = plugins.InteractiveLegendPlugin(line_collections, labels)
plugins.connect(fig, interactive_legend)


PLOTFIG = mpld3.fig_to_html(fig)


### REPORT_RENDERING_CODE [BEGIN]
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('asset'),
    autoescape=False
)

template = env.get_template('index.template_2.html')
template_content = template.render(plot=PLOTFIG)


f = open("index.html", "w")
f.write(template_content)
f.close()

output = {
    "every" : "thing",
    "else" : "yes",
    "report" : template_content
}