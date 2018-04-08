import cv2
import os
import time
import glob
import capture_realtime as cr

itrn = 0
faces = "/home/tushaar/Desktop/code.fun.do/captures/faces"

defaultXML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_default.xml")
alt2XML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt2.xml")
altXML= cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt.xml")
altTreeXML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt_tree.xml")

def deleteAllFiles(directory):
    filelist = [f for f in os.listdir(directory)]
    for f in filelist:
        os.remove(os.path.join(directory, f))

def viola_jones(image):
    frame = cv2.imread(image)
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_default = defaultXML.detectMultiScale(grayImage, scaleFactor=1.2, minNeighbors = 5)
    face_alt2 = alt2XML.detectMultiScale(grayImage, scaleFactor=1.2, minNeighbors = 5)
    face_alt = altXML.detectMultiScale(grayImage, scaleFactor=1.2, minNeighbors = 5)
    face_altTree = altTreeXML.detectMultiScale(grayImage, scaleFactor=1.2, minNeighbors = 5)
    
    if len(face_default) != 0:
        face_features = face_default
    elif len(face_alt2) != 0:
        face_features = face_alt2
    elif len(face_alt) != 0:
        face_features = face_alt
    elif len(face_altTree) != 0:
        face_features = face_altTree
    else:
        face_features = ""

    print "Number of faces captured: %s" %len(face_features)
    global itrn
    
    for (x, y, w, h) in face_features:
        sub_face = grayImage[y : y + h, x : x + w]
        
        try:
            resizedImage = cv2.resize(sub_face, (100, 100))
            cv2.imwrite("%s/%s.jpg" %(faces, itrn), resizedImage)
        except:
            pass
        
        itrn = itrn + 1
         
def preprocessing():   
    deleteAllFiles(faces)
    '''
    # In case of realtime detection, capture row-by-row images using:
    deleteAllFiles("/home/tushaar/Desktop/code.fun.do/captures/images/")
    image = cr.capture_image()
    '''

    images = sorted(glob.glob("/home/tushaar/Desktop/code.fun.do/captures/images/*"))
    for image in images:
        viola_jones(image)
