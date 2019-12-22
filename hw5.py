import numpy as np, matplotlib.pyplot as plt, glob, os
import IPython.display as IPdisplay, matplotlib.font_manager as fm
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D
from PIL import Image

title_font = fm.FontProperties(family='DejaVu Sans', style='normal', size=20, weight='normal', stretch='normal')

print("Please input directory to save gif with attractor")
save_folder = str(input())
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

initial_state = [0., 1., 1.01]
sigma = 10.
rho = 28.
beta = 2.667
start_time = 0
end_time = 100
interval = 100
time_points = np.linspace(start_time, end_time, end_time * interval)


def lorenz_system(current_state, t):
    x, y, z = current_state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

def plot_lorenz(xyz, n):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.gca(projection='3d')
    ax.xaxis.set_pane_color((1, 1, 1, 1))
    ax.yaxis.set_pane_color((1, 1, 1, 1))
    ax.zaxis.set_pane_color((1, 1, 1, 1))
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    ax.plot(x, y, z, color='g', alpha=0.7, linewidth=0.7)
    ax.set_xlim((-30, 30))
    ax.set_ylim((-30, 30))
    ax.set_zlim((0, 50))
    ax.set_title('Lorenz system attractor', fontproperties=title_font)

    plt.savefig('{}/{:03d}.png'.format(save_folder, n), dpi=60, bbox_inches='tight', pad_inches=0.1)
    plt.close()

def get_chunks(full_list, size):
    size = max(1, size)
    chunks = [full_list[0:i] for i in range(1, len(full_list) + 1, size)]
    return chunks

chunks = get_chunks(time_points, size=20)

points = [odeint(lorenz_system, initial_state, chunk) for chunk in chunks]

for n, point in enumerate(points):
    plot_lorenz(point, n)

first_last = 100
standard_duration = 10
durations = tuple([first_last] + [standard_duration] * (len(points) - 2) + [first_last])

images = [Image.open(image) for image in glob.glob('{}/*.png'.format(save_folder))]
gif_filepath = save_folder + '/animated-lorenz-attractor.gif'

gif = images[0]
gif.info['duration'] = durations
gif.info['loop'] = 0
gif.save(fp=gif_filepath, format='gif', save_all=True, append_images=images[1:])

Image.open(gif_filepath).n_frames == len(images) == len(durations)

IPdisplay.Image(url=gif_filepath)