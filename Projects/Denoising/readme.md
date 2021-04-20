# Image_denoising : Remove Noise from image.

## Requisites python and packages: 
1. python 3.9
2. opencv 4.1
3. PIL(python image library)
4. Numpy
5. skimage.restoration import estimate_sigma
6. os
7. time 

## Overview :
To test your own images follow the below steps:

* Step 1: Make a folder name Denoising
		1. Inside that folder first copy the Denoising.py file
		2. Also, make folder name Denoised_image and Original_image

* Step 2: Copy all the images in Original_image which has to be denoised.

* Step 3: Run on terminal type : python Denoising.py.

* Step 4: The outputs will be saved in "Denoised_image" directory.

## There are two folder directory:

1. Original_image  -- It consist input images
2. Denoised_image  -- Contain output images

* To give path for input images : "C:\Users\vipen\Desktop\Denoising\Original_image"
* To give path for output images : "C:\Users\vipen\Desktop\Denoising\Denoised_image"

* Note:

Time taken in processing an image is mainly depends on image resolution not on image size.

* On 6GB RAM PC : 
1. (420, 540, 3) = 4.5 - 4.8 sec
2. (258, 540, 3) = 2.1 - 2.3 sec
3. (2200, 1700, 3) = 60 sec
4. (2338, 1654, 3) = 60 - 62 sec

* On 16 GB RAM PC : 
1. (420, 540, 3) = 1.7 - 1.9 sec
2. (258, 540, 3) = 1.4 - 1.7 sec
3. (2338, 1654, 3) = 45 - 47 sec


## Input Images or images in Original_image directory

![Webp net-gifmaker](https://user-images.githubusercontent.com/78907282/115428745-572aad80-a220-11eb-95dd-d22bfbb00802.gif)

## Output Images or images in Denoise_image directory

![Webp net-gifmaker (1)](https://user-images.githubusercontent.com/78907282/115429148-c1dbe900-a220-11eb-94d1-bd2431a00b25.gif)

