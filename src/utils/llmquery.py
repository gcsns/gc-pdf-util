from field import Field

def get_fields_query(fields: list[Field]) -> str:
    description_position = 50
    fields_query = "fieldName" + " "* (description_position - 9) +"description\n" + "-" * (description_position + 12) + "\n"
    for field in fields:
        fields_query += f"{field.name}"
        if field.description:
            fields_query += " " * (description_position - len(field.name)) + field.description + "\n"
        else:
            fields_query += "\n"
    return fields_query
