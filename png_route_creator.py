

from PIL import Image
import numpy as np
from scipy.ndimage import binary_dilation
import os

# ==========================================
# IMAGE PATH
# ==========================================
newest_image_path = "cani2.jpg"

# ==========================================
# COLOUR DETECTION SETTINGS
# ==========================================
# Adjust these values to detect different colours

# BLUE ROUTE DETECTION
colour_lower = np.array([0, 50, 120, 255])
colour_upper = np.array([120, 180, 255, 255])

# ==========================================
# OUTPUT ROUTE COLOUR
# ==========================================
# RGBA FORMAT:
# [RED, GREEN, BLUE, ALPHA]

route_colour = [0, 140, 255, 255]

# ==========================================
# ROUTE THICKNESS
# ==========================================
# Higher number = thicker route

route_thickness = 4

# ==========================================
# LOAD IMAGE
# ==========================================
image = Image.open(newest_image_path).convert("RGBA")
data = np.array(image)

# ==========================================
# DETECT ROUTE COLOUR
# ==========================================
mask = (
    (data[:, :, 0] >= colour_lower[0]) &
    (data[:, :, 0] <= colour_upper[0]) &
    (data[:, :, 1] >= colour_lower[1]) &
    (data[:, :, 1] <= colour_upper[1]) &
    (data[:, :, 2] >= colour_lower[2]) &
    (data[:, :, 2] <= colour_upper[2])
)
                    

# ==========================================
# THICKEN ROUTE LINE
# ==========================================
thickened_mask = binary_dilation(
mask,
iterations=route_thickness
)

# ==========================================
# CREATE TRANSPARENT OUTPUT
# ==========================================
output_data = np.zeros_like(data)

# Apply route colour
output_data[thickened_mask] = route_colour

# ==========================================
# CREATE OUTPUT FILENAME
# ==========================================
base, ext = os.path.splitext(newest_image_path)

newest_thickened_path = f"{base}_route.png"

# ==========================================
# SAVE PNG
# ==========================================
output_image = Image.fromarray(output_data, mode="RGBA")

output_image.save(newest_thickened_path)

print("")
print("===================================")
print("ROUTE PNG CREATED")
print("===================================")
print("")
print("Saved to:")
print(newest_thickened_path)

print("")