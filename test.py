from detector import ObjectDetector
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to an image for object detection...")
args = vars(ap.parse_args())

detector = ObjectDetector(loadPath="model.svm")
imagePath = args["image"]
image = cv2.imread(imagePath)
detector.detect(image,annotate="Face Mask")