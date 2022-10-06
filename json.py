import json


people_string = '''
{
  "people": [
    {
        "name": "john smith",
        "phone": "09345892",
        "emails": ["johnsmith@gmail.com", "john.smith@work-place.com"],
        "has_license": false
    },
    {
        "name": "jane wangui",
        "phone": "76788987",
        "emails": null,
        "has_license": true,
        }
     }
}
'''

data = json.loads(people_string)
for person in data['people']:
    print(person)
