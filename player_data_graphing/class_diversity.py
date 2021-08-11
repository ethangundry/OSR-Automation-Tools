# Displays a chart showing how many of each class have been played within the game world.

import matplotlib.pyplot as plt
import json
import os

class_list = []
for file in os.listdir('./characters'):
    if not (file.startswith('~') or file.endswith('~')):
        print(file)
        with open('./characters/' + file, 'r') as f:
            data = json.load(f)
            class_list.append(data['class'].lower())

labels = list(set(class_list))
labels.sort()
class_list.sort()

sizes = []
for label in labels:
    size = class_list.count(label)
    sizes.append(size)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')

plt.show()

print(labels)

print(class_list)
