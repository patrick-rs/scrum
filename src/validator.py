from schema import SchemaError


def ValidateDictionary(schema, dict):
    try:
        schema.validate(dict)
        return True
    except SchemaError:
        return False
