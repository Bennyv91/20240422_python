person = {
    "first_name": "Bob", 
    "last_name": "Smith", 
    "age": 23,
}

print (person["first_name"])
print (person["last_name"])
print (person["age"])

print(person)

person["age"] = 24
person["hair_color"] = "brown"

for key in person:
    print(key, person[key])

try:
    print(person["middle_name"])
except KeyError:
    print("KeyError: middle_name", "N/A")

print(person.get("middle_name", "N/A"))
