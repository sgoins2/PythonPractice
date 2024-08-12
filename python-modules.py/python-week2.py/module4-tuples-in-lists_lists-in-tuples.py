# Creating tuples for three cities with their name, country code, and population (in millions)
city_1 = ('Tokyo', 'JPN', 13.96)
city_2 = ('Paris', 'FRN', 2.16)
city_3 = ('Budapest', 'HGR', 1.78)

# Creating a list of tuples, each representing a capital city with name, country code, and population (in millions)
capitals = [('Tokyo', 'JPN', 8.87), ('Paris', 'FRN', 10.1), ('Budapest', 'HGR', 5.7)]

# Iterating over the list of capitals
for capital in capitals:
    # Printing the name, country code, and population of each capital
    print('Name:', capital[0], 'Country:', capital[1], 'Population:', capital[2])