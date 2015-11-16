from pandas.io.parsers import read_csv
from pylab import *
import numpy as np

colors = ['#27B86F', '#248CC0', '#DF9F02', '#C01315']
captions = ['Chroma', 'Fuzziness']
scala = ['-2', '-1', 'neutral', '+1', '+2']
ind = np.arange(5)

# Helpful to find anatomy faster:
uncertainty_perception = [
	[0,2,3,7,2], [0,0,0,7,7]
]

# diagnostic_value
diagnostic_value = [
	[2,2,4,4,2], [0,1,5,5,3]
]

def create_plot(dataset, plot_title, filename):
	figure(figsize=(8,4.5))
	suptitle(plot_title)

	for index, i in enumerate([0, 1]):
		ax = subplot(211+index)
		title(captions[i])

		ax.bar(ind, dataset[i], 1, color=colors[1])

		ax.set_xticks(ind+0.5)
		ax.set_xticklabels(scala)
		ax.set_ylim(0, 10)
		subplots_adjust(hspace=0.5)

	subplots_adjust(left=0.05, right=0.95, top=0.875, bottom=0.075)
	savefig(filename, dpi=300)
	show()


create_plot(uncertainty_perception, 'How intuitive is the visualization?', 'expert_uncertainty_perception.png')
create_plot(diagnostic_value, 'General diagnostic value', 'expert_diagnostic_value.png')
