def is_armstrong_number(number):
    x=[]
    for i in str(number):
        x.append(int(int(i)**len(str(number))))
    if sum(x) == number : return(True)
    else : return(False)
    pass
