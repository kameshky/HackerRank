def mutate_string(string, position, character):
    list_string = list(string)
    list_string[position] = character
    joined_string = "".join(list_string)
    return joined_string