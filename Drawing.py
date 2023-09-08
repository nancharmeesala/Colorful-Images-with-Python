import numpy as np
import matplotlib.pyplot as plt

# Create a 3D NumPy array representing the image
# The array shape will be (height, width, channels), where channels are usually 3 (R, G, B)
height = 200
width = 300
channels = 3

# Initialize an empty array filled with zeros
colorful_image = np.zeros((height, width, channels), dtype=np.uint8)

# Fill the image with colors (for example, a gradient)
for y in range(height):
    for x in range(width):
        colorful_image[y, x, 0] = x  # Red channel
        colorful_image[y, x, 1] = y  # Green channel
        colorful_image[y, x, 2] = 255 - x - y  # Blue channel

# Display the image
plt.imshow(colorful_image)
plt.title('Colorful Image')
plt.axis('off')
plt.show()