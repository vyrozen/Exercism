def square(number):
    if not 1<=number<=64 : raise ValueError("square must be between 1 and 64")
    return (2**(number-1))
    pass


def total():
    x = 1
    for i in range(63):
        x = x + (2**(i+1))
    return(x)
    pass
