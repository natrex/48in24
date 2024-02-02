def isDiv3(num): 
    return "Pling" if num % 3 == 0 else ""
def isDiv5(num):
    return "Plang" if num % 5 == 0 else ""
def isDiv7(num):
    return "Plong" if num % 7 == 0 else ""
def convert(number):
    raindrop = isDiv3(number) + isDiv5(number) + isDiv7(number)
    return raindrop if raindrop != "" else str(number)


print(convert(52))