from detector import ObjectDetector
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d","--detector",default=None,help="path to save the trained detector...")
args = vars(ap.parse_args())

annots = np.load("annot.npy")
imagePaths = np.load("images.npy")

detector = ObjectDetector(options=True)

detector.fit(imagePaths,annots,visualize=True,savePath=args["detector"])
