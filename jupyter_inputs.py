'''
	- This code is to be run inside of the python interpreter (Jupyter Notebook)
	- The first line imports both matplotlib and NumPy modules
	- The second and third line are for the data visualization libraries
	- Tutorials followed: https://www.youtube.com/watch?v=Q73ADVZCqSU
						  https://www.youtube.com/watch?v=a9UrKTVEeZA
'''
%pylab inline 
import pandas 
import seaborn

'''
 - this will load the csv into the pandas dataframe which is a python object
 - the file path will differ depending on where you saved the csv
'''
data = pandas.read_csv('Documents/Github_Projects/data_analysis/wyoming_2017.csv')

# to check if the data saved correctly call on the data variable by printing out data
data

# plots location combined population and male population
plt.plot(data.Geography, data.combined_pop_ages_15to44, data.male_pop_age15to44)

# plots locationed combined population and female population
plt.plot(data.Geography, data.combined_pop_ages_15to44, data.female_pop_age15to44)

# creates legend labels for line reference
plt.legend(['Baseline', 'Male', 'Combined', 'Female'])

# sets x axis label to county
plt.xlabel('County')

# sets y axis label to population size
plt.ylabel('Population Size')

# var set to rotate county labels to prevent names overlapping 
label_rotate = [plt.xticks(rotation=90)]

# shows the plotted chart
plt.show()