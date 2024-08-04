#my code
question1 = int(input('How many days ago have you purchased the item? '))
question2 = input('Have you used the item at all [y/n]? ')
question3 = input('Has the item broken down on its own [y/n]? ')

if ((question1 <= 10 and question2 == 'n') or question3 == 'y'):
    print('You can get a refund')
else:
    print('You cannot get a refund')


#######################################################################################


#solution
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')
