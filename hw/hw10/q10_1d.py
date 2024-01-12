from this import d
import numpy as np
import matplotlib.pyplot as plt
c0 = 4
c1 = 3
lr = 1
iterations = 10000
print(f"Init :c0 is {c0}, c1 is {c1}, lr is {lr}")
c0_list = [c0]
c1_list = [c1]
for i in range(1, iterations):
    dE_dc0 = - (4*(c1**4)*c0) / (c0**2+c1**2)**3
    dE_dc1 = 4 * c1**3 * c0**2 / (c0**2+c1**2)**3
    c0 -= lr * dE_dc0
    c1 -= lr * dE_dc1
    c0_list.append(c0)
    c1_list.append(c1)
    if i%1000==0:
        print(f"Iter {i}: c0 is {c0}, c1 is {c1}")
print(f"Final: c0 is {c0}, c1 is {c1}")
x = np.linspace(start=0, stop=iterations, num=iterations)
plt.title('Plot for c0 & c1 versus iterations') #写上图题
plt.xlabel('Iter')
plt.ylabel('value')       
plt.xlim(right=iterations)
plt.plot(x, c0_list, label='c0')
plt.plot(x, c1_list, label='c1')
plt.legend()
plt.savefig("C:/Users/19602/Desktop/cs-182-DL/hw/hw10/submit.jpg")
plt.show()