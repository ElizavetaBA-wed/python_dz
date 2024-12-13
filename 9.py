from matplotlib import pyplot as plt
import numpy as np


def f(x, a, b):
    y = (x**b + a**b)/x**b
    return y


n = 0
x_left = np.linspace(-20, n-0.01, 20000)
x_right = np.linspace(n+0.01, 20, 20000)



a, b = 1, 0.5
plt.plot(x_left, f(x_left, a, b), color = '#7FFF00')
plt.plot(x_right, f(x_right, a, b), color = '#7FFF00F', label = r"$f(x) = \frac{x^{1}+1^{1}}{x^{1}}$")

a, b = 1, -0.5
plt.plot(x_left, f(x_left, a, b), color = '#ADD8E6')
plt.plot(x_right, f(x_right, a, b), color = '#ADD8E6', label = r"$f(x) = \frac{x^{1}+2^{1}}{x^{1}}$")

a, b = 1, -1.5
plt.plot(x_left, f(x_left, a, b), color = '#9F2B68')
plt.plot(x_right, f(x_right, a, b), color = '#ADD8E6', label = r"$f(x) = \frac{x^{2}+1^{2}}{x^{2}}$")


plt.axvline(n, color = "red", linestyle='--', label='точка разрыва')
plt.title(r"График функции $f(x) = \frac{x^{b}+a^{b}}{x^{b}}$")
plt.xlim(-1, 20)
plt.grid(True)
plt.show()


a = 1
b =[0.5, 0.8, -0.5, -0.8, -1.5, -2.5]
for i in [0, 2, 4]:
    plt.subplot(1, 3, (i//2)+1)
    plt.plot(x_right, f(x_right, 1, 0), label = r"$f(x) = \frac{x^{0}+1^{0}}{x^{0}}$")
    plt.plot(x_right, f(x_right, 1, -1), label = r"$f(x) = \frac{x^{-1}+1^{-1}}{x^{-1}}$")
    j = b[i]
    plt.plot(x_right, f(x_right, 1, j), label = f"f(x), a=1, b = {b[i]}")
    j = b[i+1]
    plt.plot(x_right, f(x_right, 1, j), label = f"f(x), a=1, b = {b[i+1]}")
    
    plt.xlim(0, 20)
    plt.grid(True)
    plt.legend()

plt.suptitle(r"График функции $f(x) = \frac{x^{b}+a^{b}}{x^{b}}$")
plt.show()
