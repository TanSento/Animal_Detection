import cam_PIR
from keras.models import load_model
import cv2
import numpy as np
import time

WildlifeModel = load_model('TransferLearning-AlexNet-new.h5')

while True:
	img = cam_PIR.obtainImage()
	# img_array = cv2.imread(img_path)
	new_array = cv2.resize(img, (227, 227))
	#print(new_array)
	x = np.array(new_array).reshape(-1, 227, 227, 3)
	x = x/255.0

	result = np.around(WildlifeModel.predict(x),decimals = 3)
	print(result)
	#0=buffalo, 1=cheetah, 2=elephant, 3=gazelle, 4=giraffe, 5=hartebeest, 6=lionfemale&cub, 7=lionmale, 
	#8=ostrict, 9=secretarybird, 10=wildebeest, 11=zebra 
	categories = ["Buffalo", "Cheetah", "Elephant", "GazelleThomsons", "Giraffe", "Hartebeest", 
		      "Lionfemale&Cub", "Lionmale", "Ostrich", "SecretaryBird", "Wildebeest", "Zebra"]
	print('The animal type is :{}'.format(categories[np.argmax(result)]))

	time.sleep(5)
