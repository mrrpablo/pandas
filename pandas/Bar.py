# Year 1993
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Beginners = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
Value = [3.083, 28.321, 16.077, 16.762, 35.757]
bar_labels = ["Water", "Urban", "Shrubs", "Forest", "Bare Soil"]
bar_colors = ["tab:cyan", "tab:blue", "tab:orange", "tab:green", "tab:red"]
ax.bar(Beginners, Value, label = bar_labels, color = bar_colors)
ax.set_ylabel ("Year 1993")
ax.set_xlabel ("Land Cover Land Use Class")
ax.legend(title = "LCLU", loc = 2)
ax.set_title("Land Cover Land Use Class Changes Year 1993")
plt.show()

#Year 2003
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Beginners = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
Value = [3.036, 31.414, 13.572, 15.603, 36.374]
bar_labels = ["Water", "Urban", "Shrubs", "Forest", "Bare Soil"]
bar_colors = ["tab:cyan", "tab:blue", "tab:orange", "tab:green", "tab:red"]
ax.bar(Beginners, Value, label = bar_labels, color = bar_colors)
ax.set_ylabel ("Year 2003")
ax.set_xlabel ("Land Cover Land Use Class")
ax.legend(title = "LCLU", loc = 2)
ax.set_title("Land Cover Land Use Class Changes Year 2003")
plt.show()

#Year 2013
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Beginners = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
Value = [2.990, 35.543, 11.610, 12.077, 37.780]
bar_labels = ["Water", "Urban", "Shrubs", "Forest", "Bare Soil"]
bar_colors = ["tab:cyan", "tab:blue", "tab:orange", "tab:green", "tab:red"]
ax.bar(Beginners, Value, label = bar_labels, color = bar_colors)
ax.set_ylabel ("Year 2013")
ax.set_xlabel ("Land Cover Land Use Class")
ax.legend(title = "LCLU", loc = 2)
ax.set_title("Land Cover Land Use Class Changes Year 2013")
plt.show()

#Year 2023
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Beginners = ["Water/Meshland", "Urban", "Shrubs", "Forest", "Bare Soil"]
Value = [3.077, 38.765, 10.290, 10.290, 37.432]
bar_labels = ["Water", "Urban", "Shrubs", "Forest", "Bare Soil"]
bar_colors = ["tab:cyan", "tab:blue", "tab:orange", "tab:green", "tab:red"]
ax.bar(Beginners, Value, label = bar_labels, color = bar_colors)
ax.set_ylabel ("Year 2023")
ax.set_xlabel ("Land Cover Land Use Class")
ax.legend(title = "LCLU", loc = 2)
ax.set_title("Land Cover Land Use Class Changes Year 2023")
plt.show()
