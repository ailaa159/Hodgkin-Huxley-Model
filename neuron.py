import numpy as np
import matplotlib.pyplot as plt

#probabilities
#m= 0.05 //sodium
#h=0.6  //soidum
#n=0.32 //potassium activation gate
#alpha is opening rate, beta is closing gate

def alpha_m(V): return (0.1*(V+40)) / (1-np.exp(-(V+40)/10))
def beta_m(V):  return 4*np.exp(-(V+65)/18)
def alpha_h(V): return 0.07*np.exp(-(V+65)/20)
def beta_h(V):  return 1/(1+np.exp(-(V+35)/10))
def alpha_n(V): return (0.01*(V+55)) / (1-np.exp(-(V+55)/10))
def beta_n(V):  return 0.125*np.exp(-(V+65)/80)

#conductances, how much each CAN flow if fully open gates.
gNa, gK, gL = 120,36,0.3
ENa, EK, EL= 50,-77,-54.4

#membrane capacitence -> capacity to hold charge
C=1.0

dt, T=0.01, 150
t=np.arange(0,T,dt)

V,m,h,n=-65,0.05,0.6,0.32
Vs=np.zeros(len(t))

for i in range(len(t)):
    I_Na= gNa * m**3 * h * (V-ENa)
    I_K  = gK  * n**4 * (V - EK)
    I_L  = gL * (V - EL)

    #derivatives wrt time
    dV = (5 - I_Na - I_K - I_L) / C
    dm = alpha_m(V)*(1-m) - beta_m(V)*m
    dh = alpha_h(V)*(1-h) - beta_h(V)*h
    dn = alpha_n(V)*(1-n) - beta_n(V)*n

    V += dV * dt
    m += dm * dt
    h += dh * dt
    n += dn * dt

    Vs[i]=V

plt.plot(t, Vs,color='steelblue')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.title("Hodgkin-Huxley neuron")
plt.show();