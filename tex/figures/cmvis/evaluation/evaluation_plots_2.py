from pandas.io.parsers import read_csv
from pylab import *
import numpy as np

colors = ['#27B86F', '#248CC0', '#DF9F02', '#C01315']
captions = ['Color Overlay', 'Fuzziness', 'Chroma']
scala = ['-2', '-1', 'neutral', '+1', '+2']
ind = np.arange(5)

# Helpful to find anatomy faster:
helpful_faster = [
	[0,2,6,2,2], [0,0,7,3,2], [0,0,4,4,4]
]

# Intuitiveness
intuitiveness = [
	[0,0,2,0,10], [0,1,5,4,3], [0,0,0,6,7]
]

def create_plot(dataset, plot_title, filename):
	figure()
	suptitle(plot_title)

	for index, i in enumerate([0,2,1]):
		ax = subplot(311+index)
		title(captions[i])

		ax.bar(ind, dataset[i], 1, color=colors[0])

		ax.set_xticks(ind+0.5)
		ax.set_xticklabels(scala)
		ax.set_ylim(0, 10)
		subplots_adjust(hspace=0.5)

	subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)
	savefig(filename, dpi=300)
	show()


create_plot(helpful_faster, 'Does the visualization help to find anatomical structures faster?', 'helpful_to_find_anatomy.png')
create_plot(intuitiveness, 'How intuitive is the visualization?', 'intuitiveness.png')
