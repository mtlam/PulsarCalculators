import numpy as np
from decimal import *




x = Decimal('1.89799095')
xerr = Decimal('0.00000004')
ecc = Decimal('0.000000092')
eccerr = Decimal('0.000000013')
i = 86.1 #degrees
ierr = 0.1
deg_to_rad = np.pi/180
sini = Decimal(np.sin(i*deg_to_rad))
sinierr = Decimal(ierr*np.cos(i*deg_to_rad))



a = (x/sini)*ltsec
aerr = a*((xerr/x)**2 + (sinierr/sini)**2).sqrt()



print "a =",a
print "  +/-",aerr,"m"


# Eccentricity e = sqrt(1-(b/a)^2)
# Therefore, b = a*sqrt(1-e^2)
# difference between both is a-b = a-a*sqrt(1-e^2) = a*(1-sqrt(1-e^2))



p = ecc**2 
perr = p*(2*eccerr/ecc)
q = 1-p #1-e^2
qerr = perr
r = q.sqrt() #sqrt(1-e^2)
rerr = r*(Decimal(0.5)*qerr/q)
s = 1-r #1-sqrt(1-e^2)
serr = rerr
fac = a*s
facerr = fac*((aerr/a)**2 + (serr/s)**2).sqrt()
print "a-b =",fac
print "  +/-",fix(facerr),"m"
print
