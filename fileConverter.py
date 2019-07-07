#turns PNG files into jped files, which are optimized for the network. Best resolution for images is 64x64px.

from glob import glob      
import numpy as np                                                     
import cv2 
pngs = glob('data/*.png')
def read_transparent_png(filename):
    image_4channel = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:,:,3]
    rgb_channels = image_4channel[:,:,:3]

    # White Background Image
    white_background_image = np.ones_like(rgb_channels, dtype=np.uint8) * 255

    # Alpha factor
    alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = white_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    return final_image.astype(np.uint8)
	
for j in pngs:
    img = read_transparent_png(j)
	#--used to crop the input image in a specific way
    #img = img[ 16:16+64,94:94+64]
	
	#-- resizes the image to fit the 64x64px scheme
    img = cv2.resize(img,(64,64),interpolation=cv2.INTER_NEAREST )
    cv2.imwrite(j[:-3] + 'jpg', img)