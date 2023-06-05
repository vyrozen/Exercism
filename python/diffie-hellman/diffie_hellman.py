import random
def private_key(p):
    return(random.randrange(2,p))
    pass


def public_key(p, g, private):
    return ((g**private)%p)
    pass


def secret(p, public, private):
    return((public**private)%p)
    pass
