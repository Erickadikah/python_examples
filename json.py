import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)























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
