x= int(input("Enter a year please: "))

leap = (x % 4 == 0) and ((x % 100 != 0) or (x % 400 == 0))

print(leap)

#fonksiyon halini yazdık.
def leapfunc(x):
    leap = (x % 4 == 0) and ((x % 100 != 0) or (x % 400 == 0))
    return leap 
    