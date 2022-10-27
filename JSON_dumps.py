import json

# creating a dictionary
Dictionary = {1: 'Welcome', 2: 'to', 3: 'my', 4: 'world', 5: 'of geek'}

# our dictionary contains a tuple
# as key, so it si autoatically
# skipped if we have not set
# skipkeys = True the the code
# throws error


json_string = json.dumps(Dictionary, skipkeys=True)
print('Equivalent json string of input dictionary:',
      json_string)
print("  ")

print("-" * 50)


# class Person_User(object):
#     def __int__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# user = Person_User(first_name="jake", last_name="Dolye")
# json_data = json.dumps(user.__dict__)
# print(json_data)
# print(Person_User(**json.loads(json_data)))


import json
from uuid import uuid4

class GFG_User(object):
      def __init__(self, first_name: str, last_name: str):
            self.first_name = first_name
            self.last_name = last_name

      def do_uuid(self, line):
            print(uuid4())


user = GFG_User(first_name="Jake", last_name="Doyle")
json_data = json.dumps(user.__dict__)
print(json_data)
print(GFG_User(**json.loads(json_data)))
