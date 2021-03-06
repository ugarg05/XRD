from matplotlib import rc
rc("text", usetex=True)

import numpy as np
import matplotlib.pyplot as pl

region,ratio = np.loadtxt("ratiorho1.txt", unpack= "true")

pl.xscale('log')
pl.scatter(region,ratio)


y = np.array([0,10])
<<<<<<< HEAD
pl.semilogx( y*40. + 6.5e5, y, linestyle=":", color="red",linewidth=2)

=======
pl.semilogx( y*100. + 6.5e5, y, linestyle=":", color="red",linewidth=2)
>>>>>>> Reitveld

pl.xlabel("$\\lambda\\,{\\rm [cm]}$",fontsize=18)

pl.ylabel("$P_{max}/P_{min}$",fontsize=21)

pl.ylim(0,9) 

pl.xticks(fontsize=19)
pl.yticks(fontsize=20)

#pl.title("Rho = 1e7 gm/cm^3")
#pl.show()
pl.savefig("ratiorho1.pdf")
pl.savefig("ratiorho2.pdf")
