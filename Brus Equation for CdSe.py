# import library
import matplotlib.pyplot as plt
import numpy as np
# range of radius
r= np.linspace(3.6*10**(-9),50*10**(-9),10000000) # in meter
# constants from literature
E_gap= 2.8 * 10**(-19)
m_e= 1.18 * 10**(-31)
m_h= 4.09 * 10**(-31)
h= 6.62607015 * 10**(-34)
# brus equation
del_E= ((E_gap) + (((h**2)/(8*(r**2)))*((1/(m_e))+(1/(m_h)))))
# in eV conversion
del_E_ev= del_E* 6.242* 10**(18)
# in nm conversion
R= r*10**(9)
# conditional plot
r_15= 15*10**(-9)
del_E_15= ((E_gap) + (((h**2)/(8*((r_15)**2)))*((1/(m_e))+(1/(m_h)))))
del_E_15_ev= del_E_15* 6.242* 10**(18)

r_24= 24*10**(-9)
del_E_24= ((E_gap) + (((h**2)/(8*((r_24)**2)))*((1/(m_e))+(1/(m_h)))))
del_E_24_ev= del_E_24* 6.242* 10**(18)

r_32= 32*10**(-9)
del_E_32= ((E_gap) + (((h**2)/(8*((r_32)**2)))*((1/(m_e))+(1/(m_h)))))
del_E_32_ev= del_E_32* 6.242* 10**(18)

r_44= 44*10**(-9)
del_E_44= ((E_gap) + (((h**2)/(8*((r_44)**2)))*((1/(m_e))+(1/(m_h)))))
del_E_44_ev= del_E_44* 6.242* 10**(18)

r_c= r_15*10**(9), r_24*10**(9), r_32*10**(9), r_44*10**(9)

del_E_c= del_E_15_ev,del_E_24_ev ,del_E_32_ev,del_E_44_ev

print(r_c)
print(del_E_c)
# experimental data
r_ex= 15,24,32,44
del_E_ex= 2.03,1.96,1.87,1.68
# plotting of graphs
plt.figure(1)
#matplotlib.pyplot.ylim(1.65,2.05)
plot_ex= plt.scatter(r_ex,del_E_ex,color='red')
plot_C= plt.scatter(r_c,del_E_c)
plot= plt.plot(R,del_E_ev)
#plt.legend(a,b,c)
plt.xlabel('Radius (nm)',weight='bold')
plt.xticks([0,4,8,12,16,20,24,28,32,36,40,44,48,52])
plt.ylabel('\u0394E(r) (eV)',weight='bold')

plt.show()