import matplotlib.pyplot as plt
import numpy as py
overs=py.arange(1, 11)
score=[4,8,2,6,8,10,13,1,5,3]
plt.bar(overs, score, color='green')
plt.title("Score summary")
plt.xlabel("Overs")
plt.ylabel("RUNS TAKEN")
plt.xticks(overs)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
