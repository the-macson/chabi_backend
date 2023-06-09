def switch_key_value(d):
    return {v: k for k, v in d.items()}


print(switch_key_value({
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}))