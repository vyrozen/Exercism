def convert(number):
    x = []
    if number%3 == 0 : x.append("Pling")
    if number%5 == 0 : x.append("Plang")
    if number%7 == 0 : x.append("Plong")
    k = ""
    for i in range (len(x)):
        k = k + x[i]
    if k == "" : return(str(number))
    else : return(k)
    pass

output = convert(21)
print(output)