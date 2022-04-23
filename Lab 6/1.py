# 1
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.array([1,2,3])
# corresponding y axis values
y = np.array([2,4,1])

# plotting the points
plt.plot(x,y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph')

# function to show the plot
plt.show()

#%%
# 2
import matplotlib.pyplot as plt

# x co-ordinates of left side of bars
left = [1,2,3,4,5]

# heights of bars
height = [10,24,36,40,5]

# label for bars
tick_label = ['one','two','three','four','five']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red','green'])

#%%
# 3
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (8,6),dpi = 80)

# Create a new subplot from a grid of 1x1
plt.subplot(1,1,1)
X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C,S = np.cos(X),np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color = "blue", linewidth = 1.0, linestyle = "-", label = "cosine")
# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color = "green", linewidth = 1.0, linestyle = "-", label = "sine")

# Set x limits
plt.xlim(-4.0, 4.0)
# Set x ticks 
plt.xticks(np.linspace(-4, 4, 9, endpoint = True))

plt.xticks([-np.pi, np.pi / 2, 0, np.pi / 2, np.pi], 
           [r'$-\pi$',r'$-\p/2i$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Set y limits
plt.ylim(-1.0, 1.0)
# Set y ticks 
plt.yticks(np.linspace(-1, 1, 5, endpoint = True))


#### 
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], 
            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1,0,+1],
            [r'$-1$',r'$0$',r'$+1$',])
#### 

# Showing x and y labels
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Showing legend
plt.legend(loc = "upper left")

# Showing title
plt.title("Sine and Cosine Graph")
# Save figure using 72 dots per inch
plt.savefig("sample1.png",dpi = 72)

plt.show()
#%%
# 4
# plt.xticks([-np.pi, np.pi / 2, 0, np.pi / 2, np.pi], 
#            [r'$-\pi$',r'$-\p/2i$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# plt.yticks([-1,0,+1],
#             [r'$-1$',r'$0$',r'$+1$',])

#%%
# 5
t = 2*np.pi/3
plt.plot([t, t],[0,np.cos(t)],color='blue',linewidth=2.5,linestyle="--")
plt.scatter([t,],[np.cos(t),],50,color='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t,np.sin(t)),xycoords='data',
             xytext=(+10,+30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)],color="red",linewidth=2.5,linestyle="--")
plt.scatter([t,],[np.sin(t),],50,color="red")
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t,np.cos(t)),xycoords='data',
             xytext=(-90,-50),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#%% 
# 6
plt.subplot(2,1,1)
plt.subplot(2,1,2)

plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

#%%
# 7
plt.axes([0.1,0.1,.8,.8])
plt.axes([0.2,0.2,.3,.3])

#%%
# 8
axes = plt.gca()
axes.set_xlim(0,4)
axes.set_ylim(0,3)
axes.set_xticklabels([])
axes.set_yticklabels([])
plt.show()