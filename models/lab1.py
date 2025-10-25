import numpy as np
import matplotlib.pyplot as plt

t = 19.62616
v = 1.693186

q_max = 2 / (1 + v**2)
q_values = np.linspace(0.01, q_max, 500)

t1_values = (1 + np.sqrt((1 - q_values)/(2*q_values)*(v**2 - 1))) * t
t2_values = (1 - np.sqrt(q_values/(2*(1 - q_values))*(v**2 - 1))) * t

plt.figure(figsize=(10,6))
plt.plot(q_values, t1_values, label='t1 (медленная фаза)', color='blue')
plt.plot(q_values, t2_values, label='t2 (быстрая фаза)', color='red')
plt.axvline(0.3, color='green', linestyle='--', label='Выбранный q=0.3')
plt.title('Зависимость t1 и t2 от q')
plt.xlabel('q')
plt.ylabel('t1, t2')
plt.legend()
plt.grid(True)
plt.show()
