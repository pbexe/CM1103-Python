from questions_1_and_2 import theoreticalMeanQueueLength, singleQueue
import numpy as np
import matplotlib as mpl
mpl.use('pgf')

def figsize(scale):
    fig_width_pt = 512.14963                          # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width/2,fig_height/2]
    return fig_size

pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10/2,               # LaTeX default is 10pt font.
    "font.size": 10/2,
    "legend.fontsize": 8/2,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8/2,
    "ytick.labelsize": 8/2,
    "lines.linewidth": 0.6,
    "figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt

# I make my own newfig and savefig functions
def newfig(width):
    plt.clf()
    fig = plt.figure(figsize=figsize(width))
    ax = fig.add_subplot(111)
    plt.gcf().subplots_adjust(bottom=0.15)
    return fig, ax

def savefig(filename):
    plt.savefig('{}.pgf'.format(filename))
    plt.savefig('{}.pdf'.format(filename))


# Simple plot
fig, ax  = newfig(1)

beta = np.arange(0, 1, 0.01)
y = []
for i in beta:
    y.append(theoreticalMeanQueueLength(1,i))

ax.plot(beta, y)
ax.set_xlabel(r'Mean time of customer interaction $(\beta$ minutes)')
ax.set_ylabel('Mean Queue Length')

savefig('./figs/theoretical')