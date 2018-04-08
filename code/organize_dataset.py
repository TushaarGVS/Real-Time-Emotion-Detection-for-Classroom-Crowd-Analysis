import glob
from shutil import copyfile

def segregate_files():
    emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
    
    participantImages = "/home/tushaar/Desktop/code.fun.do/database/CK+/cohn-kanade-images"
    participantIDs = sorted(glob.glob("/home/tushaar/Desktop/code.fun.do/database/CK+/Emotion/*"))
    
    for participantID in participantIDs:
        participant = "%s" %participantID[-4:]
        for sessionID in sorted(glob.glob("%s/*" %participantID)):
            for fileID in sorted(glob.glob("%s/*" %sessionID)):
                f = open(fileID, "r")
                emotion = int(float(f.readline()))
                
                src_emotion_path = sorted(glob.glob("%s/%s/%s/*" %(participantImages, participant, sessionID[-3:])))[-1]
                src_neutral_path = sorted(glob.glob("%s/%s/%s/*" %(participantImages, participant, sessionID[-3:])))[0]
                
                dest_neutral_path = "/home/tushaar/Desktop/code.fun.do/database/emotions/neutral/" + src_neutral_path[75:]
                dest_emotion_path = "/home/tushaar/Desktop/code.fun.do/database/emotions/" + emotions[emotion] + "/" + src_emotion_path[75:]
                
                copyfile(src_neutral_path, dest_neutral_path)
                copyfile(src_emotion_path, dest_emotion_path)
