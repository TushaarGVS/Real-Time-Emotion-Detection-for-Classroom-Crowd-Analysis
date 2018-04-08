import cv2
import glob

faces = "/home/tushaar/Desktop/code.fun.do/database/faces"
    
defaultXML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_default.xml")
alt2XML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt2.xml")
altXML= cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt.xml")
altTreeXML = cv2.CascadeClassifier("/home/tushaar/Desktop/code.fun.do/haarcascades/haarcascade_frontalface_alt_tree.xml")

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
    
def detect_faces(emotion):    
    itrn = 0
    image_dirs = ["/home/tushaar/Desktop/code.fun.do/database/emotions", "/home/tushaar/Desktop/code.fun.do/database/emotions_google"]

    for image_dir in image_dirs:
        images = sorted(glob.glob("%s/%s/*" %(image_dir, emotion)))
        
        for image in images:
            frame = cv2.imread(image)
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            face_default = defaultXML.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
            face_alt2 = alt2XML.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
            face_alt = altXML.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
            face_altTree = altTreeXML.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
            
            if len(face_default) == 1:
                face_features = face_default
            elif len(face_alt2) == 1:
                face_features = face_alt2
            elif len(face_alt) == 1:
                face_features = face_alt
            elif len(face_altTree) == 1:
                face_features = face_altTree
            else:
                face_features = ""
                
            for (x, y, w, h) in face_features:
                print "Face in file <%s>" %image
                grayImage = grayImage[y : y + h, x : x + w]
                
                try:
                    resizedImage = cv2.resize(grayImage, (100, 100))
                    cv2.imwrite("%s/%s/%s.jpg" %(faces, emotion, itrn), resizedImage)
                except:
                    pass
                
                itrn = itrn + 1

def extract_faces():
    for emotion in emotions:
        detect_faces(emotion)
