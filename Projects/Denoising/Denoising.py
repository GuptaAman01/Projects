import cv2                       # For plotting or using functions to denoise the image
from PIL import Image            # For plotting the image or displaying the image
import numpy as np               # For Arithmetic Calculations
import matplotlib.pyplot as plt  # For plotting
from skimage.restoration import estimate_sigma  # For finding the standard deviation of the image
import time
import os

def denoise_more(x,y):                   # Function for image denoising
    img = cv2.cvtColor(np.array(x), cv2.COLOR_RGB2BGR)               # For converting Image from PIL to cv2 format
    kernel = np.ones((2,2), np.uint8)  # Kernel used for denoising
    kernel1 = np.ones((1,1), np.uint8) # Kernel used for denoising
    bilateral = cv2.bilateralFilter(img, 100, 100, 275)                      # Applying Bilateral Filter  
    erosion_image = cv2.erode(bilateral, kernel, iterations=1)               # Applying Erosion in bilateral image
    bilateral = cv2.bilateralFilter(erosion_image, 100, 100, 275)            # Applying Bilateral in Erosed image
    dilation_image = cv2.dilate(bilateral, kernel1, iterations=1)            # Applying Dilation in Bilateral image
    ret, thresh3 = cv2.threshold(dilation_image, 230, 255, cv2.THRESH_TRUNC) # Truncated Threshold
    image = Image.fromarray(cv2.cvtColor(thresh3,cv2.COLOR_BGR2RGB))
    image.save('Denoised_image/'+y)

def denoise_avg(x,y):     # Function for image denoising
    img = cv2.cvtColor(np.array(x), cv2.COLOR_RGB2BGR)   # For converting Image from PIL to cv2 format
    kernel = np.ones((2,2), np.uint8) # Kernel used for denoising
    kernel1 = np.ones((1,1), np.uint8) # Kernel used for denoising
    bilateral = cv2.bilateralFilter(img, 100, 100, 275)   # Applying Bilateral Filter  
    erosion_image = cv2.erode(bilateral, kernel, iterations=1) # Applying Erosion in bilateral image
    bilateral = cv2.bilateralFilter(erosion_image, 100, 100, 275)   # Applying Bilateral Filter
    ret, thresh3 = cv2.threshold(bilateral, 230, 255, cv2.THRESH_TRUNC) # Truncated Threshold 
    image = Image.fromarray(cv2.cvtColor(thresh3,cv2.COLOR_BGR2RGB))
    image.save('Denoised_image/'+y)

def denoise_less(x,y):                    # Function for image denoising
    img = cv2.cvtColor(np.array(x), cv2.COLOR_RGB2BGR)              # For converting Image from PIL to cv2 format
    kernel = np.ones((2,2), np.uint8)   # Kernel used for denoising
    kernel1 = np.ones((1,1), np.uint8)  # Kernel used for denoising
    bilateral = cv2.bilateralFilter(img, 100, 100, 275)                     # Applying Bilateral Filter 
    erosion_image = cv2.erode(bilateral, kernel, iterations=1)              # Applying Erosion in bilateral image
    ret, thresh3 = cv2.threshold(erosion_image, 200, 255, cv2.THRESH_TRUNC) # Truncated Threshold 
    image = Image.fromarray(cv2.cvtColor(thresh3,cv2.COLOR_BGR2RGB))
    image.save('Denoised_image/'+y)

PATH = 'Original_image/'        # Path of the Directory where images are stored
start = time.time()
for filename in os.listdir(PATH):
  img = Image.open(os.path.join(PATH, filename))
  i = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) 
  a = i.shape                               # Checking shape of the image
  std=estimate_sigma(i, multichannel=True, average_sigmas=True).round(2)  # Standard Deviation of the image
  print("Standard Deviation of the image:",std)
  print("Size of the Image:",a)             # Printing shape of the image

  if a < (500, 600, 10):                    # Applying condition for image to be denoised
      start1 = time.time()
      denoise_less(img,filename)                    # For small image shape
      print("Present Noise : Less")
      end1 = time.time()
      print("Time taken in image processing:",end1-start1,"sec")
      print('\n')
  else:                                     # For large image shape
      if (0.06 <= std <= 0.5):              # If value of standard deviation is less than 0.3 then denoise_less will be called
          start2 = time.time()
          denoise_less(img,filename)      
          print("Present Noise : Less")       
          end2 = time.time()
          print("Time taken in image processing:",end2-start2,"sec")
          print('\n')
      elif (0.51 <=std<= 0.9):               # If value of standard deviation is between 0.3 to 0.4 the denoise_avg will be called
          start3 = time.time()
          denoise_avg(img,filename)
          print("Present Noise : Average")
          end3 = time.time()
          print("Time taken in image processing:",end3-start3,"sec")
          print("\n")
      elif (std <= 0.05):                   # If value of standard deviation is less than 0.05 then it will pass
          print("The Image has no noise.")
          print('\n')
          image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
          image.save('Denoised_image/'+y)
          pass                
      else:                                 # If value of standard deviation is more than 0.4 the denoise_more will be called
          start4 = time.time()
          denoise_more(img,filename)  
          print("Present Noise : High")
          end4 = time.time()
          print("Time taken in image processing:",end4-start4,"sec")
          print('\n')
end = time.time()
tme = (end-start)/60

print("Total time taken in processing all images:",tme,"min")