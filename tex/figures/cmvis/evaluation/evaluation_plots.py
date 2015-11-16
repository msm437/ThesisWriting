from pandas.io.parsers import read_csv
from pylab import *
import numpy as np

colors = ['#27B86F', '#248CC0', '#DF9F02', '#C01315']
captions = ['Color Overlay', 'Fuzziness', 'Chroma']
scala = ['Not at all', 'Somewhat', 'Very Much']
ind = np.arange(3)

# Helpful to learn US:
helpful_to_learn_us = [
	[1,4,8], [6,2,5], [2,1,10]
]

# Helpful to understand uncertainty:
helpful_to_understand_uncertainty = [
	[0,4,9], [3,4,6], [0,3,10]
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


create_plot(helpful_to_learn_us, 'Does it help to learn US/understand the US image formation process?', 'helpful_to_learn_us.png')
create_plot(helpful_to_understand_uncertainty, 'Does it help to understand the concept of uncertainty?', 'helpful_to_understand_uncertainty.png')
