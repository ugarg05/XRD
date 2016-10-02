import matplotlib.pyplot as pl
import numpy as np

Field , voltage292 = np.loadtxt("BSC392_393B_273b_292.015.text",usecols=[0,7],unpack=True)
Field1 , voltage292_1 = np.loadtxt("BSC392_393B_273b_292.017.text",usecols=[0,7],unpack=True)
Field2 , voltage292_2 = np.loadtxt("BSC392_393B_273b_292.019.text",usecols=[0,7],unpack=True)
Field3 , voltage292_3 = np.loadtxt("BSC392_393B_273b_292.025.text",usecols=[0,7],unpack=True)
Field4 , voltage292_4 = np.loadtxt("BSC392_393B_273b_292.027.text",usecols=[0,7],unpack=True)
Field5 , voltage292_5 = np.loadtxt("BSC392_393B_273b_292.029.text",usecols=[0,7],unpack=True)
Field6 , voltage292_6 = np.loadtxt("BSC392_393B_273b_292.031.text",usecols=[0,7],unpack=True)
Field7 , voltage292_7 = np.loadtxt("BSC392_393B_273b_292.033.text",usecols=[0,7],unpack=True)

pl.plot(Field , voltage292, label = "90 degree")
pl.plot(Field1 , voltage292_1, label = "75 degree")
pl.plot(Field2 , voltage292_2, label = "60 degree") 
pl.plot(Field3 , voltage292_3, label = "45 degree")
pl.plot(Field4 , voltage292_4, label = "30 degree")
pl.plot(Field5 , voltage292_5, label = "15 degree")
pl.plot(Field6 , voltage292_6, label = "0 degree")
pl.plot(Field7 , voltage292_7, label = "-15 degree")
pl.xlabel("Magnetic Field (Tesla)")
pl.ylabel("Voltage (volt)")
pl.title("Magnetic field vs voltage for sample #273b at 0.3 K") 
#pl.show()
pl.legend(loc="best")
pl.savefig("voltage273b_vs_Field.pdf")

