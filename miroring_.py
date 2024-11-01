import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load the image
path = ("C:\\Users\\user\\\Downloads\\tiger.jpg.jpg")
image = img.imread(path)

# Create a mirrored copy of the image
mirrored_image = np.fliplr(image)

# Display the original and mirrored images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(mirrored_image)
plt.title("Mirrored Image")
plt.show()