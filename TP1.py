import math

a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("Masukkan c: "))

d = (b**2) - (4*a*c)

if d>0:
    x1 = ((-b)+math.sqrt(d))/(2*a)
    x2 = ((-b)-math.sqrt(d))/(2*a)
    print("Solusinya adalah {0} dan {1}" .format(x1,x2))
else:
    print("Persamaan tidak memiliki akar")