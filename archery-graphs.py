# -*- encoding: utf8 -*-
import clipboard
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from math import ceil
from statistics import mean

indata = clipboard.get()
all_series = []
all_dates = []

title = indata.split('\n')[0]
for line in indata.split('\n'):
	if '-' in line:
		# remove commas and split string on space
		serie = line.rstrip().replace(',','').split(' ')
		# move dates to new list
		all_dates.append(str(serie.pop(0)))
		# convert list elements to integers
		all_series.append(list(map(int, serie)))
		
plt.boxplot((all_series), notch=False, sym="o")
plt.title(title)
plt.show()

for plot_no, serie in enumerate(all_series, start = 1):
	# Lines: no of graphs / 3 rounded up, Columns: 3, current plot number
	plt.subplot(ceil(len(all_series) / 3.0), 3, plot_no)
	plt.xlim(1,len(serie))
	plt.ylim(0, 30)
	date = all_dates[plot_no - 1]
	title = "%s --> %d" % (date, mean(serie) * 10)
	plt.title(title)
	plt.scatter(range(1,len(serie) + 1), serie, marker='x')

plt.tight_layout()
plt.show()
