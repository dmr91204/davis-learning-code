# Davis Rogers
import matplotlib.pyplot as plt
import numpy as np
with open("levels.dat","r") as data:
	levels = np.float64(data.readlines())
avg = np.mean(levels)
plt.plot(levels)
plt.plot([0,len(levels)],[avg,avg],"--")
plt.annotate(f"mean=(avg:.2f)m", [len(levels),avg], [0,10], textcoords="offset pixels", ha="right")
plt.ylabel("Level (m)")
plt.tight_layout()
plt.savefig("levels.png",bbox_inches="tight")
plt.show()

