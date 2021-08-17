# TrainYourOwnYOLO: Building a Custom Object Detector(like : Image, Text region etc.) from Scratch License: CC BY 4.0
This repo let's you train a custom image detector using the state-of-the-art YOLOv3 computer vision algorithm. This repo works with TensorFlow 2.3 and Keras 2.4.

## Pipeline Overview
To build and test your YOLO object detection algorithm follow the below steps:

1. Image Annotation
- Install Microsoft's Visual Object Tagging Tool (VoTT)
- Annotate images
2. Training
- Download pre-trained weights
- Train your custom YOLO model on annotated images
3. Inference
- Detect objects in new images and videos

## Repo structure
- 1_Image_Annotation: Scripts and instructions on annotating images
- 2_Training: Scripts and instructions on training your YOLOv3 model
- 3_Inference: Scripts and instructions on testing your trained YOLO model on new images and videos
- Data: Input Data, Output Data, Model Weights and Results
- Utils: Utility scripts used by main scripts

## Getting Started
### Google Colab Tutorial Open In Colab
With Google Colab you can skip most of the set up steps and start training your own model right away.

### Requisites
The only hard requirement is a running version of python 3.6 or 3.7. To install python 3.7 go to

- python.org/downloads
and follow the installation instructions. Note that this repo has only been tested with python 3.6 and python 3.7 thus it is recommened to use either python3.6 or python3.7.

To speed up training, it is recommended to use a GPU with CUDA support. For example on AWS you can use a p2.xlarge instance (Tesla K80 GPU with 12GB memory). Inference is very fast even on a CPU with approximately ~2 images per second. If you want to use your own machine, follow the instructions at tensorflow.org/install/gpu to install CUDA drivers. Make sure to install the correct version of CUDA and cuDNN. Or you can choose GPU in "Runtime -> change run type --> GPU" in option at top of google colab ipynb

### Installation
Setting up Virtual Environment [Linux or Mac]
Clone this repo with:

git clone https://github.com/Vipendra-pal-rajput/Text-and-image-detection-using-YoloV3
cd Text-and-image-detection-using-YoloV3/

Create Virtual (Linux/Mac) Environment:

python3 -m venv env
source env/bin/activate
Make sure that, from now on, you run all commands from within your virtual environment.

Setting up Virtual Environment [Windows]
Use the Github Desktop GUI to clone this repo to your local machine. Navigate to the TrainYourOwnYOLO project folder and open a power shell window by pressing Shift + Right Click and selecting Open PowerShell window here in the drop-down menu.

Create Virtual (Windows) Environment:

py -m venv env
.\env\Scripts\activate
PowerShell Make sure that, from now on, you run all commands from within your virtual environment.

Install Required Packages [Windows, Mac or Linux]
Install required packages (from within your virtual environment) via:

pip install -r requirements.txt
If this fails, you may have to upgrade your pip version first with pip install pip --upgrade.

Quick Start (Inference only)
To test the object detector on test images located in Text-and-image-detection-using-YoloV3/Data/Source_Images/Test_Images run the Minimal_Example.py script in the root folder with:

python Minimal_Example.py
And if you have video file and you want to detect object then go to test images or video file located in Text-and-image-detection-using-YoloV3/Data/Source_Images/Test_Images then Switch to diretory Text-and-image-detection-using-YoloV3/3_Inference for run the Detector.py script in the root folder with:

python Detector.py
The outputs are saved in Text-and-image-detection-using-YoloV3/Data/Source_Images/Test_Image_Detection_Results. This includes:

multiple object(Image, text_region, stamp, Signature) with bounding boxes around object with confidence scores and
Detection_Results.csv file with file names and locations of bounding boxes.
If you want to detect Object in your own pictures, replace the images in Data/Source_Images/Test_Images with your own images.

Full Start (Training and Inference)
To train your own custom YOLO object detector please follow the instructions detailed in the three numbered subfolders of this repo:

1_Image_Annotation,
2_Training and
3_Inference.
To make everything run smoothly it is highly recommended to keep the original folder structure of this repo!

Each *.py script has various command line options that help tweak performance and change things such as input and output directories. All scripts are initialized with good default values that help accomplish all tasks as long as the original folder structure is preserved. To learn more about available command line options of a python script <script_name.py> run:

python <script_name.py> -h
NEW: Weights and Biases
TrainYourOwnYOLO supports Weights & Biases to track your experiments online. Sign up at wandb.ai to get an API key and run:

wandb -login <API_KEY>
where <API_KEY> is your Weights & Biases API key.
