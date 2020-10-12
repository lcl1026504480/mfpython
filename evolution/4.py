import matplotlib.pyplot as plt
import numpy as np

POP_SIZE = 100
N_GENERATIONS = 50
Cp=2
Cg=2
Ws=.9
We=.4

X_BOUND=[-10,10]
V_BOUND=[i/N_GENERATIONS*10 for i in X_BOUND]



def F(x): return np.sin(x**2) + np.cos(2*x)*x     # to find the maximum of this function



# convert binary DNA to decimal and normalize it to a range(0, 5)



pop = np.random.uniform(*X_BOUND, POP_SIZE)
pov = np.random.uniform(*V_BOUND, POP_SIZE)
def F(x): return np.sin(10*x)*x + np.cos(2*x)*x     # to find the maximum of this function


# find non-zero fitness for selection
prev=float("-inf")
plt.ion()       # something about plotting
x = np.linspace(*X_BOUND, 200)
plt.plot(x, F(x))

for i in range(N_GENERATIONS):
    F_values = F(pop)   # compute function value by extracting DNA

    # something about plotting
   
    w=(Ws-We)*(N_GENERATIONS-i)/N_GENERATIONS+We
    # parent is replaced by its child
    g=pop[F_values.argmax()]
    if not i:
            p=g
    else:
            p=g if F(p)<=F(g) else p
    if 'sca' in globals(): 
            sca.remove()
            sca1.remove()
            sca2.remove()
    sca = plt.scatter(pop, F_values, 100,"r")
    sca1=plt.scatter(p,F(p),100,'b')
    sca2=plt.scatter(g,F(g),100,"g"); plt.pause(0.1)

    
    pov=w*pov+Cg*np.random.rand(POP_SIZE)*(g-pop)+Cp*np.random.rand(POP_SIZE)*(p-pop)
    pov=np.clip(pov,*V_BOUND)
    pop+=pov
    pop=np.clip(pop,*X_BOUND)

plt.ioff(); plt.show()



