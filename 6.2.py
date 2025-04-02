import math
from matplotlib import pyplot as plt
import numpy as np

class Derivative():
    h = 10**(-5)

    def __init__(self, a):
        self.a = a
    
    def __call__(self, x):
        x1 = ExponentialFunction(self.a)
        return (x1(x+self.h) - x1(x-self.h))/(2*self.h)

    def __get__(self, instance, owner):
        return (instance, owner)



class ExponentialFunction():
    def __init__(self, a):
        self.a = a
        self.der = Derivative(a)
        
    def __call__(self, x):
        return self.a*np.exp(x)
    
    def derivative(self, x):
        return self.der(x)
    

    def plot(self):
        x = np.linspace(0, 5)
        y = self(x)

        plt.plot(x, y, label = 'f(x)=a⋅e^x')
        plt.grid(True)

        x = np.linspace(0, 5)
        y = self.derivative(x)
        plt.plot(x, y, label = 'f′(x)≈(f(x+h)−f(x−h))/2h')

        plt.legend()
        plt.show()
        

    


exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()