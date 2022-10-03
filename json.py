import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

    with open ("new_states.json", 'w') as f:
        json.dump(data, f indent=2)






















# people_string = '''
# {
#   "people": [
#     {
#         "name": "john smith",
#         "phone": "09345892",
#         "emails": ["johnsmith@gmail.com", "john.smith@work-place.com"],
#         "has_license": false
#     },
#     {
#         "name": "jane wangui",
#         "phone": "76788987",
#         "emails": null,
#         "has_license": true,
#         }
#      }
# }
# '''
# data = json.loads(people_string)
#
# print(type(data['people']))
# print(data)
# for person in data['people']:
#     print(person)
