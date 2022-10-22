# import json
#
# # Creating a dictionary
# Dictionary = {1: 'Welcome', 2: 'to',
#               3: 'programing', 4: 'erick',
#               5: 'adikah'}
#
# # Converts input dictionary into
# # string and stores it in json_string
# json_string = json.dumps(Dictionary)
# print('Equivalent json string of input dictionary:',
#       json_string)
# print("        ")
#
# # Checking type of object
# # returned by json.dumps
# print(type(json_string))

#!/usr/bin/python3
import json
#json string:

#multi-line string

x = """{
    "Name": "Erick Adikah",
    "Contact Number": 7867567898,
    "Email": "adikaherick123@gmail.com",
    "Hobbies":["Reading", "Sketching", "gammer"]
    }"""

# parse x:
y = json.loads(x)
#the result is a python dictionary.

print(y)
print(y['Name'])

# import json
#
# #JSON string
#
# employee = '{"id":"39630361", "name": "Erick adikah", "department": "finance"}'
# employee_dict = json.loads(employee)
# print(employee)
# print(employee_dict['name'])