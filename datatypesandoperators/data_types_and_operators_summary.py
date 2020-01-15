import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pathlib import Path

directory = Path(os.getcwd())
file_dir = f"{directory}/resources/datatypes_summary.png"
img = mpimg.imread(file_dir)
plot = plt.imshow(img)
print("Data Types in python")
plt.show()

file_dir = f"{directory}/resources/operators_summary.png"
img = mpimg.imread(file_dir)
plot = plt.imshow(img)
print("Operators in python")
plt.show()