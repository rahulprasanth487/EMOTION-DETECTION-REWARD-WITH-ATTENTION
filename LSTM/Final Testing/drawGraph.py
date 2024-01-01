import matplotlib.pyplot as plt
import numpy as np
functions = ['NoReward', 'RewardF1', 'RewardF2', 'RewardF3', 'RewardF4']

accuracies = [79.26,78.52,82.96,77.78,88.15]

plt.figure(figsize=(10, 6))
plt.plot(functions, accuracies, marker='o', linestyle='-', color='b', label='Accuracy')

plt.xlabel('Functions')
plt.ylabel('Accuracy (%)')
plt.title('Comparison of Function Accuracies')

for i, (function, accuracy) in enumerate(zip(functions, accuracies)):
    plt.text(i, accuracy, f'({function}, {accuracy:.2f}%)', ha='left', va='bottom')


smooth_function = np.linspace(0, len(functions) - 1, 100)
smooth_accuracies = np.interp(smooth_function, np.arange(len(functions)), accuracies)

plt.plot(smooth_function, smooth_accuracies, color='r', linestyle='--', label='Smooth Curve')
plt.legend()


plt.grid(True)
plt.show()
