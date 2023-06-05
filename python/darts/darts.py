def score(x, y):
    if (x**2)+(y**2)>100 : return(0)
    elif 25<(x**2)+(y**2)<=100 : return(1)
    elif 1<(x**2)+(y**2)<=25 : return(5)
    else : return(10)
    pass
