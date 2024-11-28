import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import numpy as np
   
import warnings
warnings.filterwarnings('ignore')
   
from tensorflow import keras
from keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.preprocessing import image_dataset_from_directory
   
import os
import matplotlib.image as mpimg


# Dataset Link- https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
import zipfile
zip_ref = zipfile.ZipFile('/Users/ahmet/Uni/projects/chest-xray-pneumonia.zip', 'r')
zip_ref.extractall('/Users/ahmet/Uni/projects')
zip_ref.close()


path = '/Users/ahmet/Uni/projects/chest_xray/chest_xray/train'
classes = os.listdir(path)
print(classes)


# Define the directories for the X-ray images
PNEUMONIA_dir = os.path.join(path + '/' + classes[0])
NORMAL_dir = os.path.join(path + '/' + classes[1])
 
# Create lists of the file names in each directory
PNEUMONIA_dir = os.path.join(path, 'PNEUMONIA')
NORMAL_dir = os.path.join(path, 'NORMAL')


pneumonia_names = os.listdir(PNEUMONIA_dir)
normal_names = os.listdir(NORMAL_dir)

print('There are', len(pneumonia_names), 'images of pneumonia infected in training dataset')
print('There are', len(normal_names), 'normal images in training dataset')


# Check if directories exist
"""
if os.path.exists(PNEUMONIA_dir) and os.path.exists(NORMAL_dir):
    
else:
    print("One or both directories are missing.")

"""





"""
# Set the figure size
fig = plt.gcf()
fig.set_size_inches(16, 8)
 
# Select the starting index for the images to display
pic_index = 210
 
# Create lists of the file paths for the 16 images to display
pneumonia_images = [os.path.join(PNEUMONIA_dir, fname)
                    for fname in pneumonia_names[pic_index-8:pic_index]]
# Loop through the image paths and display each image in a subplot
for i, img_path in enumerate(pneumonia_images):
    sp = plt.subplot(2, 4, i+1)
    sp.axis('Off')
 
    # Read in the image using Matplotlib's imread() function
    img = mpimg.imread(img_path)
    plt.imshow(img)
 
# Display the plot with the 16 images in a 4x4
plt.show()
"""

# Set the figure size
fig = plt.gcf()
fig.set_size_inches(16, 8)

# Select the starting index for the images to display
pic_index = 210

# Create lists of the file paths for the 16 images to display
normal_images = [os.path.join(NORMAL_dir, fname)
			for fname in normal_names[pic_index-8:pic_index]]
# Loop through the image paths and display each image in a subplot
for i, img_path in enumerate(normal_images):
	sp = plt.subplot(2, 4, i+1)
	sp.axis('Off')

	# Read in the image using Matplotlib's imread() function
	img = mpimg.imread(img_path)
	plt.imshow(img)

# Display the plot with the 16 images in a 4x4 grid
plt.show()
