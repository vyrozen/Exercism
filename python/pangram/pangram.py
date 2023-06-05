def is_pangram(sentence):
    test_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in sentence:
        if i.lower() in test_case:
            test_case.remove(i.lower())
    if len(test_case) == 0 : return (True)
    else : return (False)
    pass
