#assigning variables

city1 = 'New York City'
city2 = 'Los Angeles'
city3 = 'Chicago'
city4 = 'Houston'
city5 = 'Miami'
city6 = 'Atlanta'

############################

#creating a list

top_cities = ['New York City','Los Angeles','Chicago','Houston','Miami','Atlanta']
print(top_cities)

############################

#indexing a list

#example1
top_cities[3]
# Houston

#example2
top_cities[-5]
# Los Angeles

#example3
top_cities[0]
# New York City

############################

#slicing a list

#example1
top_cities[2:6]
# 'Chicago','Houston','Miami','Atlanta'

#example2
top_cities[:3]
# 'New York City','Los Angeles','Chicago'

#example3
top_cities[4:]
# 'Miami','Atlanta'

#example4
top_cities[:]
#'New York City','Los Angeles','Chicago','Houston','Miami','Atlanta'