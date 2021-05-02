import seaborn as sns; sns.set_theme()
import numpy as np
import matplotlib.pyplot as plt
from math import floor


def generate_heatmap(x_data, y_data,  file_path = None) -> None:
	ax = sns.kdeplot(x=x_data, y=y_data,fill=True, thresh=0, levels=100, cmap="mako")
	if file_path is not None:
		ax.savefig(file_path)

if __name__ == '__main__':
	x = np.random.uniform(low=1, high=128, size=(100,))
	y = np.random.uniform(low=1, high=256, size=(100,))
	generate_heatmap(x, y)