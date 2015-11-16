from pandas.io.parsers import read_csv
from pylab import *

iterations = [20, 50, 80, 110]
colors = ['#27B86F', '#248CC0', '#DF9F02', '#C01315']
padding = 0.0
figuresize = (8, 5.5)

def load_data(folder, size, iterations, suffix=''):
	filename = '%s/cmCuda_512_5000---cmCuda_%i_%i%s.csv' % (folder, size, iterations, suffix)
	return read_csv(filename, header=0, skipinitialspace=True)

def create_plot(folder, sizes, iterations, variable, filename):
	figure(figsize=figuresize)

	# Load first dataset just to get number of entry
	data = load_data(folder, sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	subplots_adjust(left=0.125, right=0.95, top=0.925, bottom=0.125)

	for size in sizes:
		for i, cg_iterations in enumerate(iterations):
			data = load_data(folder, size, cg_iterations)
			plot(t, data[variable], linewidth=1, color=colors[i], label=('%i iterations' % cg_iterations))

	# Draw reference (where the previous solution is discarded)
	try:
		data = load_data(folder, size, cg_iterations, '_reset')
		plot(t, data[variable], linewidth=1, linestyle="--", dashes=(4,1), color=colors[i], label=('%i iterations (discarding previous result)' % cg_iterations))
	except: pass

	grid()
	title('PCG Iterations vs. SSIM')
	legend(loc='lower center', prop={'size':11})
	ylabel('Structural Similarity')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)
	show()

def create_plot3ssim(folder, sizes, iterations, variable, filename):
	figure(figsize=figuresize)


	# Load first dataset just to get number of entry
	data = load_data(folder, sizes[0], iterations[0])
	datapoints = len(data)

	t = arange(0.0, datapoints/30.0, 1.0/30.0)
	xlim(0.0-padding,datapoints/30.0+padding)
	subplots_adjust(left=0.125, right=0.95, top=0.925, bottom=0.125)

	for i in [0, 1, 2]:
		size = sizes[i]
		cg_iterations = iterations[i]
		data = load_data(folder, size, cg_iterations)
		plot(t, data[variable], linewidth=1, color=colors[i], label=('30ms, %i iterations' % cg_iterations + ', resample scale %s' % (size / 512)))

	grid()
	title('PCG Iterations/Resample Scale vs. SSIM')
	legend(loc='lower center', prop={'size':11})
	ylabel('Structural Similarity')
	xlabel('Image Sequence (seconds)')

	savefig(filename, dpi=300)
	show()
	
create_plot('cm_stuff', [256], iterations, 'MinSSIM', 'kidney_iterations_vs_minssim_0.50.png')
create_plot('gullbladder', [256], iterations, 'MinSSIM', 'gullbladder_iterations_vs_minssim_0.50.png')

create_plot3ssim('cm_stuff', [256, 384, 512], [100, 50, 30], 'MinSSIM', 'kidney_minssim_30ms.png')
create_plot3ssim('gullbladder', [256, 384, 512], [100, 50, 30], 'MinSSIM', 'gullbladder_minssim_30ms.png')

