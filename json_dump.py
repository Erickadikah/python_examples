import json

# Creating a dictionary
Dictionary = {1: 'Welcome', 2: 'to',
              3: 'programing', 4: 'erick',
              5: 'adikah'}

# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',
      json_string)
print("        ")

# Checking type of object
# returned by json.dumps
print(type(json_string))