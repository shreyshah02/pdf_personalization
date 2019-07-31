from matplotlib.patches import Circle, Wedge
from matplotlib import patches
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effect


def gauge(fname, percAuto=50, labels=('Red', 'Yellow', 'Green'), colors=('#00aa41', '#F1BE48', '#c70f2e'), arrow=1, title='' ):
    fig, ax = plt.subplots()  # facecolor='#002B49'
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
        patches.append(Wedge((0., 0.), .4, *ang, width=.12, facecolor=c, lw = 2, alpha = 0.5, path_effects=[path_effect.withSimplePatchShadow(offset=(-2, -2))]))

    [ax.add_patch(p) for p in patches]

    pos = (100 - percAuto)/100 * 180
    ax.arrow(0, 0, 0.255*np.cos(np.radians(pos)), 0.255*np.sin(np.radians(pos)), width=0.006, head_width=0.03,
             head_length=0.1, fc='k', ec='k', path_effects=[path_effect.withSimplePatchShadow(offset=(-3, -3))], zorder=11)
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='k', path_effects=[path_effect.withSimplePatchShadow(offset=(-2, -2))], zorder=11))
    ax.add_patch(Circle((0, 0), radius=0.002, facecolor='w', path_effects=[path_effect.withSimplePatchShadow(offset=(-2, -2))], zorder=12))

    wedge = Wedge((0., 0.), 0.28, 0, 180, color='#002B49', zorder=10, fill=True, path_effects=[path_effect.withSimplePatchShadow(offset=(-2, -2))])
    ax.add_patch(wedge)
    ax.text(0, 0.115, str(percAuto)+'%', horizontalalignment='center', verticalalignment='center', fontsize=26, fontweight='bold', zorder=12, color='w')

    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    #ax.axes.set_facecolor('#002B49')
    #ax.axes.set_frame_on(True)
    plt.tight_layout()
    if fname:
        #fig.savefig(fname, dpi=200)
        plt.savefig(fname)
    #plt.show()


# AR = int(input('Enter the AR%: '))
# gauge(percAuto=AR, fname='test')


def gauge_cycle(days, avgDays):
    fig, ax = plt.subplots()  # facecolor='#002B49'
    xy = (0., 0.)
    if days < avgDays:
        color = '#00aa41'
    elif days == avgDays:
        color = '#F1BE48'
    else:
        color = '#c70f2e'

    fancybox = patches.FancyBboxPatch(xy, width=2, height=1, boxstyle='round', color=color,
                                      path_effects=[
                                          path_effect.withSimplePatchShadow(offset=(-4, -4), shadow_rgbFace='k')])
    ax.add_patch(fancybox)
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')
    plt.tight_layout()
    #ax.axes.set_facecolor('#002B49')
    #ax.axes.set_frame_on(True)
    plt.savefig('gauge.png')
