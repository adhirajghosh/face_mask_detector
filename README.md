# Face Mask Detector
Object Detection Model to accurately detect whether a person in an image is wearing a face mask or not.

This model utilises the Histogram of Oriented Gradients (HOG) algorithm in order to establish a feature understanding of the training images. The core theory for this repository has been inspired by the [Face recognition using Histograms of Oriented Gradients](https://d1wqtxts1xzle7.cloudfront.net/42736520/5419ded60cf203f155ae1415.pdf?1455645353=&response-content-disposition=inline%3B+filename%3DFace_recognition_using_Histograms_of_Ori.pdf&Expires=1606743825&Signature=Y3~wag6VlICGOKV7jrUVJQxxoI-xrPkpqbc8ENunMqMNze8mjC7gX4J6XMJO6jOzGMXcH-yGlM1IUE8zseoVSMMtUumOcAmKmZjP5RIpwkVKtVWl0~RynppPZICM3ijFfIkjCiQE~yvGP6hjjbDL-7-sTkD6If6EqGr2eoNX7SIh0JHX12sy5W82p9ZeMf3SV8sp8MbEu7azrefRJ4kvo7wvhQAFe3VeCVDOR08Dk9cCEJFEbTXaDBHNdKUZSin0v18b0hxZnDnSlKa2yDbibETrRmoqnIj8RxTwR0d8vTSREvr6xicK1m~WMVYLp3QdhwlPA1zJ8GJ-QaceFOxgkQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) paper. 

This repository contains the annotations and trained model for a sample dataset of people wearing masks and a good model should be able to distinguish a person wearing a face mask from someone who is not. The annotations and model is stored as annotations.npy and model.svm respectively. The images used for training can be accessed [here](https://drive.google.com/drive/folders/1TKa_WhWxJL9Cvr4rh2sKiPhJWf5oUuhj?usp=sharing). The model works well for the test images provided for the task. However if you wish to scale-up the task, feel free to generate your own dataset and create your manual annotations and training model.


Command to install the required libraries:

 	pip install -r requirements.txt  

## Project Structure
**Object Detector**

1. annot.py- script to annotate each image using a box selector.
2. box_selector.py- contains BoxSelector class which helps us to annotate and create a bounding box of the specific region of the image that is relevant to the task.
3. detector.py- script for training and detecting objects.
4. train.py - script used for training the object detector and generating the model.
5. test.py- script to detect face masks in untrained images.

**Other files**
1. annotations.npy - Stores the annotations of training images.
2. images.npy - Stores the path of the training images.
3. model.svm - Stores the trained model used to detect face masks in test images.

## Usage

    git clone https://github.com/adhirajghosh/face_mask_detector
    cd face_mask_detector
    
### Annotate Training Images
    python annot.py --dataset images/ --annotations annotations.npy --images images.npy

### Training the model
    python train.py --annotations annotations.npy --images images.npy --detector model.svm
    
### Evaluation
    python test.py --detector model.svm --image <insert test image path here> --annotate Face_Mask
