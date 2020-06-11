import numpy as np 
import matplotlib.pyplot as plt 

import matplotlib.lines  as lines

'''Basic goals:
1. Just draw a friggin line
2. Change the colors of the line
3. Draw a 7 segment figure
4. make figure interactible - change color by clicking line
5. '''

fig = plt.figure()
p = (0.1,.9)
q = (.9, .9)
x1 = p[0]
y1 = p[1]
x2 = q[0]
y2 = q[1]

fig.add_artist(lines.Line2D([x1, x2], [y1, y2]))    
plt.show()

segmentA = ([.1, .9], [.9, .9])

#%%

