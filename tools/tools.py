import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pathlib import Path


def display_image(image_file_name, image_title):
    directory = Path(os.getcwd())
    file_dir = f"{directory}/resources/{image_file_name}"
    img = mpimg.imread(file_dir)
    plot = plt.imshow(img)
    print(image_title)
    plt.show()
