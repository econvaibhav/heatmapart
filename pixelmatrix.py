# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rxJzMznPrEHo0Uh-bBf8TCI0B0n7lOiS
"""

from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

image_path = '/content/900_Grasshopper-Geography_Elevation_map_of_India_with_white_background.jpg'
image = Image.open(image_path)

image

rgb_image = image.convert('RGB')

rgb_image

rgb_image.size

# Extract RGB values
width, height = rgb_image.size
rgb_values = []
for x in range(width):
    for y in range(height):
        r, g, b = rgb_image.getpixel((x, y))
        rgb_values.append([x, y, r, g, b])

rgb_values

df_rgb = pd.DataFrame(rgb_values, columns=['X', 'Y', 'R', 'G', 'B'])
df_rgb.head()

df_rgb['Average'] = df_rgb[['R', 'G', 'B']].mean(axis=1)

df_rgb.head()

heatmap_data = df_rgb.pivot('Y', 'X', 'Average')

heatmap_data.head()



# Creating the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='Reds')
plt.title('Heatmap of Average RGB Values')
plt.axis('off')  # Turn off the axis
plt.show()

downsample_size = (300, 300)
downsampled_image = rgb_image.resize(downsample_size)

downsampled_rgb_values = []
for x in range(downsample_size[0]):
    for y in range(downsample_size[1]):
        r, g, b = downsampled_image.getpixel((x, y))
        downsampled_rgb_values.append([x, y, r, g, b])

df_downsampled_rgb = pd.DataFrame(downsampled_rgb_values, columns=['X', 'Y', 'R', 'G', 'B'])

df_downsampled_rgb['Average'] = df_downsampled_rgb[['R', 'G', 'B']].mean(axis=1)

downsampled_heatmap_data = df_downsampled_rgb.pivot('Y', 'X', 'Average')

plt.figure(figsize=(10, 8))
sns.heatmap(downsampled_heatmap_data, cmap='Greys')
plt.title('Pixelated Heatmap of Average RGB Values')
plt.axis('off')
plt.show()

# Extract RGB values
width, height = rgb_image.size
rgb_values = []
for x in range(width):
    for y in range(height):
        r, g, b = rgb_image.getpixel((x, y))

        # Replace 255 with 0 and 0 with 255
        r = 0 if r == 255 else 255 if r == 0 else r
        g = 0 if g == 255 else 255 if g == 0 else g
        b = 0 if b == 255 else 255 if b == 0 else b

        rgb_values.append([x, y, r, g, b])

df_rgb = pd.DataFrame(rgb_values, columns=['X', 'Y', 'R', 'G', 'B'])
df_rgb['Average'] = df_rgb[['R', 'G', 'B']].mean(axis=1)
heatmap_data = df_rgb.pivot('Y', 'X', 'Average')

# Creating the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='Greys')
plt.title('Heatmap of Average RGB Values')
plt.axis('off')  # Turn off the axis
plt.show()

image_path = '/content/WhatsApp Image 2024-01-06 at 15.12.18.jpeg'
image = Image.open(image_path)
#rgb_image = image.convert('RGB')

downsample_size = (600, 600)
downsampled_image = rgb_image.resize(downsample_size)

downsampled_rgb_values = []
for x in range(downsample_size[0]):
    for y in range(downsample_size[1]):
        r, g, b = downsampled_image.getpixel((x, y))

        downsampled_rgb_values.append([x, y, r, g, b])

df_downsampled_rgb = pd.DataFrame(downsampled_rgb_values, columns=['X', 'Y', 'R', 'G', 'B'])

df_downsampled_rgb['Average'] = df_downsampled_rgb[['R', 'G', 'B']].mean(axis=1)

downsampled_heatmap_data = df_downsampled_rgb.pivot('Y', 'X', 'Average')

plt.figure(figsize=(10, 8))
sns.heatmap(downsampled_heatmap_data, cmap='inferno')
plt.title('Pixelated Heatmap of Average RGB Values')
plt.axis('off')
plt.show()