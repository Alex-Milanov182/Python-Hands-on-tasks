import json

with open('users_1k.json', 'r') as file:
    data = json.load(file)

def replace_values(obj, key_to_replace, new_value):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == key_to_replace:
                obj[key] = new_value
            else:
                replace_values(value, key_to_replace, new_value)
    elif isinstance(obj, list):
        for item in obj:
            replace_values(item, key_to_replace, new_value)


replace_values(data, 'name', None)


with open('output_users_1k.json', 'w') as file:
    json.dump(data, file, indent=4)