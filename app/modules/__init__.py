def typeof(data):
    types_dict = {
        "bool": "boolean",
        "dict": "dictionary",
        "int": "integer",
        "str": "string",
    }
    typeof_data = str(type(data))
    data_type = typeof_data[8:-2]

    for key in types_dict:
        if key == data_type:
            data_type = types_dict[key]

    return data_type


def set_wrong_fields(data: dict, strings: list, integers: list):
    wrong_fields = {}

    for key in data.keys():
        data_type = typeof(data[key])

        if key in integers and not type(data[key]) is int:
            wrong_fields.update(
                {
                    f"{key}": f"must be integer, not {data_type}",
                }
            )

        elif key in strings and not type(data[key]) is str:
            wrong_fields.update(
                {
                    f"{key}": f"must be string, not {data_type}",
                }
            )

        elif key == "value" and not type(data[key]) is float:
            wrong_fields.update({f"{key}": f"must be float, not {data_type}"})

    return wrong_fields


def only_allowed_fields(data: dict, fields: list):
    not_allowed_fields = [key for key in data.keys() if key not in fields]

    if not_allowed_fields:
        return {"only_allowed_fields": fields}
