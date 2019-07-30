from matplotlib.patches import Circle, Wedge, Rectangle, Arrow
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effect


def gauge(fname, percAuto=50, labels=('Red', 'Yellow', 'Green'), colors=('#00aa41', '#F1BE48', '#c70f2e'), arrow=1, title='' ):
    fig, ax = plt.subplots()
    N= len(labels)
    ang_range = [(0, 90), (90, 126), (126, 180)]
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

    # r = Rectangle((-0.4, -0.1,), 0.8, 0.1, facecolor='b', lw =2)
    # ax.add_patch(r)
    # ax.text(0, -0.05, percAuto, horizontalalignment='center', verticalalignment='center', fontsize=22, fontweight='bold')

    pos = (100 - percAuto)/100 * 180
    ax.arrow(0, 0, 0.255*np.cos(np.radians(pos)), 0.255*np.sin(np.radians(pos)), width=0.006, head_width=0.03,
             head_length=0.1, fc='k', ec='k', path_effects=[path_effect.withSimplePatchShadow(offset=(1, 4))], zorder=11)
    #ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k', zorder=11))
    #ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    wedge = Wedge((0., 0.), 0.3, 0, 180, color='#002B49', zorder=10, fill=True, path_effects=[path_effect.withSimplePatchShadow(offset=(-2, -2))])
    ax.add_patch(wedge)
    ax.text(0, 0.12, str(percAuto)+'%', horizontalalignment='center', verticalalignment='center', fontsize=22, fontweight='bold', zorder=12, color='w')

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

# AR = int(input('Enter the AR%: '))
# fig = gauge(percAuto=AR, fname='test')
# fig.show()