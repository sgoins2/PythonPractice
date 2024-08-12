# Example 1: Accessing values in a dictionary

# Define a dictionary with players and their achievements
players = {
    'Michael Jordan': '6 time world champion',
    'Kobe Bryant': '5 time world champion',
    'LeBron James': '4 time world champion' 
}

# Print the achievement of Kobe Bryant
print(players['Kobe Bryant'])

###########################################################

# Example 2: Accessing values in a dictionary with numerical keys

# Define a dictionary with Olympic cities and their hosting years
olympic_cities = {
    2024: 'Paris, France',
    2020: 'Tokyo, Japan',
    2016: 'Rio de Janeiro, Brazil',
    2012: 'London, England'
}

# Print the city that hosted the Olympics in 2016
print(olympic_cities[2016])

###########################################################

# Example 3: Handling duplicate keys in a dictionary

# Define a dictionary with Olympic cities and their hosting years, including a duplicate key
olympic_cities = {
    2024: 'Paris, France',
    2020: 'Tokyo, Japan',
    2016: 'Rio de Janeiro, Brazil',
    2012: 'London, England',
    2012: 'Sydney, Australia'  # Duplicate key, the value will overwrite the previous entry
}

# Print the city that hosted the Olympics in 2012
print(olympic_cities[2012])
