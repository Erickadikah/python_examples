import json
#creating a dictionary
Dictionary ={1:'Welcome', 2: 'to', 3:'my', 4:'world', 5:'of geek'}

#our dictionary contains a tuple
#as key, so it si autoatically
#skipped if we have not set
#skipkeys = True the the code
#throws error
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',
      json_string)
print("  ")