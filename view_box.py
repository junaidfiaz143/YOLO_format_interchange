import numpy as np
import cv2
import os

def read(file):
	read_file = open(path + "\\" + file, "r")
	data = read_file.read()
	read_file.close()
	return data

def from_yolo_to_cor(box, shape):
	img_h, img_w, _ = shape
	# x1, y1 = ((x + witdth)/2)*img_width, ((y + height)/2)*img_height
	# x2, y2 = ((x - witdth)/2)*img_width, ((y - height)/2)*img_height
	x1, y1 = int((box[0] + box[2]/2)*img_w), int((box[1] + box[3]/2)*img_h)
	x2, y2 = int((box[0] - box[2]/2)*img_w), int((box[1] - box[3]/2)*img_h)
	return x1, y1, x2, y2

def create_annotatoin(filename, annotation):
	write_file = open(filename, "a+")
	data = write_file.write(annotation+"\n")
	write_file.close()

path = "dataset"

annotations = os.listdir(path)

for ann in annotations:
	if ann.split(".")[1] == "txt":
		data = read(ann)
		box = [float(i) for i in data.split(" ")[1:5]] 
		image = cv2.imread(path + "\\" + ann.split(".")[0] + ".jpg")
		x, y, w, h = from_yolo_to_cor(box, image.shape)
		image = cv2.rectangle(image, (x, y), (w, h), (255, 0, 0), 1)
		cv2.imshow("", image)
		cv2.waitKey(0)