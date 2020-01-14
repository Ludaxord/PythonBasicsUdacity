import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pathlib import Path
x = 2
y = x
print(f"x => {x} y => {y}")

x,y,z = 2,3,5
print(f"x {x}, y {y}, z {z}")

x = 74728
y = 11.995
z = x/y
print(z)

directory = Path(os.getcwd())
file_dir = f"{directory}/resources/keywords.png"
print(f"file dir {file_dir}")
img = mpimg.imread(file_dir)
plot = plt.imshow(img)
print("Reserved keywords in python")
plt.show()

mv_population = 74728
non_python_mv_population = mv_population + 4000 - 600
print(non_python_mv_population)
mv_population += 4000 - 600
print(mv_population)

# QUIZ

# 1
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
print(f"reservoir volume = {reservoir_volume}")

# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
print(f"rainfall = {rainfall}")

# decrease the rainfall variable by 10% to account for runoff
decrease = rainfall*0.10
rainfall -= decrease
print(f"decreased rainfall by 10% (equal to {decrease}) = {rainfall}")

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(f"reservoir volume with rainfall = {reservoir_volume}")

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
decrease = reservoir_volume*0.05
reservoir_volume += decrease
print(f"decreased reservoir_volume by 5% (equal to {decrease}) = {reservoir_volume}")

# decrease reservoir_volume by 5% to account for evaporation
decrease = reservoir_volume*0.05
reservoir_volume -= decrease
print(f"decreased reservoir_volume by 5% (equal to {decrease}) = {reservoir_volume}")

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# 2
