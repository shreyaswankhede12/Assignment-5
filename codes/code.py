import matplotlib.pyplot as plt
from matplotlib_venn import venn3,venn3_unweighted

labels=['A','B','C']
items=[50,50,25,50,25,25,10]
venn3(subsets=items,set_labels=labels,alpha=0.4)
plt.show()