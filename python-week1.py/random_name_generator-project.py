# Output the number of names to EC2 instances:

import random
employees = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", 
             "Christopher", "Daniel", "Matthew", "Anthony", "Mark","Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", 
             "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Margaret", "Betty", "Sandra"]

ec2_instances = int(input('How many EC2 instances do you want named? '))
print(random.sample(employees, ec2_instances ))


############################################################

#concat department to the names

import random

# List of employees
employee_list = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", 
                 "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Mary", "Patricia", "Jennifer", "Linda", 
                 "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Margaret", "Betty", 
                 "Sandra"]

# Get user input for the number of EC2 instances and the department
ec2_instances = int(input('How many EC2 instances do you want named? '))
department = input('What department are you in? ')

# Generate the EC2 instance names by randomly sampling from the employee list and concatenating with the department
unique_name = [f"{department}-{employee}" for employee in random.sample(employee_list, ec2_instances)]

# Print the EC2 instance names
for name in unique_name:
    print(name)


############################################################

# concat hashing characters and department to the name

import random

# List of employees
employee_list = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", 
                 "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Mary", "Patricia", "Jennifer", "Linda", 
                 "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Margaret", "Betty", 
                 "Sandra"]

# Get user input for the number of EC2 instances and the department
ec2_instances = int(input('How many EC2 instances do you want named? '))
department = input('What department are you in? ')
symbols = ('1234567890!@#$%^&*')
# Generate the EC2 instance names by randomly sampling from the employee list and concatenating with the department
unique_name = [f"{department}-{employee}-{random.sample(symbols,10)}" for employee in random.sample(employee_list, ec2_instances)]

# Print the EC2 instance names
for name in unique_name:
    print(name)