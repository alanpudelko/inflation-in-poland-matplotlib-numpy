from matplotlib import pyplot as plt
import numpy as np

years = np.arange(2000, 2024)

rates = [10.1, 5.5, 1.9, 0.8, 3.5, 2.1, 1.0, 2.5, 4.2, 3.5, 2.6, 4.3, 3.7, 0.9, 0.0, -0.9, -0.6, 2.0, 1.6, 2.3, 3.4,
         5.1, 14.4, 11.4]

plt.figure(figsize=(8, 4))

plt.plot(years, rates, color="red", linewidth=2)

plt.xticks(np.arange(min(years), max(years) + 1, 1), rotation=90)
plt.yticks(np.arange(int(min(rates)), int(max(rates)) + 1, 1))

plt.title("Inflation in Poland 2000-2023")
plt.xlabel("Years")
plt.ylabel("Inflation in %")

plt.subplots_adjust(bottom=0.19)

plt.show()