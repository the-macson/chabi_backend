def sort_list_of_dict(list_of_dict, key):
    return sorted(list_of_dict, key=lambda x: x[key])


print(sort_list_of_dict([
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
], "fruit"))

print(sort_list_of_dict([
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
], "color"))
