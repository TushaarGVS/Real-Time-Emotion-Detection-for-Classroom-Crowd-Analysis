import cv2
import glob
import time
import random
import numpy as np

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
fisherface = cv2.createFisherFaceRecognizer()

class custom_imread:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

def get_training_labels():
    training_data, training_labels = [], []
    testing_data, testing_images  = [], []

    for emotion in emotions:
        training = sorted(glob.glob("/home/tushaar/Desktop/code.fun.do/database/faces/%s/*" %emotion))
        
        for item in training:
            image = cv2.imread(item)
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            training_data.append(grayImage)
            training_labels.append(emotions.index(emotion))

    testing = sorted(glob.glob("/home/tushaar/Desktop/code.fun.do/captures/faces/*"))
    
    for item in testing:
        image = custom_imread(item)
        grayImage = cv2.cvtColor(image.img, cv2.COLOR_BGR2GRAY)
        testing_images.append(str(image))
        testing_data.append(grayImage)
        
    return training_data, training_labels, testing_data, testing_images

def classify_fisherface():
    classification = dict.fromkeys([emotions[0], emotions[1], emotions[2], emotions[3], emotions[4], emotions[5], emotions[6],  emotions[7]], 0)
    training_data, training_labels, testing_data, testing_images = get_training_labels()
    print "Training using Fisher Face Classifier"
    fisherface.train(training_data, np.asarray(training_labels))

    print "Testing using Fisher Face Classifier"
    itrn = 0
    for image in testing_data:
        prediction, confidence = fisherface.predict(image)
        print testing_images[itrn]
        print "%s: %s, confidence: %s" %(prediction, emotions[prediction], confidence)
        classification[emotions[prediction]] = classification[emotions[prediction]] + 1
        itrn = itrn + 1
        print 40 * "+" + "\n"

    for (key, value) in classification.items():
        classification[key] = round((value * 100)/float(len(testing_data)), 2)

    overall_emotion_value = - (5 * classification['fear']) - (4 * classification['anger']) - (3 * classification['contempt']) - (2 * classification['sadness']) - classification['disgust'] + classification['neutral'] + (4 * classification['happy']) + (5 * classification['surprise'])
    return classification, overall_emotion_value, time.strftime("%m.%d.%y-%H:%M:%S")
