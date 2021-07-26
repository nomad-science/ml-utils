def convert_column_names_to_lowercase(input_list):
    output_names = []

    for name in input_list:
        name = name.lower().replace(" ", "_")
        output_names.append(name)

    return output_names

def replace_column_names(input_dict, list_to_update):
    output_list = []
    
    for value in list_to_update:
        if value in input_dict:
            output_list.append(input_dict[value])
        else:
            output_list.append(value)

    return output_list