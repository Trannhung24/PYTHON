#int
a = 4 
print(type(a))
#str
b = " new lang"
print(type(b))
#decimal
#lay toan bo nd cua tvien decimal
from decimal import*
#lay toi da 30 chu so phan nguyen va p thap phan deciaml
getcontext().prec = 3
print(Decimal(10)/Decimal(3))
#phanso
from fractions import *
c = Fraction(6,9)
print(c)
print(type(c))
#so phuc
d = complex(2,5)
print(d)
#lay phan thuc
print(d.real)
#lay p.ao
print(d.imag)
print('\a')
