
# deleting specific items from a list

top_cities = ['New York City','Los Angeles','Chicago','Baton Rouge','Houston','Miami','Atlanta','Paris']
del top_cities[3]
print(top_cities)


##############################################

# deleting a slice

# example 1
top_cities = ['New York City','Los Angeles','Chicago','Baton Rouge','Houston','Miami','Atlanta','Paris']
del top_cities[:3]
print(top_cities)

# example 2
top_cities = ['New York City','Los Angeles','Chicago','Baton Rouge','Houston','Miami','Atlanta','Paris']
del top_cities[4:]
print(top_cities)

#example 3
top_cities = ['New York City','Los Angeles','Chicago','Baton Rouge','Houston','Miami','Atlanta','Paris']
del top_cities[:]
print(top_cities)