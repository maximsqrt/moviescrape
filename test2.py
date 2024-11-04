""" import json

# Sample Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "is_employee": True,
    "hobbies": ["reading", "cycling", "hiking"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"
    }
}

# Serialize the dictionary to a JSON string
json_string = json.dumps(data, separators=(',', ':'), indent=0)

# Print the serialized JSON string
print(json_string)
 """