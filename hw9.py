#----------------------Submitted by Uma Garg------------

#-------------- Homework 9 ---------------------------

import numpy as np

import matplotlib.pyplot as pl

from pylab import *


P , Pdot = np.loadtxt("hw9.txt",usecols=(1,2),unpack='True', delimiter=' ') # loads data for binary system

P1 , Pdot1 = np.loadtxt("solo.txt",usecols=(1,2),unpack='True', delimiter=' ')# loads data when pulsar doesnot have companion



x = np.log10(P/(365.0*24.0*3600.0))
x1 = np.log10(P1/(365.0*24.0*3600.0))
y = np.log10(Pdot/(365.0*24.0*3600.0))
y1 = np.log10(Pdot1/(365.0*24.0*3600.0))

X,Y = np.meshgrid(x,y)
time = np.log10(x/(2*y)) # characteristic time period
time1 = np.log10(x1/(2*y1)) # characteristic time period

P, Pdot=np.meshgrid(P, Pdot)

tau = np.log10(P/(2*Pdot))
B = np.log10(3.2e15 * (x * y)**(1./2.))
B1 = np.log10(3.2e15 * (x1 * y1)**(1./2.))
Mfield= np.log10(3.2e15 * (P * Pdot)**(1./2.))



pl.figure(0)
pl.scatter(y,x,marker='^', color='red', label='Pulsar in binary system')
pl.scatter(y1,x1,marker='.', color='k', label='Pulsar not present in binary system')
C=pl.contour(Y,X,tau, 8, colors= 'green')
C1=pl.contour(Y,X,Mfield, 8,colors ='blue')
C.collections[1].set_label('Constant $\\tau$')
C1.collections[1].set_label('Constant B')

pl.title('Time Period Derivative Vs Period')
pl.legend(loc='best')
pl.xlabel("Pdot")
pl.ylabel("P")


pl.figure(1)

x2 = np.logspace(-10.5,-6.5) # time period
y2 = np.logspace(16.60,16.75) #magnetic field
X2, Y2 = np.meshgrid(x2, y2)
tau2 = (X2*(3.2*1e15/Y2)**2/2)*(1/(365.0*24.0*60.0*60.0))
Pdot2 = (Y2/(3.2*10**15))**2

pl.scatter(B, x,marker='^', color='red', label='Pulsar in binary system')
pl.scatter(B1, x1,marker='^', color='k', label='Pulsar not present in binary system')

D=pl.contour(np.log10(Y2),np.log10(X2),np.log10(Pdot2),colors ='blue')
D1=pl.contour(np.log10(Y2),np.log10(X2),np.log10(tau2), colors= 'green')
pl.title(' Time Period Vs Magnetic Field ')
D1.collections[1].set_label('Constant $\\tau$')
D.collections[1].set_label('Constant $\dot{P}$')
pl.xlabel("B")
pl.ylabel("P")
pl.legend(loc='best')


pl.figure(2)
x3 = np.logspace(-0.82,-0.68) # charateristic time period
y3 = np.logspace(16.60,16.75) #magnetic field
X3, Y3 = np.meshgrid(x3, y3)
pl.scatter(B,time,marker='^', color='red', label='Pulsar in binary system')
pl.scatter(B1,time1,marker='^', color='k', label='Pulsar not present in binary system')

P3= ((2*X3*Y3**2)**(1./2.))/(3.2*1e15)
Pdot3 = (Y3**2)/(2*X3*(3.5*1e15)**2)
E=pl.contour(np.log10(Y3),np.log10(X3),np.log10(P3),4,colors ='blue')
E1=pl.contour(np.log10(Y3),np.log10(X3),np.log10(Pdot3),4, colors= 'green')
E.collections[1].set_label('Constant $P$')
E1.collections[1].set_label('Constant $\dot{P}$')
pl.title(' Characteristic age Vs Magnetic Field')
pl.xlabel("B")
pl.ylabel("Tau")
pl.legend(loc='best')


pl.show()

 
