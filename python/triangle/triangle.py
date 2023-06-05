def equilateral(sides):
    if 0 in sides : return(False)
    elif not sides[0]+sides[1]>=sides[2] and not sides[0]+sides[2]>=sides[1] and not sides[1]+sides[2]>=sides[0] : return(False)
    elif sides[0] == sides[1] == sides[2] : return(True)
    else : return(False)
    pass


def isosceles(sides):
    if 0 in sides : return(False)
    elif sides[0]+sides[1]>=sides[2] and sides[0]+sides[2]>=sides[1] and sides[1]+sides[2]>=sides[0] :
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2] : return(True)
        else : return(False)
    else : return(False)
    pass


def scalene(sides):
    if 0 in sides : return(False)
    elif sides[0]+sides[1]>=sides[2] and sides[0]+sides[2]>=sides[1] and sides[1]+sides[2]>=sides[0] :
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2] : return(True)
        else : return(False)
    else : return(False)
    pass
