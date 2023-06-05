def rotate(text, key):
    rotated_char, rotated_string = {}, ""
    plain = "abcdefghijklmnopqrstuvwxyz"
    for i in range (len(plain)):
        if i+key <= 25:
            rotated_char[plain[i]]=(plain[i+key])
        else: 
            for j in range (0,key):
                rotated_char[plain[i]]=(plain[j])
                i += 1
            break
    for j in text:
        if j.lower() in rotated_char:
            if j.isupper () : rotated_string = rotated_string + rotated_char[j.lower()].upper()
            else : rotated_string = rotated_string + rotated_char[j]
        else : rotated_string = rotated_string + j
    return(rotated_string)
    pass