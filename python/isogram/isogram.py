def is_isogram(string):
    string_array = []
    for i in string:
        if "a"<=i.lower()<="z":
            if i.lower() in string_array : return (False)
            else : string_array.append(i.lower())
        else:continue
    return(True)
    pass
