from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs = np.array([1, 2, 3, 4, 5, 6])
#ys = np.array([5, 22, 16, 32, 40, 35])

def create_dataset(hm, variance, step=2, correlation=False):
	val = 1
	ys = []
	for i in range(hm):

		y = val + random.randrange(-variance, variance)
		ys.append(y)

		if correlation and correlation=='positive':
			val = val + step

		elif correlation and correlation=='negative':
			val = val - step

	xs = [i for i in range(len(ys))]

	return np.array(ys, dtype=np.float64), np.array(xs, dtype=np.float64)

xs, ys = create_dataset(50, 66, 2, correlation='positive')

def best_fit_slope(xs, ys):

	m = ((mean(xs) * mean(ys)) - mean(xs * ys)) / (mean(xs)**2 - mean(xs**2))

	return m

m = best_fit_slope(xs, ys)


def best_fit_line(xs, ys):

	b = mean(ys) - (m*mean(xs))

	return b

b = best_fit_line(xs, ys)

def squared_error(ys_original, ys_line):

	return sum((ys_line-ys_original)**2)

def coefficient_of_determination(ys_original, ys_line):

	y_mean_line = [mean(ys_original) for y in ys_original]
	squared_error_regression = squared_error(ys_original, ys_line)
	squared_error_mean = squared_error(ys_original, y_mean_line)
	return 1-(squared_error_regression/squared_error_mean)

regression_line = [(m*x) + b for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

predict_x = 8
predict_y = (m*predict_x)+b

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()

