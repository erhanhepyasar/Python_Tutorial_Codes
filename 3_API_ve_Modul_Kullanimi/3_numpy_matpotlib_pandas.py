################################################################
# Create an array containing 250 random floats between 0 and 5
################################################################
# import numpy
#
# x = numpy.random.uniform(0.0, 5.0, 250)
#
# print(x)


################################################################
# Draw a histogram
################################################################
# import numpy
# import matplotlib.pyplot as plt
#
# x = numpy.random.uniform(0.0, 5.0, 250)
#
# plt.hist(x, 5)
# plt.show()

################################################################
# A typical normal data distribution
################################################################
# import numpy
# import matplotlib.pyplot as plt
#
# x = numpy.random.normal(5.0, 1.0, 100000)
#
# plt.hist(x, 100)
# plt.show()

################################################################
# Use the scatter() method to draw a scatter plot diagram
################################################################
# import matplotlib.pyplot as plt
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
# plt.scatter(x, y)
# plt.show()

################################################################
# Predict the speed of a 10 years old car
################################################################
# from scipy import stats
#
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
# def myfunc(x):
#   return slope * x + intercept
#
# speed = myfunc(10)
#
# print(speed)

################################################################
# Pandas ile csv dosyası okuma
################################################################
# import pandas
# from sklearn import linear_model
#
# df = pandas.read_csv("cars.csv")
#
# X = df[['Weight', 'Volume']]
# y = df['CO2']
#
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
#
# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300ccm:
# predictedCO2 = regr.predict([[2300, 1300]])
#
# print(predictedCO2)
# We have predicted that a car with 1.3 liter engine,
# and a weight of 2300 kg, will release approximately
# 107 grams of CO2 for every kilometer it drives.