from matplotlib.patches import Circle, Wedge, Rectangle, Arrow
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import os, sys


def gauge(percAuto = 50, labels=['Red', 'Yellow', 'Green'], colors='jet_r', arrow=1, title='', fname=False):
    fig, ax = plt.subplots()
    N= len(labels)
    ang_range = [(0, 54), (54, 90), (90, 180)]
    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arrange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list):
        if len(colors) == N:
            colors = colors[::-1]

    patches = []
    for ang, c in zip(ang_range, colors):
        patches.append(Wedge((0., 0.), .4, *ang, width=.10, facecolor=c, lw = 2, alpha = 0.5))

    [ax.add_patch(p) for p in patches]

    r = Rectangle((-0.4, -0.1,), 0.8, 0.1, facecolor='b', lw =2)
    ax.add_patch(r)
    ax.text(0, -0.05, title, horizontalalignment='center', verticalalignment='center', fontsize=22, fontweight='bold')

    pos = (100 - percAuto)/100 * 180
    ax.arrow(0, 0, 0.225*np.cos(np.radians(pos)), 0.225*np.sin(np.radians(pos)), width=0.04, head_width=0.09,
             head_length=0.1, fc='k', ec='k')
    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.tight_layout()
    if fname:
        #fig.savefig(fname, dpi=200)
        plt.savefig(fname)
    #plt.show()
    return fig


fig = gauge(percAuto=20, colors=['#00aa41', '#F1BE48', '#c70f2e'], title='86%', fname='test.png')
fig.show()