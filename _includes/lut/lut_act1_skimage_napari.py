# %% [markdown]
# # Explore LUTs

# %%
# Instantiate the napari viewer
import napari
viewer = napari.Viewer()

# %%
# Read the image
from OpenIJTIFF import open_ij_tiff
image, axes, scales, units = open_ij_tiff('https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_high_dynamic_range.tif')

# %% [markdown]
# ### Napari GUI alternative to load data
# Drag and drop and rename the layer (alternative for loading data)\
# Change name of layer `viewer.layers[0].name = 'image_grayscale'` \
# Get the data as numpy array `image = viewer.layers['image_grayscale'].data` 

# %%
# Check image type and values
import numpy as np
print(image.dtype, np.min(image), np.max(image))

# %%
# View the intensity image as grayscale
viewer.add_image(image, name='image_grayscale', colormap='gray')

# %%
# Change brightness and contrast
viewer.layers['image_grayscale'].contrast_limits=(100, 175)

# %% [markdown]
# **Napari GUI** explore different contrast limits

# %%
# View the intensity image as grayscale
viewer.add_image(image, name='image_grayscale2', colormap='gray')

# %% [markdown]
# **Napari GUI** visualize images side by side\
# **Napari GUI** change brightness and contrast to visualize dim nuclei

# %%
# Check available colormap
print(list(napari.utils.colormaps.AVAILABLE_COLORMAPS))

# %%
# Change colormap
viewer.add_image(image, name='image_turbo', colormap='turbo')

# %% [markdown]
# **Napari GUI** explore different LUTs

# %%
# Extract image data from the layers
image_grayscale = viewer.layers['image_grayscale'].data
image_grayscale2 = viewer.layers['image_grayscale2'].data

# %%
# Compare raw data
print(image_grayscale[0:5,0:5])
print(image_grayscale2[0:5,0:5])
print((image_grayscale == image_grayscale2).all())

