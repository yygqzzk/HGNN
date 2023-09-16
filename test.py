import torch
import dhg
from matplotlib import pyplot as plt

print(torch.cuda.is_available())
g = dhg.random.graph_Gnm(5, 8)
g.draw()
plt.show()