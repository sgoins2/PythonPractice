# iterating a list 

# example 1

top_cities = ['New York City','Los Angeles','Chicago','Houston','Miami','Atlanta']
for city_index in range(len(top_cities)):
    print('Current Index:', city_index ,'| Current City:', top_cities[city_index], )

# example 2

spendings = [25.0, 32.76, 15.63, 24.12, 83.62] 
sum = 0.0
for costs in spendings:
    sum += costs
print('Money Spent:', '$',sum)    
        
