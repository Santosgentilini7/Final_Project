import matplotlib.pyplot as plt


#ALCOHOL CONSUMPTION

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Alcohol_use = [3.9,6,5,6,10,13,24,36,48,52]
Age = [12,13,14,15,16,17,18,19,20,21]
ax.bar(Age,Alcohol_use)
plt.xlabel('Age') # Adds x label
plt.ylabel('Alcohol use') # Adds y label
plt.title('Alcohol use over the years')
colors = ["skyblue","lightblue","cornflowerblue","royalblue","blue","mediumblue","darkblue",
          "navy","midnightblue","midnightblue"]
plt.bar(Age, Alcohol_use, color =colors )
plt.show()

#MARIJUANA CONSUMPTION

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Marijuana_use = [1.1,3.4,8.7,14.5,22.5,28,33.7,33.4,34,33]
Age = [12,13,14,15,16,17,18,19,20,21]
ax.bar(Age,Marijuana_use)
plt.xlabel('Age') # Adds x label
plt.ylabel('Marijuana use') # Adds y label
plt.title('Marijuana use over the years')
colors = ["palegreen","lightgreen","lime","limegreen","forestgreen","green","green",
          "green","darkgreen","darkgreen"]
plt.bar(Age, Marijuana_use, color =colors)
plt.show()

#COCAINE CONSUMPTION

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Cocaine_use = [0.1,0.1,0.1,0.5,1,2,3.2,4.1,4.9,4.8]
Age = [12,13,14,15,16,17,18,19,20,21]
ax.bar(Age,Cocaine_use)
plt.xlabel('Age') # Adds x label
plt.ylabel('Cocaine use') # Adds y label
plt.title('Cocaine use over the years')
colors = ["rosybrown","lightcoral","indianred","red","brown","firebrick",
          "maroon","maroon","darkred","darkred"]
plt.bar(Age, Cocaine_use, color =colors, )
plt.show()

#EVOLUTION OF ALCOHOL CONSUMPTION FROM 12 TO 60 YEARS OLD

import pandas as pd
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()
drugs_consumption = pd.read_csv(
   "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv")


ages = [12,13,14,15,16,17,18,19,20,21,22,24,26,30,35,50,65]
plt.plot(ages,drugs_consumption["alcohol-use"])
plt.xlabel('Age') # Adds x label
plt.ylabel('Alcohol use') # Adds y label
plt.title('Alcohol use over the years')

print(plt.plot(ages,drugs_consumption["alcohol-use"]))

#COMPARISON OF DIFFERENT DRUGS OVER THE YEARS 1

import numpy as np
import matplotlib.pyplot as plt
data = [[33.7, 33.4, 34.0, 33.0],
[3.2, 	4.1, 4.9, 	4.8],
[0.4, 0.5, 	0.9, 0.6]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('Marijuana, Cocaine and Heroin consumption')
ax.set_title('Marijuana versus Cocaine versus Heroin consumption from 18 to 21 years old')
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25, label = "Marijuana")
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25, label = "Cocaine")
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25, label = "Heroin")
ax.legend()


#COMPARISON OF DIFFERENT DRUGS OVER THE YEARS 2

import numpy as np
import matplotlib.pyplot as plt
data = [[58.7, 64.6, 69.7,83.2],
[33.7, 	33.4, 34.0,	33.0],
[0.4, 0.5, 	0.9, 0.6]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('Alcohol and Marijuana consumption')
ax.set_title('Alcohol versus Marijuana consumption from 18 to 21 years old')
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25,label = "Alcohol")
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25,label = "Marijuana")
leg = ax.legend()