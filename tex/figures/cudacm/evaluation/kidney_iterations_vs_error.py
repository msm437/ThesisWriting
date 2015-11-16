from pandas.io.parsers import read_csv
from pylab import *

iterations = [20, 50, 80, 110]
colors = ['#27B86F', '#248CC0', '#DF9F02', '#C01315']
padding = 0.0
figuresize = (8, 5.5)

def load_data(folder, size, iterations, suffix=''):
	filename = '%s/size_%s__iterations_%i%s.csv' % (folder, size, iterations, suffix)
	return read_csv(filename, header=0, skipinitialspace=True)

def create_plot(sizes, iterations, variable, filename):
	figure(figsize=figuresize)

	# Load first dataset just to get number of entry
	data = load_data('kidney', sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	subplots_adjust(left=0.125, right=0.95, top=0.925, bottom=0.125)

	for size in sizes:
		for i, cg_iterations in enumerate(iterations):
			data = load_data('kidney', size, cg_iterations)
			plot(t, data[variable], linewidth=1, color=colors[i], label=('%i iterations' % cg_iterations))

	# Draw reference (where the previous solution is discarded)
	try:
		data = load_data('kidney', size, cg_iterations, '_reset')
		plot(t, data[variable], linewidth=1, linestyle="--", dashes=(4,1), color=colors[i], label=('%i iterations (discarding previous result)' % cg_iterations))
	except: pass

	grid()
	title('PCG Iterations vs. Error')
	legend(loc='upper center', prop={'size':11})
	ylabel('Error: $\|\|Lx-b\|\|_2$')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)
	show()

def create_plot2(sizes, iterations, variable, filename):
	figure(figsize=figuresize)

	# Load first dataset just to get number of entry
	data = load_data('kidney', sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	ylim(0.0, 50)

	for i, size in enumerate(sizes):
		for j, cg_iterations in enumerate(iterations):
			data = load_data('kidney', size, cg_iterations)
			plot(t, data[variable], linewidth=1, color=colors[j], label=('%s iterations' % cg_iterations))

	grid()
	title('Image Size and PCG Iterations vs. Runtime')
	legend(loc='upper right')
	ylabel('Runtime (ms)')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)


def create_plot3error(sizes, iterations, variable, filename):
	figure(figsize=figuresize)


	# Load first dataset just to get number of entry
	data = load_data('kidney', sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	subplots_adjust(left=0.125, right=0.95, top=0.925, bottom=0.125)

	for i in [0, 1, 2]:
		size = sizes[i]
		cg_iterations = iterations[i]
		data = load_data('kidney', size, cg_iterations)
		plot(t, data[variable], linewidth=1, color=colors[i], label=('30ms, %i iterations' % cg_iterations + ', resample scale %s' % size))

	grid()
	title('PCG Iterations/Resample Scale vs. Error')
	legend(loc='upper center', prop={'size':11})
	ylabel('Error: $\|\|Lx-b\|\|_2$')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)
	show()

def create_plot3time(sizes, iterations, variable, filename):
	figure(figsize=figuresize)


	# Load first dataset just to get number of entry
	data = load_data('kidney', sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	subplots_adjust(left=0.125, right=0.95, top=0.925, bottom=0.125)

	for i in [0, 1, 2]:
		size = sizes[i]
		cg_iterations = iterations[i]
		data = load_data('kidney', size, cg_iterations)
		plot(t, data[variable], linewidth=1, color=colors[i], label=('%i iterations' % cg_iterations + ', resample scale %s' % size))

	grid()
	title('PCG Iterations/Resample Scale vs. Runtime')
	legend(loc='upper center', prop={'size':11})
	ylabel('Runtime (ms)')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)
	show()

create_plot([0.50], iterations, 'solverError', 'kidney_iterations_vs_error_0.50.png')
#create_plot([0.75], iterations, 'solverError', 'kidney_iterations_vs_error_0.75.png')
#create_plot2([0.5], iterations, 'solverExecutionTime', 'cg_solver_time_0.50.png')
#create_plot2([0.75], iterations, 'solverExecutionTime', 'cg_solver_time_0.75.png')
#create_plot2([0.5], iterations, 'totalExecutionTime', 'cg_total_time_0.50.png')
#create_plot2([0.75], iterations, 'totalExecutionTime', 'cg_total_time_0.75.png')

create_plot3error([0.5, 0.75, 1], [100, 50, 30], 'solverError', 'error_30ms.png')
create_plot3time([0.5, 0.75, 1], [100, 50, 30], 'totalExecutionTime', 'runtime_30ms.png')
#create_plot3([0.5, 0.75, 1], [100, 50, 30], 'totalExecutionTime', 'cg_total_time_40.png')

