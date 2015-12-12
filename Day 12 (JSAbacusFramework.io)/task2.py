import json

text_object = open("input.txt", "r").readline()
json_object = json.loads(text_object)


def parse(value):

    if isinstance(value, dict):

        if "red" in value.values() or "red" in value.keys():
            return 0

        dict_result = 0
        for key, v in value.items():
            dict_result += parse(v)

        return dict_result

    elif isinstance(value, list):

        list_result = 0
        for element in value:
            list_result += parse(element)

        return list_result

    else:
        # String or integer
        try:
            return int(value)
        except ValueError:
            return 0

print parse(json_object)
