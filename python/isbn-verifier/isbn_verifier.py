def is_valid(isbn):
    isbn_arr = []
    for i in isbn.lower():
        if "a"<=i<="w" or "y"<=i<="z" : return(False)
        if "0"<=i<="9" : isbn_arr.append(int(i))
        if i=="x" :
            if isbn[len(isbn)-1]=="X":
                 isbn_arr.append(10)
            else : return(False)
    if len(isbn_arr) != 10 : return(False)
    return ((isbn_arr[0]*10)+(isbn_arr[1]*9)+(isbn_arr[2]*8)+(isbn_arr[3]*7)+(isbn_arr[4]*6)+(isbn_arr[5]*5)+(isbn_arr[6]*4)+(isbn_arr[7]*3)+(isbn_arr[8]*2)+(isbn_arr[9]*1)) % 11 == 0
    pass
