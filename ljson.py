import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print(person_dict)
#prints the dictionary
print(person_dict['languages'])
#output: ['English', 'french']